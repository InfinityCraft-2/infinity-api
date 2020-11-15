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


# async def auth_token(request: Request):
#     print(request.headers)
#     if token != xtoken:
#         raise HTTPException(status_code=400, detail="X-Token header invalid")

# @app.middleware("http")
# async def auth(request: Request, call_next):
#     pass
# if token in request.headers:
#     print(request.headers['Authorization'])
#     response = await call_next(request)
#     return response
# else:
#     response = await call_next(request)
#     response.status_code = status.HTTP_401_UNAUTHORIZED
#     response.content = "None"
#     response.body = "None"
#     return response
# @requires(["authenticated"], status_code=404)


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
    # dependencies=[Depends(auth_token)],
    responses={404: {"description": "Endpoint not found"}},
)
