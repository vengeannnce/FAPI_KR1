from fastapi import FastAPI
from fastapi.responses import FileResponse
from models import User, UserAge, Feedback

app = FastAPI()

feedbacks = []

# Задание 1.2
@app.get("/")
async def read_index():
    return FileResponse("index.html")

# Задание 1.4
@app.get("/users")
async def get_user():
    user = User(name="Ваше Имя и Фамилия", id=1)
    return user

# Задание 1.5
@app.post("/user")
async def check_adult(user: UserAge):
    is_adult = user.age >= 18
    return {
        "name": user.name,
        "age": user.age,
        "is_adult": is_adult
    }

# Задание 2.2
@app.post("/feedback")
async def submit_feedback(feedback: Feedback):
    feedbacks.append(feedback)
    
    return {"message": f"Спасибо, {feedback.name}! Ваш отзыв сохранён."}