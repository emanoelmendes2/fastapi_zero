from http import HTTPStatus

from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from fastapi.responses import HTMLResponse

from fastapi_zero.schemas import (
    Message,
    UserDb,
    UserList,
    USerPublic,
    USerSchema,
)

app = FastAPI()

database = []


@app.get("/", status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {"message": "Hello World"}


@app.get("/html", status_code=HTTPStatus.OK, response_class=HTMLResponse)
def read_html():
    return """
    <html>
      <head>
        <title> Nosso olá mundo!</title>
      </head>
      <body>
        <h1> Olá Mundo </h1>
      </body>
    </html>"""


@app.post("/users/", status_code=HTTPStatus.CREATED, response_model=USerPublic)
def create_user(user: USerSchema):
    user_with_id = UserDb(
        id=len(database) + 1,
        **user.model_dump(),  # trasforma o objeto em um dicionário
    )
    database.append(user_with_id)
    return user_with_id


@app.get("/users/", response_model=UserList)
def read_users():
    return {"users": database}


@app.put("/users/{user_id}", response_model=USerPublic)
def update_user(user_id: int, user: USerSchema):
    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="User not found",
        )
    user_with_id = UserDb(
        id=user_id,
        **user.model_dump(),  # trasforma o objeto em um dicionário
    )
    database[user_id - 1] = user_with_id
    return user_with_id


@app.delete("/users/{user_id}", response_model=Message)
def delete_user(user_id: int):
    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="User not found",
        )

    del database[user_id - 1]
    return {"message": "User deleted successfully"}


@app.get("/users_one/{user_id}", response_model=USerPublic)
def read_users_one(user_id: int):
    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail="User not found",
        )
    return database[user_id - 1]
