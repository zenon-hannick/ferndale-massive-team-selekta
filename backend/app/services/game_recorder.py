from typing import List, Dict, Any
from app.models.game import Game, Team, GameScore


class GameRecorder:
    """Service for recording games and analyzing historical data"""
    
    def __init__(self):
        # In-memory storage for development (will be replaced with database)
        self.games: List[Game] = []
    
    def record_game(self, date: str, red_team: Team, yellow_team: Team, score: GameScore) -> Game:
        """
        Record a new game with teams and score.
        
        Args:
            date: Game date (YYYY-MM-DD format)
            red_team: Red team
            yellow_team: Yellow team
            score: Game score
            
        Returns:
            Recorded game
        """
        game = Game(
            date=date,
            red_team=red_team,
            yellow_team=yellow_team,
            score=score
        )
        self.games.append(game)
        return game
    
    def get_game_history(self) -> List[Game]:
        """
        Get all recorded games.
        
        Returns:
            List of games sorted by date (oldest first)
        """
        return sorted(self.games, key=lambda game: game.date)
    
    def get_player_performance_stats(self, player_name: str) -> Dict[str, Any]:
        """
        Get performance statistics for a specific player.
        
        Args:
            player_name: Name of the player
            
        Returns:
            Dictionary with performance statistics
        """
        total_games = 0
        wins = 0
        losses = 0
        
        for game in self.games:
            # Check if player was in red team
            red_players = [p.name for p in game.red_team.players]
            yellow_players = [p.name for p in game.yellow_team.players]
            
            if player_name in red_players:
                total_games += 1
                if game.score.red_score > game.score.yellow_score:
                    wins += 1
                else:
                    losses += 1
            elif player_name in yellow_players:
                total_games += 1
                if game.score.yellow_score > game.score.red_score:
                    wins += 1
                else:
                    losses += 1
        
        win_rate = wins / total_games if total_games > 0 else 0.0
        
        return {
            "total_games": total_games,
            "wins": wins,
            "losses": losses,
            "win_rate": win_rate
        }
    
    def get_team_correlation_stats(self) -> Dict[str, Any]:
        """
        Get team correlation statistics to identify strong partnerships.
        
        Returns:
            Dictionary with team correlation data
        """
        # This will be implemented in the next iteration
        # For now, return basic structure
        return {
            "strong_partnerships": [],
            "weak_partnerships": [],
            "recommendations": []
        } 