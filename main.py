# main.py
from typing import Union
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database.db import get_db
from database.models import Movie, Link, Rating, Tag

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

@app.get("/movies")
def get_movies(db: Session = Depends(get_db)):
    return db.query(Movie).all()

@app.get("/links")
def get_links(db: Session = Depends(get_db)):
    return db.query(Link).all()

@app.get("/ratings")
def get_ratings(db: Session = Depends(get_db)):
    return db.query(Rating).limit(100).all()

@app.get("/tags")
def get_tags(db: Session = Depends(get_db)):
    return db.query(Tag).all()
