from fastapi import FastAPI
from task_model import Task

app = FastAPI()
#this is a constructor 

tasks = [
    Task(),
    Task()
]

@app.get("/")
def root():
    return "Hello world"

@app.get("/get-all-tasks")
def get_all_tasks():
    return tasks

@app.put("/")
def update_task():
    return "Hello world"

@app.post("/")
def add_task():
    return "Hello world"

@app.delete("/")
def delete_task():
    return "Hello world"
