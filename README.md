# Football Team Selector

A React + Python application for creating balanced football teams using player attributes and historical performance data.

## 📚 Documentation

**📖 [Complete Documentation](docs/README.md)** - Start here for comprehensive guides

- **[🚀 Quick Start Guide](docs/QUICK_START.md)** - Get up and running in 5 minutes
- **[👥 User Guide](docs/USER_GUIDE.md)** - Complete user manual with examples
- **[🔧 API Reference](docs/API_REFERENCE.md)** - Complete API documentation
- **[🏗️ Technical Documentation](docs/TECHNICAL_DOCUMENTATION.md)** - Architecture and implementation details

## Features

- Player management with skill attributes (Attacking, Defending, Goalkeeping, Energy)
- Availability tracking for upcoming games
- **Intelligent team balancing** using player attributes and skill scores
- **Game recording and historical data analysis**
- **Player performance statistics** (wins, losses, win rate)
- **Database persistence** (SQLite for local development)
- Team correlation analysis
- Game score recording and historical data
- Two teams: Red and Yellows (5-6 players each)

## Technology Stack

- **Backend**: Python (FastAPI)
- **Frontend**: React (TypeScript)
- **Database**: SQLite (local), PostgreSQL (cloud-ready)
- **Testing**: pytest (backend), Jest (frontend)
- **Development**: TDD (Test-Driven Development)

## Project Structure

```
TeamSelectorFootball/
├── backend/                 # Python FastAPI backend
│   ├── app/
│   │   ├── models/         # Data models (Player, Game, Team)
│   │   ├── services/       # Business logic (TeamBalancer, GameRecorder, DatabaseService)
│   │   ├── api/           # API endpoints
│   │   └── tests/         # Backend tests (24 tests passing)
│   ├── requirements.txt
│   ├── run_server.py      # Startup script
│   └── main.py
├── frontend/               # React frontend
│   ├── src/
│   │   ├── components/    # React components
│   │   ├── services/      # API calls
│   │   └── tests/         # Frontend tests
│   └── package.json
├── docs/                   # 📚 Comprehensive documentation
│   ├── README.md          # Documentation index
│   ├── QUICK_START.md     # 5-minute setup guide
│   ├── USER_GUIDE.md      # Complete user manual
│   ├── API_REFERENCE.md   # API documentation
│   └── TECHNICAL_DOCUMENTATION.md # Technical details
└── README.md
```

## Current Progress

### ✅ Backend (Complete with Database Persistence)
- **Models**: Player, PlayerAttributes, Game, Team, GameScore
- **Services**: 
  - TeamBalancer with intelligent balancing algorithm
  - GameRecorder for historical data analysis
  - **DatabaseService for SQLite persistence**
- **API**: FastAPI endpoints for players, team balancing, and game recording
- **Tests**: 24 tests passing (100% coverage for current features)
- **Server**: Running on http://localhost:8000

### 🔄 Frontend (Setup Required)
- **Structure**: Created but needs Node.js installation
- **Dependencies**: Defined in package.json
- **Components**: To be implemented

## Development Approach

This project follows **Test-Driven Development (TDD)** as described by Kent Beck:
1. **Red**: Write a failing test
2. **Green**: Write minimal code to make the test pass
3. **Refactor**: Improve the code while keeping tests green

## Getting Started

### Backend Setup
```bash
cd backend
pip3 install -r requirements.txt
python3 -m pytest app/tests/  # Run tests
python3 run_server.py         # Start development server
```

The API will be available at:
- **API**: http://localhost:8000
- **Documentation**: http://localhost:8000/docs
- **Alternative docs**: http://localhost:8000/redoc

### Frontend Setup (Requires Node.js)
```bash
# Install Node.js first (https://nodejs.org/)
cd frontend
npm install
npm test  # Run tests
npm start # Start development server
```

## API Endpoints

- `GET /` - Root endpoint
- `POST /players/` - Create a new player
- `GET /players/` - Get all players
- `GET /players/{player_name}/stats` - Get player performance statistics
- `POST /teams/balance` - Balance players into two teams (intelligent balancing)
- `POST /games/` - Record a new game
- `GET /games/` - Get game history

## Team Balancing Algorithm

The application uses an intelligent team balancing algorithm that:

1. **Calculates total skill scores** for each player (attacking + defending + goalkeeping + energy)
2. **Sorts players by skill** (highest to lowest)
3. **Distributes players alternately** between Red and Yellow teams
4. **Ensures balanced teams** with similar total skill levels
5. **Handles extreme skill imbalances** by distributing high and low skill players evenly

### Example Output
With 10 players of varying skill levels, the algorithm creates two balanced teams:
- **Red Team**: 3 high-skill + 2 low-skill players
- **Yellow Team**: 3 high-skill + 2 low-skill players

## Game Recording & Historical Analysis

The application now includes comprehensive game recording and analysis:

### Game Recording
- **Record game results** with teams and scores
- **Store game history** for analysis
- **Track player participation** in games

### Player Performance Statistics
- **Total games played** by each player
- **Win/loss records** and win rates
- **Historical performance** tracking

### Database Persistence
- **SQLite database** for local development
- **Player data persistence** with CRUD operations
- **Game history storage** with team and score data
- **Automatic table creation** on startup

### Example API Usage
```bash
# Record a game
curl -X POST "http://localhost:8000/games/" \
  -H "Content-Type: application/json" \
  -d '{"date": "2024-01-15", "red_team": {...}, "yellow_team": {...}, "score": {"red_score": 3, "yellow_score": 2}}'

# Get game history
curl -X GET "http://localhost:8000/games/"

# Get player statistics
curl -X GET "http://localhost:8000/players/Player1/stats"
```

## Completed Steps (1-5)

✅ **Step 1**: Historical data analysis and game recording functionality
✅ **Step 2**: Game recording API endpoints
✅ **Step 3**: Player performance statistics
✅ **Step 4**: Database persistence (SQLite)
✅ **Step 5**: Integration testing and documentation

## Next Steps

1. **Install Node.js** for frontend development
2. **Implement React components** for player management and game recording
3. **Add team correlation analysis** using historical data
4. **Deploy to cloud** (AWS/Azure/GCP)

## Testing

### Backend Tests
```bash
cd backend
python3 -m pytest app/tests/ -v
```

**Test Coverage:**
- ✅ Player model validation (3 tests)
- ✅ Game model validation (2 tests)
- ✅ Team balancing with 10/12 players (2 tests)
- ✅ Unavailable player filtering (1 test)
- ✅ Intelligent team balancing (2 tests)
- ✅ Extreme skill imbalance handling (1 test)
- ✅ Game recording functionality (3 tests)
- ✅ API endpoints (6 tests)
- ✅ Database persistence (5 tests)

### Frontend Tests (after Node.js installation)
```bash
cd frontend
npm test
``` 