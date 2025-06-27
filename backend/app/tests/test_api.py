import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


class TestPlayerAPI:
    """Test cases for Player API endpoints"""
    
    def test_create_player(self):
        """Test creating a new player"""
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
        response = client.post("/players/", json=player_data)
        
        # Assert
        assert response.status_code == 201
        data = response.json()
        assert data["name"] == "John Doe"
        assert data["attributes"]["attacking"] == 7
    
    def test_get_players(self):
        """Test getting all players"""
        # Act
        response = client.get("/players/")
        
        # Assert
        assert response.status_code == 200
        assert isinstance(response.json(), list)


class TestTeamBalancingAPI:
    """Test cases for Team Balancing API endpoints"""
    
    def test_balance_teams(self):
        """Test balancing teams with players"""
        # Arrange
        players_data = [
            {
                "name": f"Player {i}",
                "attributes": {
                    "attacking": 7,
                    "defending": 6,
                    "goalkeeping": 3,
                    "energy": 8
                }
            }
            for i in range(1, 11)  # 10 players
        ]
        
        # Act
        response = client.post("/teams/balance", json={"players": players_data})
        
        # Assert
        assert response.status_code == 200
        data = response.json()
        assert "red_team" in data
        assert "yellow_team" in data
        assert len(data["red_team"]["players"]) == 5
        assert len(data["yellow_team"]["players"]) == 5


class TestGameRecordingAPI:
    """Test cases for Game Recording API endpoints"""
    
    def test_record_game(self):
        """Test recording a new game"""
        # Arrange
        game_data = {
            "date": "2024-01-15",
            "red_team": {
                "name": "Red",
                "players": [
                    {
                        "name": "Player1",
                        "attributes": {
                            "attacking": 7,
                            "defending": 6,
                            "goalkeeping": 3,
                            "energy": 8
                        }
                    }
                ]
            },
            "yellow_team": {
                "name": "Yellows",
                "players": [
                    {
                        "name": "Player2",
                        "attributes": {
                            "attacking": 6,
                            "defending": 7,
                            "goalkeeping": 4,
                            "energy": 7
                        }
                    }
                ]
            },
            "score": {
                "red_score": 3,
                "yellow_score": 2
            }
        }
        
        # Act
        response = client.post("/games/", json=game_data)
        
        # Assert
        assert response.status_code == 201
        data = response.json()
        assert data["date"] == "2024-01-15"
        assert data["score"]["red_score"] == 3
        assert data["score"]["yellow_score"] == 2
    
    def test_get_game_history(self):
        """Test getting game history"""
        # Act
        response = client.get("/games/")
        
        # Assert
        assert response.status_code == 200
        assert isinstance(response.json(), list)
    
    def test_get_player_stats(self):
        """Test getting player performance statistics"""
        # Act
        response = client.get("/players/Player1/stats")
        
        # Assert
        assert response.status_code == 200
        data = response.json()
        assert "total_games" in data
        assert "wins" in data
        assert "losses" in data
        assert "win_rate" in data 