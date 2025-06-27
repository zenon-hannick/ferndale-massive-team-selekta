import pytest
import tempfile
import os
from app.models.player import Player, PlayerAttributes
from app.models.game import Team, Game, GameScore
from app.services.database import DatabaseService


class TestDatabaseService:
    """Test cases for the DatabaseService"""
    
    def test_create_database(self):
        """Test creating a new database"""
        # Arrange
        with tempfile.NamedTemporaryFile(suffix='.db', delete=False) as tmp:
            db_path = tmp.name
        
        try:
            # Act
            db = DatabaseService(db_path)
            
            # Assert
            assert os.path.exists(db_path)
            assert db is not None
        finally:
            # Cleanup
            if os.path.exists(db_path):
                os.unlink(db_path)
    
    def test_save_and_load_player(self):
        """Test saving and loading a player"""
        # Arrange
        with tempfile.NamedTemporaryFile(suffix='.db', delete=False) as tmp:
            db_path = tmp.name
        
        try:
            db = DatabaseService(db_path)
            player = Player(
                name="Test Player",
                attributes=PlayerAttributes(attacking=7, defending=6, goalkeeping=3, energy=8)
            )
            
            # Act
            db.save_player(player)
            loaded_player = db.get_player("Test Player")
            
            # Assert
            assert loaded_player is not None
            assert loaded_player.name == "Test Player"
            assert loaded_player.attributes.attacking == 7
        finally:
            if os.path.exists(db_path):
                os.unlink(db_path)
    
    def test_save_and_load_game(self):
        """Test saving and loading a game"""
        # Arrange
        with tempfile.NamedTemporaryFile(suffix='.db', delete=False) as tmp:
            db_path = tmp.name
        
        try:
            db = DatabaseService(db_path)
            red_team = Team(
                name="Red",
                players=[
                    Player(name="Player1", attributes=PlayerAttributes(attacking=7, defending=6, goalkeeping=3, energy=8))
                ]
            )
            yellow_team = Team(
                name="Yellows",
                players=[
                    Player(name="Player2", attributes=PlayerAttributes(attacking=6, defending=7, goalkeeping=4, energy=7))
                ]
            )
            game = Game(
                date="2024-01-15",
                red_team=red_team,
                yellow_team=yellow_team,
                score=GameScore(red_score=3, yellow_score=2)
            )
            
            # Act
            db.save_game(game)
            loaded_games = db.get_all_games()
            
            # Assert
            assert len(loaded_games) == 1
            loaded_game = loaded_games[0]
            assert loaded_game.date == "2024-01-15"
            assert loaded_game.score.red_score == 3
            assert loaded_game.score.yellow_score == 2
        finally:
            if os.path.exists(db_path):
                os.unlink(db_path)
    
    def test_get_all_players(self):
        """Test getting all saved players"""
        # Arrange
        with tempfile.NamedTemporaryFile(suffix='.db', delete=False) as tmp:
            db_path = tmp.name
        
        try:
            db = DatabaseService(db_path)
            player1 = Player(name="Player1", attributes=PlayerAttributes(attacking=7, defending=6, goalkeeping=3, energy=8))
            player2 = Player(name="Player2", attributes=PlayerAttributes(attacking=6, defending=7, goalkeeping=4, energy=7))
            
            # Act
            db.save_player(player1)
            db.save_player(player2)
            all_players = db.get_all_players()
            
            # Assert
            assert len(all_players) == 2
            player_names = [p.name for p in all_players]
            assert "Player1" in player_names
            assert "Player2" in player_names
        finally:
            if os.path.exists(db_path):
                os.unlink(db_path)
    
    def test_update_player(self):
        """Test updating an existing player"""
        # Arrange
        with tempfile.NamedTemporaryFile(suffix='.db', delete=False) as tmp:
            db_path = tmp.name
        
        try:
            db = DatabaseService(db_path)
            player = Player(name="Test Player", attributes=PlayerAttributes(attacking=7, defending=6, goalkeeping=3, energy=8))
            db.save_player(player)
            
            # Update player
            updated_player = Player(name="Test Player", attributes=PlayerAttributes(attacking=8, defending=7, goalkeeping=4, energy=9))
            
            # Act
            db.update_player(updated_player)
            loaded_player = db.get_player("Test Player")
            
            # Assert
            assert loaded_player.attributes.attacking == 8
            assert loaded_player.attributes.defending == 7
        finally:
            if os.path.exists(db_path):
                os.unlink(db_path) 