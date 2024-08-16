# from fastapi.responses import HTMLResponse
from http import HTTPStatus

from fastapi import FastAPI

from fast_zero.Schemas import Message, UserPublic, UserSchema

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}
    # response_class=HTMLResponse,
    # return """
    # <html>
    #   <head>
    #     <title> Nosso olá mundo!</title>
    #   </head>
    #   <body>
    #     <h1> Olá Mundo </h1>
    #   </body>
    # </html>"""


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user=UserSchema): 
    return user
