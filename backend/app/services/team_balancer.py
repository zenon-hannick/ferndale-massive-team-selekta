from typing import List, Tuple
from app.models.player import Player
from app.models.game import Team


class TeamBalancer:
    """Service for balancing players into two teams"""
    
    def balance_teams(self, players: List[Player]) -> Tuple[Team, Team]:
        """
        Balance available players into two teams of equal size.
        
        Args:
            players: List of all players
            
        Returns:
            Tuple of (red_team, yellow_team)
        """
        # Filter only available players
        available_players = [player for player in players if player.available]
        
        # Determine team size based on number of available players
        if len(available_players) == 10:
            team_size = 5
        elif len(available_players) == 12:
            team_size = 6
        else:
            raise ValueError(f"Expected 10 or 12 available players, got {len(available_players)}")
        
        # Calculate total skill score for each player
        player_scores = []
        for player in available_players:
            total_score = (player.attributes.attacking + 
                          player.attributes.defending + 
                          player.attributes.goalkeeping + 
                          player.attributes.energy)
            player_scores.append((player, total_score))
        
        # Sort players by skill score (highest first)
        player_scores.sort(key=lambda x: x[1], reverse=True)
        
        # Simple alternating distribution: Red gets 1st, 3rd, 5th, 7th, 9th
        # Yellow gets 2nd, 4th, 6th, 8th, 10th
        red_players = []
        yellow_players = []
        
        for i, (player, score) in enumerate(player_scores):
            if i % 2 == 0:  # Even indices (0, 2, 4, 6, 8) go to Red
                red_players.append(player)
            else:  # Odd indices (1, 3, 5, 7, 9) go to Yellow
                yellow_players.append(player)
        
        # Create teams
        red_team = Team(name="Red", players=red_players)
        yellow_team = Team(name="Yellows", players=yellow_players)
        
        return red_team, yellow_team 