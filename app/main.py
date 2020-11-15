from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from starlette.middleware import Middleware
from starlette.middleware.authentication import AuthenticationMiddleware

from routers import players
from utils import auth

middleware = [
    Middleware(AuthenticationMiddleware, backend=auth.KeyAuth())
]

app = FastAPI(middleware=middleware)


@app.on_event("startup")
async def create_pool():
    pass


@app.get("/test")
async def test():
    return {"test": "failed"}


@app.get("/")
async def root():
    return RedirectResponse("/v1/docs")

app.include_router(
    players.router,
    prefix="/players",
    tags=["players"],
    responses={404: {"description": "Endpoint not found"}},
)
