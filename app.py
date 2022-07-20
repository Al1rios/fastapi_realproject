from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4

from requests import delete


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


@app.get("/animals/{animail_id}")
def get_animal(animail_id: str):
    for animal in db:
        if animal.id == animail_id:
            return animal
        return {"message":"animal not exist"}


@app.delete("/animals/{animal_id}")
def delete_animal(animal_id: str):
    for index, animal in enumerate(db):
        if animal.id == animal_id:
            db.pop(index)
            return {"message":"success"}
    return {"message":"id not exist"}

@app.post("/animals")
def create_animal(animal: Animal):
    animal.id = str(uuid4())
    db.append(animal)
    return None
