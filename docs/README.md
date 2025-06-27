# Football Team Selector - Documentation

Welcome to the Football Team Selector documentation! This comprehensive guide will help you understand, use, and contribute to the application.

## 📚 Documentation Index

### 🚀 Getting Started
- **[Quick Start Guide](QUICK_START.md)** - Get up and running in 5 minutes
- **[User Guide](USER_GUIDE.md)** - Complete user manual with examples

### 🔧 Technical Documentation
- **[API Reference](API_REFERENCE.md)** - Complete API documentation with examples
- **[Technical Documentation](TECHNICAL_DOCUMENTATION.md)** - Architecture, algorithms, and implementation details

### 📖 Additional Resources
- **[Main README](../README.md)** - Project overview and setup instructions
- **[Interactive API Docs](http://localhost:8000/docs)** - Live API documentation (when server is running)

## 🎯 What is Football Team Selector?

The Football Team Selector is an intelligent application that helps create balanced football teams using player attributes and historical performance data. It features:

- **Intelligent Team Balancing**: Automatically creates balanced teams of 5-6 players each
- **Player Management**: Add players with skill ratings (Attacking, Defending, Goalkeeping, Energy)
- **Game Recording**: Track game results and team performance
- **Player Statistics**: View individual player performance history
- **Historical Analysis**: Analyze past games and team correlations
- **Database Persistence**: SQLite storage with automatic data management

## 🏗️ Architecture Overview

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │   Backend       │    │   Database      │
│   (React)       │◄──►│   (FastAPI)     │◄──►│   (SQLite)      │
│   (Future)      │    │                 │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### Technology Stack
- **Backend**: Python 3.9+ with FastAPI
- **Database**: SQLite (development), PostgreSQL (production-ready)
- **Testing**: pytest with 100% test coverage
- **Development**: Test-Driven Development (TDD)
- **API Documentation**: Auto-generated with Swagger/OpenAPI

## 🚀 Quick Start

1. **Start the server:**
   ```bash
   cd backend
   python3 run_server.py
   ```

2. **Test the API:**
   ```bash
   curl -X GET "http://localhost:8000/"
   ```

3. **Add players and create teams:**
   ```bash
   # Add a player
   curl -X POST "http://localhost:8000/players/" \
     -H "Content-Type: application/json" \
     -d '{"name": "Alex", "attributes": {"attacking": 8, "defending": 6, "goalkeeping": 3, "energy": 9}, "available": true}'
   
   # Create balanced teams (requires 10 players)
   curl -X POST "http://localhost:8000/teams/balance" \
     -H "Content-Type: application/json" \
     -d '{"players": [/* your 10 players */]}'
   ```

4. **Record games and view statistics:**
   ```bash
   # Record a game
   curl -X POST "http://localhost:8000/games/" \
     -H "Content-Type: application/json" \
     -d '{"date": "2024-01-20", "red_team": {...}, "yellow_team": {...}, "score": {"red_score": 3, "yellow_score": 2}}'
   
   # View player stats
   curl -X GET "http://localhost:8000/players/Alex/stats"
   ```

## 📊 Key Features

### Intelligent Team Balancing Algorithm
1. **Calculate Total Skill**: Sum of all attributes for each player
2. **Sort Players**: Order by skill (highest to lowest)
3. **Distribute Alternately**: Place players alternately in Red and Yellow teams
4. **Ensure Balance**: Algorithm ensures teams have similar total skill levels

### Player Skill Attributes
- **Attacking** (1-10): Shooting, passing, dribbling ability
- **Defending** (1-10): Tackling, positioning, defensive awareness
- **Goalkeeping** (1-10): Shot stopping, distribution, positioning
- **Energy** (1-10): Stamina, work rate, fitness level

### Game Recording & Statistics
- **Complete game data** with teams, players, and scores
- **Player performance tracking** with win/loss records
- **Historical analysis** for team optimization
- **Automatic statistics calculation**

## 🔧 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Application info |
| POST | `/players/` | Create player |
| GET | `/players/` | List all players |
| GET | `/players/{name}/stats` | Player statistics |
| POST | `/teams/balance` | Balance teams |
| POST | `/games/` | Record game |
| GET | `/games/` | Game history |

## 🧪 Testing

The application follows Test-Driven Development (TDD) with 100% test coverage:

```bash
cd backend
python3 -m pytest app/tests/ -v
```

**Test Categories:**
- **Model Tests** (5 tests): Data validation and constraints
- **Service Tests** (8 tests): Business logic and algorithms
- **API Tests** (6 tests): Endpoint functionality
- **Database Tests** (5 tests): Data persistence

## 📈 Current Status

### ✅ Completed Features
- **Backend API** with 7 endpoints
- **Intelligent team balancing** algorithm
- **Game recording** and statistics
- **Database persistence** (SQLite)
- **Comprehensive testing** (24 tests)
- **API documentation** (auto-generated)

### 🔄 In Progress
- **Frontend development** (React)
- **Team correlation analysis**
- **Advanced statistics**

### 🚀 Planned Features
- **Web interface** for easier management
- **Cloud deployment** options
- **Mobile app** support
- **Real-time updates**

## 🤝 Contributing

We welcome contributions! Please follow these guidelines:

1. **Fork** the repository
2. **Create** a feature branch
3. **Write tests** first (TDD approach)
4. **Implement** functionality
5. **Run tests** and ensure 100% coverage
6. **Submit** a pull request

### Development Setup
```bash
# Clone the repository
git clone <repository-url>
cd TeamSelectorFootball

# Install dependencies
cd backend
pip3 install -r requirements.txt

# Run tests
python3 -m pytest app/tests/ -v

# Start development server
python3 run_server.py
```

## 📞 Support

### Getting Help
1. **Check the documentation** - Start with the Quick Start Guide
2. **Explore the API** - Visit http://localhost:8000/docs
3. **Review test files** - See `backend/app/tests/` for examples
4. **Check server logs** - Look for error details

### Common Issues
- **"Expected 10 or 12 players"**: Add more players or mark them as available
- **Server won't start**: Check if port 8000 is available
- **Player not found**: Check spelling and use URL encoding for spaces

## 📄 License

This project is open source and available under the MIT License.

## 🎯 Roadmap

### Short Term (Next 2-4 weeks)
- [ ] React frontend with TypeScript
- [ ] Team correlation analysis
- [ ] Enhanced player statistics

### Medium Term (Next 2-3 months)
- [ ] Cloud deployment (AWS/Azure/GCP)
- [ ] Mobile app development
- [ ] Advanced analytics dashboard

### Long Term (Next 6-12 months)
- [ ] Machine learning for team optimization
- [ ] Real-time multiplayer features
- [ ] Integration with external football APIs

---

**Happy team building! ⚽**

For the latest updates and issues, please check the main repository. 