from pydantic import BaseModel

class User(BaseModel):
    username: str
    public_key: str
    signature: str
    friends: list[str] = []

collection = "user"