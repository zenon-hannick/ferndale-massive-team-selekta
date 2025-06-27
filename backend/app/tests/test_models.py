import pytest
from pydantic import ValidationError
from app.models.player import Player, PlayerAttributes
from app.models.game import Game, Team, GameScore


class TestPlayer:
    """Test cases for the Player model"""
    
    def test_player_creation_with_valid_data(self):
        """Test that a player can be created with valid data"""
        # Arrange
        player_data = {
            "name": "John Doe",
            "attributes": {
                "attacking": 7,
                "defending": 6,
                "goalkeeping": 3,
                "energy": 8
            }
        }
        
        # Act
        player = Player(**player_data)
        
        # Assert
        assert player.name == "John Doe"
        assert player.attributes.attacking == 7
        assert player.attributes.defending == 6
        assert player.attributes.goalkeeping == 3
        assert player.attributes.energy == 8
    
    def test_player_attributes_validation(self):
        """Test that player attributes must be between 1 and 10"""
        # Arrange & Act & Assert
        with pytest.raises(ValidationError):
            Player(
                name="Invalid Player",
                attributes={
                    "attacking": 11,  # Invalid: > 10
                    "defending": 6,
                    "goalkeeping": 3,
                    "energy": 8
                }
            )
    
    def test_player_name_required(self):
        """Test that player name is required"""
        # Arrange & Act & Assert
        with pytest.raises(ValidationError):
            Player(
                attributes={
                    "attacking": 7,
                    "defending": 6,
                    "goalkeeping": 3,
                    "energy": 8
                }
            )


class TestGame:
    """Test cases for the Game model"""
    
    def test_game_creation_with_valid_data(self):
        """Test that a game can be created with valid data"""
        # Arrange
        red_team = Team(
            name="Red",
            players=[
                Player(
                    name="Player 1",
                    attributes=PlayerAttributes(attacking=7, defending=6, goalkeeping=3, energy=8)
                )
            ]
        )
        
        yellow_team = Team(
            name="Yellows",
            players=[
                Player(
                    name="Player 2",
                    attributes=PlayerAttributes(attacking=6, defending=7, goalkeeping=4, energy=7)
                )
            ]
        )
        
        game_data = {
            "date": "2024-01-15",
            "red_team": red_team,
            "yellow_team": yellow_team,
            "score": GameScore(red_score=3, yellow_score=2)
        }
        
        # Act
        game = Game(**game_data)
        
        # Assert
        assert game.date == "2024-01-15"
        assert game.red_team.name == "Red"
        assert game.yellow_team.name == "Yellows"
        assert game.score.red_score == 3
        assert game.score.yellow_score == 2
    
    def test_game_score_validation(self):
        """Test that game scores must be non-negative"""
        # Arrange & Act & Assert
        with pytest.raises(ValidationError):
            GameScore(red_score=-1, yellow_score=2) 