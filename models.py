from pydantic import BaseModel, Field, field_validator

# Задание 1.4
class User(BaseModel):
    name: str
    id: int

# Задание 1.5
class UserAge(BaseModel):
    name: str
    age: int

# Задание 2.2 (обновлённая версия 2.1)
class Feedback(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    message: str = Field(..., min_length=10, max_length=500)
    
    @field_validator('message')
    @classmethod
    def check_banned_words(cls, v: str) -> str:
        banned_words = ['кринж', 'рофл', 'вайб']
        v_lower = v.lower()
        
        for word in banned_words:
            if word in v_lower:
                raise ValueError('Использование недопустимых слов')
        return v