import pytest
from app.models.player import Player, PlayerAttributes
from app.models.game import Team, Game, GameScore
from app.services.team_balancer import TeamBalancer
from app.services.game_recorder import GameRecorder


class TestTeamBalancer:
    """Test cases for the TeamBalancer service"""
    
    def test_balance_teams_with_10_players(self):
        """Test that 10 players are balanced into two teams of 5"""
        # Arrange
        players = [
            Player(name=f"Player {i}", 
                   attributes=PlayerAttributes(attacking=7, defending=6, goalkeeping=3, energy=8))
            for i in range(1, 11)
        ]
        
        balancer = TeamBalancer()
        
        # Act
        red_team, yellow_team = balancer.balance_teams(players)
        
        # Assert
        assert len(red_team.players) == 5
        assert len(yellow_team.players) == 5
        assert red_team.name == "Red"
        assert yellow_team.name == "Yellows"
    
    def test_balance_teams_with_12_players(self):
        """Test that 12 players are balanced into two teams of 6"""
        # Arrange
        players = [
            Player(name=f"Player {i}", 
                   attributes=PlayerAttributes(attacking=7, defending=6, goalkeeping=3, energy=8))
            for i in range(1, 13)
        ]
        
        balancer = TeamBalancer()
        
        # Act
        red_team, yellow_team = balancer.balance_teams(players)
        
        # Assert
        assert len(red_team.players) == 6
        assert len(yellow_team.players) == 6
        assert red_team.name == "Red"
        assert yellow_team.name == "Yellows"
    
    def test_intelligent_team_balancing(self):
        """Test that teams are balanced based on player attributes"""
        # Arrange - Create players with varying skill levels
        players = [
            Player(name="Striker", attributes=PlayerAttributes(attacking=9, defending=3, goalkeeping=1, energy=8)),
            Player(name="Defender", attributes=PlayerAttributes(attacking=3, defending=9, goalkeeping=2, energy=7)),
            Player(name="Midfielder", attributes=PlayerAttributes(attacking=7, defending=7, goalkeeping=3, energy=9)),
            Player(name="Goalkeeper", attributes=PlayerAttributes(attacking=2, defending=4, goalkeeping=9, energy=6)),
            Player(name="AllRounder", attributes=PlayerAttributes(attacking=6, defending=6, goalkeeping=4, energy=8)),
            Player(name="Striker2", attributes=PlayerAttributes(attacking=8, defending=4, goalkeeping=2, energy=7)),
            Player(name="Defender2", attributes=PlayerAttributes(attacking=4, defending=8, goalkeeping=3, energy=8)),
            Player(name="Midfielder2", attributes=PlayerAttributes(attacking=6, defending=6, goalkeeping=3, energy=9)),
            Player(name="Goalkeeper2", attributes=PlayerAttributes(attacking=1, defending=3, goalkeeping=8, energy=7)),
            Player(name="AllRounder2", attributes=PlayerAttributes(attacking=5, defending=5, goalkeeping=5, energy=8)),
        ]
        
        balancer = TeamBalancer()
        
        # Act
        red_team, yellow_team = balancer.balance_teams(players)
        
        # Assert
        assert len(red_team.players) == 5
        assert len(yellow_team.players) == 5
        
        # Calculate total team scores
        red_total = sum(player.attributes.attacking + player.attributes.defending + 
                       player.attributes.goalkeeping + player.attributes.energy 
                       for player in red_team.players)
        yellow_total = sum(player.attributes.attacking + player.attributes.defending + 
                          player.attributes.goalkeeping + player.attributes.energy 
                          for player in yellow_team.players)
        
        # Teams should be reasonably balanced (within 10% difference)
        difference = abs(red_total - yellow_total)
        max_difference = (red_total + yellow_total) * 0.1
        assert difference <= max_difference, f"Team difference {difference} exceeds 10% threshold {max_difference}"
    
    def test_extreme_skill_imbalance_balancing(self):
        """Test balancing with extremely imbalanced player skills"""
        # Arrange - Create players with very different skill levels
        players = [
            # High skill players
            Player(name="SuperStriker", attributes=PlayerAttributes(attacking=10, defending=2, goalkeeping=1, energy=9)),
            Player(name="SuperDefender", attributes=PlayerAttributes(attacking=2, defending=10, goalkeeping=3, energy=8)),
            Player(name="SuperMidfielder", attributes=PlayerAttributes(attacking=9, defending=8, goalkeeping=4, energy=10)),
            Player(name="SuperGoalkeeper", attributes=PlayerAttributes(attacking=1, defending=3, goalkeeping=10, energy=7)),
            Player(name="SuperAllRounder", attributes=PlayerAttributes(attacking=8, defending=8, goalkeeping=6, energy=9)),
            # Low skill players
            Player(name="WeakStriker", attributes=PlayerAttributes(attacking=3, defending=1, goalkeeping=1, energy=4)),
            Player(name="WeakDefender", attributes=PlayerAttributes(attacking=1, defending=3, goalkeeping=2, energy=5)),
            Player(name="WeakMidfielder", attributes=PlayerAttributes(attacking=2, defending=2, goalkeeping=1, energy=6)),
            Player(name="WeakGoalkeeper", attributes=PlayerAttributes(attacking=1, defending=1, goalkeeping=3, energy=4)),
            Player(name="WeakAllRounder", attributes=PlayerAttributes(attacking=2, defending=2, goalkeeping=2, energy=5)),
        ]
        
        balancer = TeamBalancer()
        
        # Act
        red_team, yellow_team = balancer.balance_teams(players)
        
        # Assert
        assert len(red_team.players) == 5
        assert len(yellow_team.players) == 5
        
        # Calculate total team scores
        red_total = sum(player.attributes.attacking + player.attributes.defending + 
                       player.attributes.goalkeeping + player.attributes.energy 
                       for player in red_team.players)
        yellow_total = sum(player.attributes.attacking + player.attributes.defending + 
                          player.attributes.goalkeeping + player.attributes.energy 
                          for player in yellow_team.players)
        
        # With extreme imbalance, simple splitting should fail this test
        # Teams should be balanced (within 15% difference due to extreme imbalance)
        difference = abs(red_total - yellow_total)
        max_difference = (red_total + yellow_total) * 0.15
        assert difference <= max_difference, f"Team difference {difference} exceeds 15% threshold {max_difference}"
        
        # Also check that each team has a mix of high and low skill players
        # Lower threshold to 20 since the current threshold of 25 is too high
        red_high_skill = sum(1 for p in red_team.players if p.attributes.attacking + p.attributes.defending + p.attributes.goalkeeping + p.attributes.energy > 20)
        yellow_high_skill = sum(1 for p in yellow_team.players if p.attributes.attacking + p.attributes.defending + p.attributes.goalkeeping + p.attributes.energy > 20)
        
        # Each team should have 2-3 high skill players (not all 5 high skill players on one team)
        assert 2 <= red_high_skill <= 3, f"Red team has {red_high_skill} high skill players, expected 2-3"
        assert 2 <= yellow_high_skill <= 3, f"Yellow team has {yellow_high_skill} high skill players, expected 2-3"


class TestGameRecorder:
    """Test cases for the GameRecorder service"""
    
    def test_record_game(self):
        """Test recording a new game with teams and score"""
        # Arrange
        recorder = GameRecorder()
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
        score = GameScore(red_score=3, yellow_score=2)
        date = "2024-01-15"
        
        # Act
        game = recorder.record_game(date, red_team, yellow_team, score)
        
        # Assert
        assert game.date == date
        assert game.red_team.name == "Red"
        assert game.yellow_team.name == "Yellows"
        assert game.score.red_score == 3
        assert game.score.yellow_score == 2
    
    def test_get_game_history(self):
        """Test retrieving game history"""
        # Arrange
        recorder = GameRecorder()
        
        # Record a few games
        red_team1 = Team(name="Red", players=[Player(name="Player1", attributes=PlayerAttributes(attacking=7, defending=6, goalkeeping=3, energy=8))])
        yellow_team1 = Team(name="Yellows", players=[Player(name="Player2", attributes=PlayerAttributes(attacking=6, defending=7, goalkeeping=4, energy=7))])
        
        recorder.record_game("2024-01-15", red_team1, yellow_team1, GameScore(red_score=3, yellow_score=2))
        recorder.record_game("2024-01-22", red_team1, yellow_team1, GameScore(red_score=1, yellow_score=4))
        
        # Act
        history = recorder.get_game_history()
        
        # Assert
        assert len(history) == 2
        assert history[0].date == "2024-01-15"
        assert history[1].date == "2024-01-22"
    
    def test_get_player_performance_stats(self):
        """Test getting performance statistics for a player"""
        # Arrange
        recorder = GameRecorder()
        player = Player(name="Player1", attributes=PlayerAttributes(attacking=7, defending=6, goalkeeping=3, energy=8))
        
        # Record games where this player participated
        red_team = Team(name="Red", players=[player])
        yellow_team = Team(name="Yellows", players=[Player(name="Player2", attributes=PlayerAttributes(attacking=6, defending=7, goalkeeping=4, energy=7))])
        
        recorder.record_game("2024-01-15", red_team, yellow_team, GameScore(red_score=3, yellow_score=2))
        recorder.record_game("2024-01-22", red_team, yellow_team, GameScore(red_score=1, yellow_score=4))
        
        # Act
        stats = recorder.get_player_performance_stats("Player1")
        
        # Assert
        assert stats["total_games"] == 2
        assert stats["wins"] == 1
        assert stats["losses"] == 1
        assert stats["win_rate"] == 0.5 