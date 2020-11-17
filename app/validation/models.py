from pydantic import BaseModel


class PlayerModel(BaseModel):
    uu_id: str
    username: str
    nickname: str = None
