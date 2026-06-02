# Import FastAPI - the tool that builds our API
from fastapi import FastAPI

# Create the app (this is our API)
app = FastAPI()

# When someone visits the homepage "/", send back this message
@app.get("/")
def home():
    return {"message": "Hello! My first API is working!"}

# When someone visits "/about", send back info about you
@app.get("/about")
def about():
    return {"name": "Radhika", "role": "Automation Engineer in training", "day": 30}

# Greet someone by name (name comes from the URL)
@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello {name}!"}

# Add two numbers (both come from the URL)
@app.get("/add/{a}/{b}")
def add(a: int, b: int):
    return {"result": a + b}
