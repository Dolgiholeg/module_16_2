from fastapi import FastAPI, Response, Path
from typing import Annotated


app = FastAPI()

@app.get("/user/{user_id}")
async def your_number(user_id: int = Path(ge=1, le=100, description="Enter User ID", example="1")):
    data = '"Вы вошли как пользователь №' f'{user_id}"'
    return Response(content=data, media_type="text/plain")

@app.get("/user/{user_id}")
async def your_number(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID", example="1")]):
    data = '"Вы вошли как пользователь №' f'{user_id}"'
    return Response(content=data, media_type="text/plain")

@app.get("/user/{username}/{age}")
async def user_information(username: str = Path(min_length=5, max_length=20, deprecated="Enter username", example="UrbanUser"),
               age: int = Path(ge=18, le=120, description="Enter age", example="24")):
    data = '"Информация о пользователе. Имя:'f'{username}' ', Возраст:'f'{age}".'
    return Response(content=data, media_type="text/plain")

@app.get("/user/{username}/{age}")
async def user_information(username: Annotated[str, Path(min_length=5, max_length=20, deprecated="Enter username", example="UrbanUser")],
               age: Annotated[int, Path(ge=18, le=120, description="Enter age", example="24")]):
    data = '"Информация о пользователе. Имя:'f'{username}' ', Возраст:'f'{age}".'
    return Response(content=data, media_type="text/plain")


