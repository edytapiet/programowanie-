import csv
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

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


class Movie:
    def __init__(self, movieId: str, title: str, genres: str):
        self.movieId = movieId
        self.title = title
        self.genres = genres


@app.get("/movies")
def get_movies():
    movies_list = []


    try:
        with open('database/movies.csv', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:

                movie = Movie(
                    movieId=row['movieId'],
                    title=row['title'],
                    genres=row['genres']
                )
                movies_list.append(movie)

    except FileNotFoundError:

        return {"error": "Plik movies.csv nie został znaleziony w katalogu database/"}


    return [m.__dict__ for m in movies_list]




class Link:
    def __init__(self, movieId: str, imdbId: str, tmdbId: str):
        self.movieId = movieId
        self.imdbId = imdbId
        self.tmdbId = tmdbId

class Rating:
    def __init__(self, userId: str, movieId: str, rating: float, timestamp: str):
        self.userId = userId
        self.movieId = movieId
        self.rating = rating
        self.timestamp = timestamp

class Tag:
    def __init__(self, userId: str, movieId: str, tag: str, timestamp: str):
        self.userId = userId
        self.movieId = movieId
        self.tag = tag
        self.timestamp = timestamp


@app.get("/links")
def get_links():
    links_list = []
    try:
        with open('database/links.csv', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                link = Link(
                    movieId=row['movieId'],
                    imdbId=row['imdbId'],
                    tmdbId=row['tmdbId']
                )
                links_list.append(link)
    except FileNotFoundError:
        return {"error": "Plik links.csv nie został znaleziony w katalogu database/"}
    return [l.__dict__ for l in links_list]


@app.get("/ratings")
def get_ratings():
    ratings_list = []
    try:
        with open('database/ratings.csv', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                rating = Rating(
                    userId=row['userId'],
                    movieId=row['movieId'],
                    rating=float(row['rating']),
                    timestamp=row['timestamp']
                )
                ratings_list.append(rating)
    except FileNotFoundError:
        return {"error": "Plik ratings.csv nie został znaleziony w katalogu database/"}
    return [r.__dict__ for r in ratings_list]


@app.get("/tags")
def get_tags():
    tags_list = []
    try:
        with open('database/tags.csv', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                tag = Tag(
                    userId=row['userId'],
                    movieId=row['movieId'],
                    tag=row['tag'],
                    timestamp=row['timestamp']
                )
                tags_list.append(tag)
    except FileNotFoundError:
        return {"error": "Plik tags.csv nie został znaleziony w katalogu database/"}
    return [t.__dict__ for t in tags_list]
