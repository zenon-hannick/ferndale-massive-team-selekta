from pydantic import BaseModel, Field, ConfigDict
from typing import List
from .player import Player


class Team(BaseModel):
    """Team model"""
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "name": "Red",
                "players": []
            }
        }
    )
    
    name: str = Field(..., description="Team name (Red or Yellows)")
    players: List[Player] = Field(default_factory=list, description="List of players in the team")


class GameScore(BaseModel):
    """Game score model"""
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "red_score": 3,
                "yellow_score": 2
            }
        }
    )
    
    red_score: int = Field(..., ge=0, description="Red team score")
    yellow_score: int = Field(..., ge=0, description="Yellow team score")


class Game(BaseModel):
    """Game model"""
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "date": "2024-01-15",
                "red_team": {"name": "Red", "players": []},
                "yellow_team": {"name": "Yellows", "players": []},
                "score": {"red_score": 3, "yellow_score": 2}
            }
        }
    )
    
    date: str = Field(..., description="Game date (YYYY-MM-DD format)")
    red_team: Team
    yellow_team: Team
    score: GameScore 