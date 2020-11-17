from fastapi import APIRouter

from typing import Optional

import main as DB_POOL
from ..db import db
from ..validation.models import PlayerModel

router = APIRouter()


@router.get("/all")
async def get_players():
    """Get all Players"""
    players = db.PlayerDb(DB_POOL)
    return await players.all()


@router.post("/new")
async def new_player(player: PlayerModel):
    """Create a new player"""
    pass


@router.get("/search")
async def player_search(
    uuid: Optional[str] = None,
    username: Optional[str] = None,
    id: Optional[int] = None,
):
    """Search for a player via UUID, username, or ID in the database."""
    pass
