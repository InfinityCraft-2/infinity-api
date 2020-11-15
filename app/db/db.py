import asyncpg
from secret import Secret


class PostgresConn:
    async def make_pool(self):
        async with asyncpg.create_pool(dsn=Secret.db_conn) as pool:

            async with pool.aquire() as con:
                await con.fetch(
                    """
                    SELECT * FROM players
                """
                )
