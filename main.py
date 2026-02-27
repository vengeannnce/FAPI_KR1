from fastapi import FastAPI
from fastapi.responses import FileResponse
from models import User

app = FastAPI()

# Задание 1.2
@app.get("/")
async def read_index():
    return FileResponse("index.html")

# Задание 1.4
@app.get("/users")
async def get_user():
    user = User(name="Азамат Дудаев", id=5985)
    return user