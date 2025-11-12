"""FastAPI application for testing workshop."""

from fastapi import FastAPI, HTTPException

from .calculator import Calculator
from .user_service import UserService

app = FastAPI()
calc = Calculator()
user_service = UserService()


@app.get("/")
def read_root():
    return {"message": "Testing Workshop API"}


@app.get("/calculate/add/{a}/{b}")
def add_numbers(a: float, b: float):
    return {"result": calc.add(a, b)}


@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = user_service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
