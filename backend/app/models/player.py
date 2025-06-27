from pydantic import BaseModel, Field, ConfigDict
from typing import Optional


class PlayerAttributes(BaseModel):
    """Player skill attributes model"""
    attacking: int = Field(..., ge=1, le=10, description="Attacking skill (1-10)")
    defending: int = Field(..., ge=1, le=10, description="Defending skill (1-10)")
    goalkeeping: int = Field(..., ge=1, le=10, description="Goalkeeping skill (1-10)")
    energy: int = Field(..., ge=1, le=10, description="Energy level (1-10)")


class Player(BaseModel):
    """Player model"""
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "name": "John Doe",
                "attributes": {
                    "attacking": 7,
                    "defending": 6,
                    "goalkeeping": 3,
                    "energy": 8
                },
                "available": True
            }
        }
    )
    
    name: str = Field(..., min_length=1, description="Player name")
    attributes: PlayerAttributes
    available: bool = Field(default=True, description="Whether the player is available for games") 