# Football Team Selector - Technical Documentation

## Architecture Overview

The Football Team Selector is built using a modern microservices architecture with the following components:

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │   Backend       │    │   Database      │
│   (React)       │◄──►│   (FastAPI)     │◄──►│   (SQLite)      │
│                 │    │                 │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### Technology Stack

- **Backend**: Python 3.9+ with FastAPI
- **Database**: SQLite (development), PostgreSQL (production-ready)
- **Testing**: pytest with 100% test coverage
- **Development**: Test-Driven Development (TDD)
- **API Documentation**: Auto-generated with Swagger/OpenAPI

## Project Structure

```
TeamSelectorFootball/
├── backend/
│   ├── app/
│   │   ├── models/           # Data models and validation
│   │   │   ├── __init__.py
│   │   │   ├── player.py     # Player and PlayerAttributes models
│   │   │   └── game.py       # Game, Team, GameScore models
│   │   ├── services/         # Business logic layer
│   │   │   ├── __init__.py
│   │   │   ├── team_balancer.py    # Team balancing algorithm
│   │   │   ├── game_recorder.py    # Game recording and statistics
│   │   │   └── database.py         # Database operations
│   │   ├── tests/            # Test suite
│   │   │   ├── test_models.py
│   │   │   ├── test_services.py
│   │   │   ├── test_api.py
│   │   │   └── test_database.py
│   │   └── main.py           # FastAPI application entry point
│   ├── requirements.txt      # Python dependencies
│   └── run_server.py         # Development server startup
├── frontend/                 # React frontend (future)
└── docs/                     # Documentation
```

## Core Components

### 1. Data Models

#### Player Model
```python
class PlayerAttributes(BaseModel):
    attacking: int = Field(..., ge=1, le=10)
    defending: int = Field(..., ge=1, le=10)
    goalkeeping: int = Field(..., ge=1, le=10)
    energy: int = Field(..., ge=1, le=10)

class Player(BaseModel):
    name: str
    attributes: PlayerAttributes
    available: bool = True
```

**Key Features:**
- Pydantic validation for data integrity
- Field constraints (1-10 range for attributes)
- Type safety with Python type hints

#### Game Model
```python
class GameScore(BaseModel):
    red_score: int = Field(..., ge=0)
    yellow_score: int = Field(..., ge=0)

class Team(BaseModel):
    name: str
    players: List[Player]

class Game(BaseModel):
    date: str
    red_team: Team
    yellow_team: Team
    score: GameScore
```

### 2. Team Balancing Algorithm

The intelligent team balancing algorithm is implemented in `TeamBalancer` class:

```python
class TeamBalancer:
    def balance_teams(self, players: List[Player]) -> Tuple[Team, Team]:
        # Filter available players
        available_players = [p for p in players if p.available]
        
        # Validate player count
        if len(available_players) not in [10, 12]:
            raise ValueError(f"Expected 10 or 12 available players, got {len(available_players)}")
        
        # Calculate total skill scores
        player_scores = []
        for player in available_players:
            total_score = (player.attributes.attacking + 
                          player.attributes.defending + 
                          player.attributes.goalkeeping + 
                          player.attributes.energy)
            player_scores.append((player, total_score))
        
        # Sort by skill (highest to lowest)
        player_scores.sort(key=lambda x: x[1], reverse=True)
        
        # Distribute players alternately
        red_players = []
        yellow_players = []
        
        for i, (player, _) in enumerate(player_scores):
            if i % 2 == 0:
                red_players.append(player)
            else:
                yellow_players.append(player)
        
        return Team(name="Red", players=red_players), Team(name="Yellows", players=yellow_players)
```

**Algorithm Steps:**
1. **Filter**: Only include available players
2. **Validate**: Ensure 10 or 12 players
3. **Calculate**: Sum all attributes for total skill score
4. **Sort**: Order players by skill (highest to lowest)
5. **Distribute**: Alternate assignment to Red and Yellow teams

**Benefits:**
- Ensures balanced skill distribution
- Handles extreme skill imbalances
- Simple and predictable algorithm
- O(n log n) time complexity

### 3. Game Recording System

The `GameRecorder` service manages game history and statistics:

```python
class GameRecorder:
    def __init__(self):
        self.games: List[Game] = []
    
    def record_game(self, date: str, red_team: Team, yellow_team: Team, score: GameScore) -> Game:
        game = Game(date=date, red_team=red_team, yellow_team=yellow_team, score=score)
        self.games.append(game)
        return game
    
    def get_player_performance_stats(self, player_name: str) -> Dict[str, Any]:
        total_games = wins = losses = 0
        
        for game in self.games:
            # Check if player participated
            red_players = [p.name for p in game.red_team.players]
            yellow_players = [p.name for p in game.yellow_team.players]
            
            if player_name in red_players:
                total_games += 1
                wins += 1 if game.score.red_score > game.score.yellow_score else 0
                losses += 1 if game.score.red_score <= game.score.yellow_score else 0
            elif player_name in yellow_players:
                total_games += 1
                wins += 1 if game.score.yellow_score > game.score.red_score else 0
                losses += 1 if game.score.yellow_score <= game.score.red_score else 0
        
        return {
            "total_games": total_games,
            "wins": wins,
            "losses": losses,
            "win_rate": wins / total_games if total_games > 0 else 0.0
        }
```

### 4. Database Layer

The `DatabaseService` provides persistence using SQLite:

```python
class DatabaseService:
    def __init__(self, db_path: str = "football_teams.db"):
        self.db_path = db_path
        self._create_tables()
    
    def _create_tables(self):
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
            
            # Games table with JSON serialization
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
```

**Features:**
- Automatic table creation
- JSON serialization for complex data
- CRUD operations for players and games
- Transaction safety

## API Design

### RESTful Endpoints

| Method | Endpoint | Description | Status Code |
|--------|----------|-------------|-------------|
| GET | `/` | Application info | 200 |
| POST | `/players/` | Create player | 201 |
| GET | `/players/` | List all players | 200 |
| GET | `/players/{name}/stats` | Player statistics | 200 |
| POST | `/teams/balance` | Balance teams | 200 |
| POST | `/games/` | Record game | 201 |
| GET | `/games/` | Game history | 200 |

### Request/Response Patterns

**Standard Response Format:**
```json
{
  "data": {...},
  "status": "success",
  "message": "Operation completed"
}
```

**Error Response Format:**
```json
{
  "detail": "Error description",
  "status_code": 400
}
```

## Testing Strategy

### Test-Driven Development (TDD)

The project follows Kent Beck's TDD methodology:

1. **Red**: Write failing test
2. **Green**: Write minimal code to pass
3. **Refactor**: Improve code while keeping tests green

### Test Coverage

**Current Coverage: 100%**
- **24 tests** covering all functionality
- **Unit tests** for models, services, and API
- **Integration tests** for database operations
- **Edge case testing** for team balancing

### Test Categories

1. **Model Tests** (5 tests)
   - Player validation
   - Game validation
   - Attribute constraints

2. **Service Tests** (8 tests)
   - Team balancing algorithm
   - Game recording functionality
   - Player statistics calculation

3. **API Tests** (6 tests)
   - Endpoint functionality
   - Request/response validation
   - Error handling

4. **Database Tests** (5 tests)
   - CRUD operations
   - Data persistence
   - Schema validation

## Performance Considerations

### Algorithm Complexity

- **Team Balancing**: O(n log n) due to sorting
- **Game Recording**: O(1) for recording, O(n) for statistics
- **Database Operations**: O(log n) for indexed queries

### Scalability

**Current Limitations:**
- In-memory game storage (will be replaced with database)
- Single-threaded processing
- No caching layer

**Future Improvements:**
- Database persistence for all data
- Redis caching for frequently accessed data
- Async processing for large datasets
- Horizontal scaling with load balancers

## Security Considerations

### Current Security

- Input validation with Pydantic
- SQL injection prevention with parameterized queries
- No sensitive data storage

### Future Security Enhancements

- JWT authentication
- Rate limiting
- Input sanitization
- HTTPS enforcement
- API key management

## Deployment

### Development Setup

```bash
# Install dependencies
cd backend
pip3 install -r requirements.txt

# Run tests
python3 -m pytest app/tests/ -v

# Start server
python3 run_server.py
```

### Production Deployment

**Requirements:**
- Python 3.9+
- PostgreSQL database
- Reverse proxy (nginx)
- Process manager (systemd/supervisor)

**Environment Variables:**
```bash
DATABASE_URL=postgresql://user:pass@localhost/football_teams
SECRET_KEY=your-secret-key
DEBUG=false
```

## Monitoring and Logging

### Current Logging

- FastAPI automatic logging
- SQLite query logging
- Error tracking in tests

### Future Monitoring

- Application performance monitoring (APM)
- Database query optimization
- Error tracking and alerting
- Usage analytics

## Future Enhancements

### Planned Features

1. **Team Correlation Analysis**
   - Identify strong player partnerships
   - Suggest optimal team combinations
   - Historical performance analysis

2. **Advanced Statistics**
   - Player rating adjustments based on performance
   - Team chemistry metrics
   - Predictive analytics

3. **Web Interface**
   - React frontend with TypeScript
   - Real-time updates
   - Interactive team management

4. **Cloud Deployment**
   - AWS/Azure/GCP deployment
   - Containerization with Docker
   - CI/CD pipeline

### Technical Debt

- Replace in-memory storage with database
- Add comprehensive error handling
- Implement caching layer
- Add API versioning
- Improve test performance

## Contributing

### Development Workflow

1. **Fork** the repository
2. **Create** feature branch
3. **Write tests** first (TDD)
4. **Implement** functionality
5. **Run tests** and ensure 100% coverage
6. **Submit** pull request

### Code Standards

- **Python**: PEP 8 style guide
- **Tests**: pytest with descriptive names
- **Documentation**: Docstrings for all functions
- **Type Hints**: Required for all functions

### Testing Requirements

- All new features must have tests
- Maintain 100% test coverage
- Include edge case testing
- Performance testing for algorithms 