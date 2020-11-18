import asyncpg


class Pool:
    def __init__(self, db_conn):
        self.db_conn = db_conn
        self._pool = None

    async def _init(self):
        self._pool = await asyncpg.create_pool(dsn=self.db_conn, command_timeout=10)  # NOQA
        return self

    @property
    async def acquire(self):
        return await self._pool.acquire()

    async def release(self, conn):
        return await self._pool.release(conn)


class PlayerDb:
    def __init__(self, db_pool):
        self.db_pool = db_pool

    async def new(self, player):
        conn = await self.db_pool.acquire
        try:
            await conn.execute(
                """
            INSERT INTO public.players (uu_id, username, nickname) VALUES ($1, $2, $3)""",  # NOQA
                player.uu_id,
                player.username,
                player.nickname,
            )
            await self.db_pool.release(conn)
            get_last = await self.search_uuid(player.uu_id)
            return get_last
        except asyncpg.UniqueViolationError as e:
            err = {"error_detail": e.detail}
            return err

    async def all(self):
        conn = await self.db_pool.acquire
        all_players = await conn.fetch("SELECT * FROM public.players")
        await self.db_pool.release(conn)
        return all_players

    async def search_id(self, q: int):
        conn = await self.db_pool.acquire
        player = await conn.fetchrow(
                                """
                                SELECT * FROM public.players WHERE id = $1
                                """, q,)
        await self.db_pool.release(conn)
        return player

    async def search_uuid(self, q: str):
        conn = await self.db_pool.acquire
        player = await conn.fetchrow(
            """
                                SELECT * FROM public.players WHERE uu_id = $1
                                """,
            q,
        )
        await self.db_pool.release(conn)
        return player

    async def search_username(self, q: str):
        conn = await self.db_pool.acquire
        player = await conn.fetchrow(
            """
                            SELECT * FROM public.players WHERE username = $1
                                """,
            q,
        )
        await self.db_pool.release(conn)
        return player
