from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.openapi.utils import get_openapi

from starlette.middleware import Middleware
from starlette.middleware.authentication import AuthenticationMiddleware

from app.routers import players
from app.utils import auth, secret
from app.event import reg_pool

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
    prefix="/player",
    tags=["players"],
    responses={404: {"description": "Endpoint not found"}},
)


app.openapi = custom_openapi
reg_pool(app, secret.Secret.db_conn)
