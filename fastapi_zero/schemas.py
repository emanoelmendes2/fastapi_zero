from pydantic import BaseModel


class Message(BaseModel):
    message: str


class USerSchema(BaseModel):
    username: str
    email: str
    password: str


class UserDb(USerSchema):
    id: int


class USerPublic(BaseModel):
    id: int
    username: str
    email: str


class UserList(BaseModel):
    users: list[USerPublic]
