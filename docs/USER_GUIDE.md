# Football Team Selector - User Guide

## Overview

The Football Team Selector is an intelligent application that helps create balanced football teams using player attributes and historical performance data. It automatically balances teams based on player skills and tracks game results for analysis.

## Key Features

- **Player Management**: Add players with skill ratings (Attacking, Defending, Goalkeeping, Energy)
- **Intelligent Team Balancing**: Automatically creates balanced teams of 5-6 players each
- **Game Recording**: Track game results and team performance
- **Player Statistics**: View individual player performance history
- **Historical Analysis**: Analyze past games and team correlations

## Getting Started

### 1. Start the Application

```bash
cd backend
python3 run_server.py
```

The application will be available at: http://localhost:8000

### 2. Access the API Documentation

Visit http://localhost:8000/docs for interactive API documentation.

## How to Use the Application

### Step 1: Add Players

First, add players to the system with their skill attributes:

**Example: Adding a player**
```bash
curl -X POST "http://localhost:8000/players/" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John",
    "attributes": {
      "attacking": 8,
      "defending": 6,
      "goalkeeping": 3,
      "energy": 9
    },
    "available": true
  }'
```

**Skill Attributes Explained:**
- **Attacking** (1-10): Shooting, passing, dribbling ability
- **Defending** (1-10): Tackling, positioning, defensive awareness
- **Goalkeeping** (1-10): Shot stopping, distribution, positioning
- **Energy** (1-10): Stamina, work rate, fitness level
- **Available**: Whether the player can play in upcoming games

### Step 2: View All Players

```bash
curl -X GET "http://localhost:8000/players/"
```

### Step 3: Create Balanced Teams

The application requires 10 or 12 available players to create balanced teams:

```bash
curl -X POST "http://localhost:8000/teams/balance" \
  -H "Content-Type: application/json" \
  -d '{
    "players": [
      {"name": "John", "attributes": {"attacking": 8, "defending": 6, "goalkeeping": 3, "energy": 9}, "available": true},
      {"name": "Sarah", "attributes": {"attacking": 6, "defending": 8, "goalkeeping": 4, "energy": 7}, "available": true},
      // ... add more players to reach 10 or 12 total
    ]
  }'
```

**Team Balancing Algorithm:**
1. Calculates total skill score for each player
2. Sorts players by skill (highest to lowest)
3. Distributes players alternately between Red and Yellow teams
4. Ensures balanced distribution of high and low skill players

### Step 4: Record Game Results

After a game, record the results:

```bash
curl -X POST "http://localhost:8000/games/" \
  -H "Content-Type: application/json" \
  -d '{
    "date": "2024-01-20",
    "red_team": {
      "name": "Red",
      "players": [
        {"name": "John", "attributes": {"attacking": 8, "defending": 6, "goalkeeping": 3, "energy": 9}, "available": true}
      ]
    },
    "yellow_team": {
      "name": "Yellows",
      "players": [
        {"name": "Sarah", "attributes": {"attacking": 6, "defending": 8, "goalkeeping": 4, "energy": 7}, "available": true}
      ]
    },
    "score": {
      "red_score": 3,
      "yellow_score": 2
    }
  }'
```

### Step 5: View Game History

```bash
curl -X GET "http://localhost:8000/games/"
```

### Step 6: Check Player Statistics

View individual player performance:

```bash
curl -X GET "http://localhost:8000/players/John/stats"
```

**Statistics Include:**
- Total games played
- Number of wins
- Number of losses
- Win rate percentage

## Example Workflow

### Complete Example Session

1. **Add 10 players:**
```bash
# Add players one by one
curl -X POST "http://localhost:8000/players/" -H "Content-Type: application/json" -d '{"name": "Alex", "attributes": {"attacking": 8, "defending": 6, "goalkeeping": 3, "energy": 9}, "available": true}'
curl -X POST "http://localhost:8000/players/" -H "Content-Type: application/json" -d '{"name": "Ben", "attributes": {"attacking": 6, "defending": 8, "goalkeeping": 4, "energy": 7}, "available": true}'
# ... continue for all 10 players
```

2. **Get all players:**
```bash
curl -X GET "http://localhost:8000/players/"
```

3. **Create balanced teams:**
```bash
curl -X POST "http://localhost:8000/teams/balance" -H "Content-Type: application/json" -d '{"players": [/* all 10 players */]}'
```

4. **Record a game:**
```bash
curl -X POST "http://localhost:8000/games/" -H "Content-Type: application/json" -d '{"date": "2024-01-20", "red_team": {...}, "yellow_team": {...}, "score": {"red_score": 3, "yellow_score": 2}}'
```

5. **Check player stats:**
```bash
curl -X GET "http://localhost:8000/players/Alex/stats"
```

## Tips for Best Results

### Player Rating Guidelines

- **Attacking**: Rate based on shooting accuracy, passing ability, and offensive positioning
- **Defending**: Rate based on tackling ability, defensive positioning, and marking
- **Goalkeeping**: Rate based on shot-stopping ability, distribution, and positioning
- **Energy**: Rate based on stamina, work rate, and overall fitness

### Team Balancing Tips

- Ensure all players have `"available": true` for team balancing
- The system works best with 10 or 12 players
- Players with similar total skill scores will be distributed evenly
- The algorithm automatically handles skill imbalances

### Game Recording Best Practices

- Record games immediately after completion
- Include all players who participated
- Use consistent date format (YYYY-MM-DD)
- Record accurate final scores

## Troubleshooting

### Common Issues

1. **"Expected 10 or 12 available players" error**
   - Solution: Add more players or mark more players as available

2. **Player not found in statistics**
   - Solution: Ensure the player participated in recorded games

3. **Server not starting**
   - Solution: Check if port 8000 is available, or use a different port

### Getting Help

- Check the API documentation at http://localhost:8000/docs
- Review the test files in `backend/app/tests/` for usage examples
- Ensure all required dependencies are installed

## Advanced Features

### Database Persistence

The application automatically saves all data to a SQLite database:
- Player information persists between sessions
- Game history is maintained
- Statistics are calculated from historical data

### Performance Analytics

The system tracks:
- Individual player win/loss records
- Team performance over time
- Skill-based team balancing effectiveness

### Future Enhancements

Planned features include:
- Team correlation analysis
- Advanced statistics and metrics
- Web-based user interface
- Cloud deployment options 