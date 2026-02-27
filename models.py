from pydantic import BaseModel

# Задание 1.4
class User(BaseModel):
    name: str
    id: int

# Задание 1.5
class UserAge(BaseModel):
    name: str
    age: int

# Задание 2.1
class Feedback(BaseModel):
    name: str
    message: str