from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4


app = FastAPI()


class Animal(BaseModel):
    id: Optional[str]
    name: str
    age: int
    sex: str
    color: str


db: List[Animal] = []


@app.get("/animals")
def list_animals():
    return db


@app.get("/animals/{animail_id:str}")
def get_animal(animail_id):
    for animal in db:
        if animail_id == animal.id:
            return animal

@app.post("/animals")
def create_animal(animal: Animal):
    animal.id = uuid4()
    db.append(animal)
    return None
