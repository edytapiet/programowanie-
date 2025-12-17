from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database.db import get_db, engine
from database.models import Movie, Link, Rating, Tag, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Serwer API działa! Użyj /movies, /links, /ratings lub /tags aby zobaczyć dane."}

@app.get("/movies")
def read_movies(db: Session = Depends(get_db)):

    movies = db.query(Movie).all()
    return movies

@app.get("/links")
def read_links(db: Session = Depends(get_db)):
    links = db.query(Link).all()
    return links

@app.get("/ratings")
def read_ratings(db: Session = Depends(get_db)):
    ratings = db.query(Rating).all()
    return ratings

@app.get("/tags")
def read_tags(db: Session = Depends(get_db)):
    tags = db.query(Tag).all()
    return tags