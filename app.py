from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4


app = FastAPI()


class Animals(BaseModel):
    id = int
    name = str
    age = int
    sex = str
    color = str


db: list[Animals] = []


@app.get("/animals")
def list_animals():
    return db


@app.post("/animals")
def create_animal(animal: Animals):
    #animal.id = uuid4()
    db.append(animal)
    return None
