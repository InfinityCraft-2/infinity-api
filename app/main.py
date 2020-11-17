from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.openapi.utils import get_openapi

from starlette.middleware import Middleware
from starlette.middleware.authentication import AuthenticationMiddleware

from routers import players
from utils import auth, secret
from db import db

DB_POOL = db.Pool(secret.Secret.db_conn)
middleware = [Middleware(AuthenticationMiddleware, backend=auth.KeyAuth())]

app = FastAPI(middleware=middleware)


@app.get("/")
async def root():
    return RedirectResponse("/v1/docs")


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="InfinityCraft 2.∞ API",
        version="0.1.0",
        description="Add Description Later",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.include_router(
    players.router,
    prefix="/players",
    tags=["players"],
    responses={404: {"description": "Endpoint not found"}},
)


app.openapi = custom_openapi
