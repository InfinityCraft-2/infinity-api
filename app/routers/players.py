from fastapi import APIRouter, HTTPException, status

from app.event import pool
from ..db import db
from ..validation.models import PlayerModel

router = APIRouter()


@router.post("/new")
async def new_player(player: PlayerModel):
    """Create a new player"""
    player = db.PlayerDb(pool).new(player)
    err = str(await player)
    if "error" in err:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=err)
    return await player


@router.get("/all")
async def get_players():
    """Get all Players"""
    players = db.PlayerDb(pool).all()
    return await players


@router.get("/search/id")
async def player_search_id(_id: int):
    """Search for a player via ID in the database."""
    player = db.PlayerDb(pool).search_id(_id)
    return await player


@router.get("/search/uuid")
async def player_search_uuid(
    uuid: str,
):
    """Search for a player via UUID in the database."""
    player = db.PlayerDb(pool).search_uuid(uuid)
    return await player


@router.get("/search/username")
async def player_search_username(
    username: str,
):
    """Search for a player via Username in the database."""
    player = db.PlayerDb(pool).search_username(username)
    return await player
