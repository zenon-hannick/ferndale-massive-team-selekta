# Football Team Selector - API Reference

## Base URL

```
http://localhost:8000
```

## Authentication

Currently, the API does not require authentication. All endpoints are publicly accessible.

## Data Models

### Player

```json
{
  "name": "string",
  "attributes": {
    "attacking": "integer (1-10)",
    "defending": "integer (1-10)",
    "goalkeeping": "integer (1-10)",
    "energy": "integer (1-10)"
  },
  "available": "boolean"
}
```

### Team

```json
{
  "name": "string",
  "players": ["Player"]
}
```

### Game Score

```json
{
  "red_score": "integer",
  "yellow_score": "integer"
}
```

### Game

```json
{
  "date": "string (YYYY-MM-DD)",
  "red_team": "Team",
  "yellow_team": "Team",
  "score": "GameScore"
}
```

## Endpoints

### 1. Root Endpoint

**GET /** - Get application information

**Response:**
```json
{
  "message": "Football Team Selector API"
}
```

**Example:**
```bash
curl -X GET "http://localhost:8000/"
```

### 2. Player Management

#### Create Player

**POST /players/** - Create a new player

**Request Body:**
```json
{
  "name": "John Doe",
  "attributes": {
    "attacking": 8,
    "defending": 6,
    "goalkeeping": 3,
    "energy": 9
  },
  "available": true
}
```

**Response:** `201 Created`
```json
{
  "name": "John Doe",
  "attributes": {
    "attacking": 8,
    "defending": 6,
    "goalkeeping": 3,
    "energy": 9
  },
  "available": true
}
```

**Example:**
```bash
curl -X POST "http://localhost:8000/players/" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "attributes": {
      "attacking": 8,
      "defending": 6,
      "goalkeeping": 3,
      "energy": 9
    },
    "available": true
  }'
```

#### Get All Players

**GET /players/** - Get all players

**Response:** `200 OK`
```json
[
  {
    "name": "John Doe",
    "attributes": {
      "attacking": 8,
      "defending": 6,
      "goalkeeping": 3,
      "energy": 9
    },
    "available": true
  }
]
```

**Example:**
```bash
curl -X GET "http://localhost:8000/players/"
```

#### Get Player Statistics

**GET /players/{player_name}/stats** - Get player performance statistics

**Response:** `200 OK`
```json
{
  "total_games": 5,
  "wins": 3,
  "losses": 2,
  "win_rate": 0.6
}
```

**Example:**
```bash
curl -X GET "http://localhost:8000/players/John%20Doe/stats"
```

### 3. Team Balancing

#### Balance Teams

**POST /teams/balance** - Create balanced teams from available players

**Request Body:**
```json
{
  "players": [
    {
      "name": "Player1",
      "attributes": {
        "attacking": 8,
        "defending": 6,
        "goalkeeping": 3,
        "energy": 9
      },
      "available": true
    }
    // ... more players (10 or 12 total required)
  ]
}
```

**Response:** `200 OK`
```json
{
  "red_team": {
    "name": "Red",
    "players": [
      {
        "name": "Player1",
        "attributes": {
          "attacking": 8,
          "defending": 6,
          "goalkeeping": 3,
          "energy": 9
        },
        "available": true
      }
      // ... 4-5 more players
    ]
  },
  "yellow_team": {
    "name": "Yellows",
    "players": [
      // ... 5-6 players
    ]
  }
}
```

**Error Response:** `400 Bad Request`
```json
{
  "detail": "Expected 10 or 12 available players, got 8"
}
```

**Example:**
```bash
curl -X POST "http://localhost:8000/teams/balance" \
  -H "Content-Type: application/json" \
  -d '{
    "players": [
      {"name": "Alex", "attributes": {"attacking": 8, "defending": 6, "goalkeeping": 3, "energy": 9}, "available": true},
      {"name": "Ben", "attributes": {"attacking": 6, "defending": 8, "goalkeeping": 4, "energy": 7}, "available": true}
      // ... add 8-10 more players
    ]
  }'
```

### 4. Game Management

#### Record Game

**POST /games/** - Record a new game

**Request Body:**
```json
{
  "date": "2024-01-20",
  "red_team": {
    "name": "Red",
    "players": [
      {
        "name": "Player1",
        "attributes": {
          "attacking": 8,
          "defending": 6,
          "goalkeeping": 3,
          "energy": 9
        },
        "available": true
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
          "defending": 8,
          "goalkeeping": 4,
          "energy": 7
        },
        "available": true
      }
    ]
  },
  "score": {
    "red_score": 3,
    "yellow_score": 2
  }
}
```

**Response:** `201 Created`
```json
{
  "date": "2024-01-20",
  "red_team": {
    "name": "Red",
    "players": [...]
  },
  "yellow_team": {
    "name": "Yellows",
    "players": [...]
  },
  "score": {
    "red_score": 3,
    "yellow_score": 2
  }
}
```

**Example:**
```bash
curl -X POST "http://localhost:8000/games/" \
  -H "Content-Type: application/json" \
  -d '{
    "date": "2024-01-20",
    "red_team": {"name": "Red", "players": [...]},
    "yellow_team": {"name": "Yellows", "players": [...]},
    "score": {"red_score": 3, "yellow_score": 2}
  }'
```

#### Get Game History

**GET /games/** - Get all recorded games

**Response:** `200 OK`
```json
[
  {
    "date": "2024-01-20",
    "red_team": {
      "name": "Red",
      "players": [...]
    },
    "yellow_team": {
      "name": "Yellows",
      "players": [...]
    },
    "score": {
      "red_score": 3,
      "yellow_score": 2
    }
  }
]
```

**Example:**
```bash
curl -X GET "http://localhost:8000/games/"
```

## Error Responses

### Common Error Codes

- **400 Bad Request**: Invalid request data or business logic error
- **404 Not Found**: Resource not found
- **422 Unprocessable Entity**: Validation error

### Error Response Format

```json
{
  "detail": "Error message description"
}
```

### Validation Errors

```json
{
  "detail": [
    {
      "loc": ["body", "attributes", "attacking"],
      "msg": "ensure this value is less than or equal to 10",
      "type": "value_error.number.not_le"
    }
  ]
}
```

## Rate Limiting

Currently, there are no rate limits implemented. All endpoints are available without restrictions.

## Data Validation

### Player Attributes

- **attacking**: Integer between 1-10
- **defending**: Integer between 1-10
- **goalkeeping**: Integer between 1-10
- **energy**: Integer between 1-10
- **name**: Required string
- **available**: Boolean

### Game Data

- **date**: String in YYYY-MM-DD format
- **red_score**: Non-negative integer
- **yellow_score**: Non-negative integer

## Team Balancing Algorithm

The team balancing algorithm works as follows:

1. **Calculate Total Skill**: Sum of all attributes for each player
2. **Sort Players**: Order by total skill (highest to lowest)
3. **Distribute Alternately**: Place players alternately in Red and Yellow teams
4. **Ensure Balance**: Algorithm ensures teams have similar total skill levels

### Example Distribution

With 10 players sorted by skill:
- Player 1 (highest skill) → Red Team
- Player 2 → Yellow Team
- Player 3 → Red Team
- Player 4 → Yellow Team
- ... and so on

This creates balanced teams with similar overall skill levels.

## Database Schema

### Players Table
```sql
CREATE TABLE players (
    name TEXT PRIMARY KEY,
    attacking INTEGER,
    defending INTEGER,
    goalkeeping INTEGER,
    energy INTEGER,
    available BOOLEAN
);
```

### Games Table
```sql
CREATE TABLE games (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    red_team_data TEXT,
    yellow_team_data TEXT,
    red_score INTEGER,
    yellow_score INTEGER
);
```

## Testing the API

### Using curl

All examples in this document use curl. You can also use:
- Postman
- Insomnia
- Any HTTP client

### Using the Interactive Documentation

Visit http://localhost:8000/docs for interactive API documentation with:
- Try-it-out functionality
- Request/response examples
- Schema documentation

## Support

For issues or questions:
1. Check the interactive documentation at `/docs`
2. Review the test files in `backend/app/tests/`
3. Check the server logs for error details 