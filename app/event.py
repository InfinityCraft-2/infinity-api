from fastapi import FastAPI
from app.db import db
from app.utils import secret

pool = db.Pool(secret.Secret.db_conn)


def reg_pool(app: FastAPI, db_url: str):
    @app.on_event("startup")
    async def init():

        await pool._init()
