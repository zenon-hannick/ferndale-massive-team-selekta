# Football Team Selector - Quick Start Guide

## 🚀 Get Started in 5 Minutes

This guide will help you get the Football Team Selector up and running quickly.

## Prerequisites

- Python 3.9 or higher
- Git (optional)

## Step 1: Start the Server

```bash
cd backend
python3 run_server.py
```

✅ **Success**: You should see:
```
INFO: Uvicorn running on http://0.0.0.0:8000
INFO: Application startup complete.
```

## Step 2: Test the API

Open a new terminal and test the API:

```bash
# Test the root endpoint
curl -X GET "http://localhost:8000/"

# Expected response:
# {"message":"Football Team Selector API"}
```

## Step 3: Add Some Players

```bash
# Add a striker
curl -X POST "http://localhost:8000/players/" \
  -H "Content-Type: application/json" \
  -d '{"name": "Alex", "attributes": {"attacking": 9, "defending": 4, "goalkeeping": 2, "energy": 8}, "available": true}'

# Add a defender
curl -X POST "http://localhost:8000/players/" \
  -H "Content-Type: application/json" \
  -d '{"name": "Ben", "attributes": {"attacking": 3, "defending": 9, "goalkeeping": 4, "energy": 7}, "available": true}'

# Add a midfielder
curl -X POST "http://localhost:8000/players/" \
  -H "Content-Type: application/json" \
  -d '{"name": "Charlie", "attributes": {"attacking": 7, "defending": 7, "goalkeeping": 3, "energy": 9}, "available": true}'
```

## Step 4: View Your Players

```bash
curl -X GET "http://localhost:8000/players/" | python3 -m json.tool
```

## Step 5: Create Balanced Teams

You need 10 players total. Add 7 more players first, then:

```bash
curl -X POST "http://localhost:8000/teams/balance" \
  -H "Content-Type: application/json" \
  -d '{
    "players": [
      {"name": "Alex", "attributes": {"attacking": 9, "defending": 4, "goalkeeping": 2, "energy": 8}, "available": true},
      {"name": "Ben", "attributes": {"attacking": 3, "defending": 9, "goalkeeping": 4, "energy": 7}, "available": true},
      {"name": "Charlie", "attributes": {"attacking": 7, "defending": 7, "goalkeeping": 3, "energy": 9}, "available": true}
      // ... add 7 more players to reach 10 total
    ]
  }'
```

## Step 6: Record a Game

```bash
curl -X POST "http://localhost:8000/games/" \
  -H "Content-Type: application/json" \
  -d '{
    "date": "2024-01-20",
    "red_team": {"name": "Red", "players": [/* your red team players */]},
    "yellow_team": {"name": "Yellows", "players": [/* your yellow team players */]},
    "score": {"red_score": 3, "yellow_score": 2}
  }'
```

## Step 7: Check Player Stats

```bash
curl -X GET "http://localhost:8000/players/Alex/stats"
```

## 🎯 What You've Accomplished

✅ **Started the server**  
✅ **Added players** with skill ratings  
✅ **Created balanced teams** using intelligent algorithm  
✅ **Recorded a game** with results  
✅ **Viewed player statistics**  

## 📚 Next Steps

- **Read the full User Guide**: `docs/USER_GUIDE.md`
- **Explore the API**: Visit http://localhost:8000/docs
- **Check the API Reference**: `docs/API_REFERENCE.md`
- **Learn the technical details**: `docs/TECHNICAL_DOCUMENTATION.md`

## 🔧 Troubleshooting

### Server Won't Start
```bash
# Check if port 8000 is in use
lsof -i :8000

# Use a different port
python3 -m uvicorn app.main:app --reload --port 8001
```

### "Expected 10 or 12 players" Error
- Add more players until you have exactly 10 or 12
- Ensure all players have `"available": true`

### Player Not Found
- Check spelling and case sensitivity
- Use URL encoding for spaces: `John%20Doe`

## 🎮 Interactive API Documentation

Visit **http://localhost:8000/docs** for:
- Try-it-out functionality
- Interactive examples
- Schema documentation
- Request/response examples

## 📊 Example Data

Here's a complete set of 10 players to get you started:

```json
[
  {"name": "Alex", "attributes": {"attacking": 9, "defending": 4, "goalkeeping": 2, "energy": 8}, "available": true},
  {"name": "Ben", "attributes": {"attacking": 3, "defending": 9, "goalkeeping": 4, "energy": 7}, "available": true},
  {"name": "Charlie", "attributes": {"attacking": 7, "defending": 7, "goalkeeping": 3, "energy": 9}, "available": true},
  {"name": "David", "attributes": {"attacking": 5, "defending": 8, "goalkeeping": 5, "energy": 6}, "available": true},
  {"name": "Emma", "attributes": {"attacking": 8, "defending": 5, "goalkeeping": 1, "energy": 10}, "available": true},
  {"name": "Frank", "attributes": {"attacking": 4, "defending": 6, "goalkeeping": 7, "energy": 5}, "available": true},
  {"name": "Grace", "attributes": {"attacking": 6, "defending": 8, "goalkeeping": 3, "energy": 8}, "available": true},
  {"name": "Henry", "attributes": {"attacking": 7, "defending": 6, "goalkeeping": 4, "energy": 7}, "available": true},
  {"name": "Ivy", "attributes": {"attacking": 8, "defending": 4, "goalkeeping": 2, "energy": 9}, "available": true},
  {"name": "Jack", "attributes": {"attacking": 5, "defending": 7, "goalkeeping": 6, "energy": 6}, "available": true}
]
```

## 🚀 Ready to Go!

You now have a fully functional Football Team Selector! The application will:
- **Intelligently balance teams** based on player skills
- **Track game results** and player performance
- **Provide statistics** for individual players
- **Store all data** persistently

Happy team building! ⚽ 