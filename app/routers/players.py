from fastapi import APIRouter
from typing import Optional


router = APIRouter()


@router.post("/test")
async def test_player():
    """Create a new player"""
    return {"player": "test player"}


@router.post("/new")
async def new_player():
    """Create a new player"""
    pass


@router.get("/search")
async def player_search(
    # token: str = Depends(oauth2_scheme),
    uuid: Optional[str] = None,
    username: Optional[str] = None,
    id: Optional[int] = None,
):
    """Search for a player via UUID, username, or ID in the database."""
    pass
