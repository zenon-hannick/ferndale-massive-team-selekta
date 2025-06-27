from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel
from app.models.player import Player
from app.models.game import Team, Game, GameScore
from app.services.team_balancer import TeamBalancer
from app.services.game_recorder import GameRecorder
from app.services.database import DatabaseService
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Football Team Selector",
    description="An application for creating balanced football teams",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize database service
database = DatabaseService()
game_recorder = GameRecorder()


class BalanceTeamsRequest(BaseModel):
    """Request model for team balancing"""
    players: List[Player]


class RecordGameRequest(BaseModel):
    """Request model for recording a game"""
    date: str
    red_team: Team
    yellow_team: Team
    score: GameScore


@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "Football Team Selector API"}


@app.post("/players/", status_code=201)
async def create_player(player: Player):
    """Create a new player"""
    database.save_player(player)
    return player


@app.get("/players/", response_model=List[Player])
async def get_players():
    """Get all players"""
    return database.get_all_players()


@app.put("/players/{player_name}")
async def update_player(player_name: str, player: Player):
    """Update an existing player"""
    # Ensure the player name in the URL matches the player data
    if player.name != player_name:
        raise HTTPException(status_code=400, detail="Player name in URL must match player data")
    
    # Check if player exists
    existing_player = database.get_player(player_name)
    if not existing_player:
        raise HTTPException(status_code=404, detail="Player not found")
    
    # Update the player
    database.update_player(player)
    return player


@app.get("/players/{player_name}/stats")
async def get_player_stats(player_name: str):
    """Get performance statistics for a player"""
    stats = game_recorder.get_player_performance_stats(player_name)
    return stats


@app.post("/teams/balance")
async def balance_teams(request: BalanceTeamsRequest):
    """Balance players into two teams"""
    try:
        balancer = TeamBalancer()
        red_team, yellow_team = balancer.balance_teams(request.players)
        return {
            "red_team": red_team,
            "yellow_team": yellow_team
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/games/", status_code=201)
async def record_game(request: RecordGameRequest):
    """Record a new game"""
    game = game_recorder.record_game(
        date=request.date,
        red_team=request.red_team,
        yellow_team=request.yellow_team,
        score=request.score
    )
    return game


@app.get("/games/", response_model=List[Game])
async def get_game_history():
    """Get all recorded games"""
    return game_recorder.get_game_history() 