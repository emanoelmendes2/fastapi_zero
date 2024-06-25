from http import HTTPStatus
from fastapi import FastAPI
from fastapi_zero.schemas import Message
from fastapi.responses import HTMLResponse


app = FastAPI()


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