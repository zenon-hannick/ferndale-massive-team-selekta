import sqlite3
import json
from typing import List, Optional
from app.models.player import Player, PlayerAttributes
from app.models.game import Team, Game, GameScore


class DatabaseService:
    """Service for database operations using SQLite"""
    
    def __init__(self, db_path: str = "football_teams.db"):
        self.db_path = db_path
        self._create_tables()
        if self.db_path == "football_teams.db":
            self.initialize_default_players()
    
    def _create_tables(self):
        """Create database tables if they don't exist"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Players table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS players (
                    name TEXT PRIMARY KEY,
                    attacking INTEGER,
                    defending INTEGER,
                    goalkeeping INTEGER,
                    energy INTEGER,
                    available BOOLEAN
                )
            ''')
            
            # Games table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS games (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT,
                    red_team_data TEXT,
                    yellow_team_data TEXT,
                    red_score INTEGER,
                    yellow_score INTEGER
                )
            ''')
            
            conn.commit()
    
    def save_player(self, player: Player):
        """Save a player to the database"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT OR REPLACE INTO players 
                (name, attacking, defending, goalkeeping, energy, available)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                player.name,
                player.attributes.attacking,
                player.attributes.defending,
                player.attributes.goalkeeping,
                player.attributes.energy,
                player.available
            ))
            conn.commit()
    
    def get_player(self, name: str) -> Optional[Player]:
        """Get a player by name"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT name, attacking, defending, goalkeeping, energy, available
                FROM players WHERE name = ?
            ''', (name,))
            
            row = cursor.fetchone()
            if row:
                # Handle case where available column might be None (backward compatibility)
                available = bool(row[5]) if row[5] is not None else True
                return Player(
                    name=row[0],
                    attributes=PlayerAttributes(
                        attacking=row[1],
                        defending=row[2],
                        goalkeeping=row[3],
                        energy=row[4]
                    ),
                    available=available
                )
            return None
    
    def get_all_players(self) -> List[Player]:
        """Get all players from the database"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT name, attacking, defending, goalkeeping, energy, available
                FROM players
            ''')
            
            players = []
            for row in cursor.fetchall():
                # Handle case where available column might be None (backward compatibility)
                available = bool(row[5]) if row[5] is not None else True
                player = Player(
                    name=row[0],
                    attributes=PlayerAttributes(
                        attacking=row[1],
                        defending=row[2],
                        goalkeeping=row[3],
                        energy=row[4]
                    ),
                    available=available
                )
                players.append(player)
            
            return players
    
    def update_player(self, player: Player):
        """Update an existing player"""
        self.save_player(player)  # INSERT OR REPLACE handles updates
    
    def save_game(self, game: Game):
        """Save a game to the database"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Serialize team data as JSON
            red_team_data = json.dumps([{
                "name": p.name,
                "attributes": {
                    "attacking": p.attributes.attacking,
                    "defending": p.attributes.defending,
                    "goalkeeping": p.attributes.goalkeeping,
                    "energy": p.attributes.energy
                },
                "available": p.available
            } for p in game.red_team.players])
            
            yellow_team_data = json.dumps([{
                "name": p.name,
                "attributes": {
                    "attacking": p.attributes.attacking,
                    "defending": p.attributes.defending,
                    "goalkeeping": p.attributes.goalkeeping,
                    "energy": p.attributes.energy
                },
                "available": p.available
            } for p in game.yellow_team.players])
            
            cursor.execute('''
                INSERT INTO games (date, red_team_data, yellow_team_data, red_score, yellow_score)
                VALUES (?, ?, ?, ?, ?)
            ''', (
                game.date,
                red_team_data,
                yellow_team_data,
                game.score.red_score,
                game.score.yellow_score
            ))
            conn.commit()
    
    def get_all_games(self) -> List[Game]:
        """Get all games from the database"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT date, red_team_data, yellow_team_data, red_score, yellow_score
                FROM games ORDER BY date
            ''')
            
            games = []
            for row in cursor.fetchall():
                # Deserialize team data
                red_team_players = []
                for player_data in json.loads(row[1]):
                    player = Player(
                        name=player_data["name"],
                        attributes=PlayerAttributes(
                            attacking=player_data["attributes"]["attacking"],
                            defending=player_data["attributes"]["defending"],
                            goalkeeping=player_data["attributes"]["goalkeeping"],
                            energy=player_data["attributes"]["energy"]
                        ),
                        available=player_data["available"]
                    )
                    red_team_players.append(player)
                
                yellow_team_players = []
                for player_data in json.loads(row[2]):
                    player = Player(
                        name=player_data["name"],
                        attributes=PlayerAttributes(
                            attacking=player_data["attributes"]["attacking"],
                            defending=player_data["attributes"]["defending"],
                            goalkeeping=player_data["attributes"]["goalkeeping"],
                            energy=player_data["attributes"]["energy"]
                        ),
                        available=player_data["available"]
                    )
                    yellow_team_players.append(player)
                
                game = Game(
                    date=row[0],
                    red_team=Team(name="Red", players=red_team_players),
                    yellow_team=Team(name="Yellows", players=yellow_team_players),
                    score=GameScore(red_score=row[3], yellow_score=row[4])
                )
                games.append(game)
            
            return games
    
    def initialize_default_players(self):
        """Initialize the database with default players with their current attribute values"""
        default_players = [
            ("Dermot", {"attacking": 4, "defending": 8, "goalkeeping": 6, "energy": 8}),
            ("Tom", {"attacking": 3, "defending": 7, "goalkeeping": 4, "energy": 7}),
            ("Connor", {"attacking": 5, "defending": 9, "goalkeeping": 6, "energy": 7}),
            ("Rodney", {"attacking": 5, "defending": 7, "goalkeeping": 7, "energy": 8}),
            ("Danny G", {"attacking": 8, "defending": 7, "goalkeeping": 6, "energy": 6}),
            ("Jamie Sully", {"attacking": 9, "defending": 4, "goalkeeping": 4, "energy": 7}),
            ("Glenn", {"attacking": 7, "defending": 7, "goalkeeping": 6, "energy": 8}),
            ("Joseph Smash", {"attacking": 7, "defending": 7, "goalkeeping": 6, "energy": 5}),
            ("David", {"attacking": 7, "defending": 5, "goalkeeping": 4, "energy": 5}),
            ("Zenon", {"attacking": 6, "defending": 6, "goalkeeping": 6, "energy": 7}),
            ("Dylan", {"attacking": 9, "defending": 9, "goalkeeping": 7, "energy": 9}),
            ("Matt", {"attacking": 9, "defending": 9, "goalkeeping": 7, "energy": 9}),
            ("Will", {"attacking": 8, "defending": 8, "goalkeeping": 9, "energy": 6}),
            ("Dom", {"attacking": 9, "defending": 8, "goalkeeping": 7, "energy": 8}),
            ("Liam", {"attacking": 10, "defending": 6, "goalkeeping": 4, "energy": 7}),
            ("Mikael", {"attacking": 5, "defending": 8, "goalkeeping": 8, "energy": 8}),
            ("Callum", {"attacking": 7, "defending": 6, "goalkeeping": 7, "energy": 7}),
            ("Adulai", {"attacking": 9, "defending": 7, "goalkeeping": 6, "energy": 8}),
            ("Ringer1", {"attacking": 5, "defending": 5, "goalkeeping": 5, "energy": 5}),
            ("Ringer2", {"attacking": 5, "defending": 5, "goalkeeping": 5, "energy": 5}),
            ("Ringer3", {"attacking": 5, "defending": 5, "goalkeeping": 5, "energy": 5}),
            ("Ringer4", {"attacking": 5, "defending": 5, "goalkeeping": 5, "energy": 5}),
            ("Ringer5", {"attacking": 5, "defending": 5, "goalkeeping": 5, "energy": 5})
        ]
        
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Check if players table is empty
            cursor.execute('SELECT COUNT(*) FROM players')
            count = cursor.fetchone()[0]
            
            # Only add default players if the table is empty
            if count == 0:
                for player_name, attributes in default_players:
                    cursor.execute('''
                        INSERT INTO players (name, attacking, defending, goalkeeping, energy, available)
                        VALUES (?, ?, ?, ?, ?, ?)
                    ''', (
                        player_name,
                        attributes["attacking"],
                        attributes["defending"],
                        attributes["goalkeeping"],
                        attributes["energy"],
                        True
                    ))
                
                conn.commit()
                print(f"Initialized database with {len(default_players)} default players")
            else:
                print(f"Database already contains {count} players, skipping initialization") 