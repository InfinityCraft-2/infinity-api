from fastapi import Depends, FastAPI
from fastapi.responses import RedirectResponse
from fastapi.security import OAuth2PasswordBearer
from typing import Optional
# from jose import JWTError, jwt
# import db

app = FastAPI()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.on_event("startup")
async def create_pool():
    pass


@app.get("/")
@app.get("/curie")
async def root():
    return RedirectResponse("/docs")


@app.get("/test/")
async def get_test(token: str = Depends(oauth2_scheme)):
    return {"token": token}


@app.post("/curie/player/new")
async def new_player():
    """Create a new player"""
    pass


@app.get("/curie/player/search")
async def player_search(
    uuid: Optional[str] = None,
    username: Optional[str] = None,
    id: Optional[int] = None
):
    """Search for a player via UUID, username, or ID in the database."""
    pass
