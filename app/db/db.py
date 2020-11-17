import asyncpg


class Pool:

    def __init__(self, db_conn):
        self.db_conn = db_conn

    async def pool(self):
        pool = await asyncpg.create_pool(dsn=self.db_conn, command_timeout=10)
        return await pool

    async def aquire(self):
        return await self.pool.aquire()


class PlayerDb:

    def __init__(self, pool):
        self.pool = pool

    async def new():
        pass

    async def all(self):
        conn = await self.pool.aquire()
        all_players = await conn.fetch("SELECT * FROM players")
        return all_players

    async def search():
        pass
