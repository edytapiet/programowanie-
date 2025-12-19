import sqlite3
from typing import List
from fastapi import FastAPI
import uvicorn

app = FastAPI()
DB_NAME = "movies.db"



class Movie:
    def __init__(self, movieId: int, title: str, genres: str):
        self.movieId = movieId
        self.title = title
        self.genres = genres.split("|") if genres else []


class Link:
    def __init__(self, movieId: int, imdbId: str, tmdbId: str):
        self.movieId = movieId
        self.imdbId = imdbId
        self.tmdbId = tmdbId


class Rating:
    def __init__(self, userId: int, movieId: int, rating: float, timestamp: int):
        self.userId = userId
        self.movieId = movieId
        self.rating = rating
        self.timestamp = timestamp


class Tag:
    def __init__(self, userId: int, movieId: int, tag: str, timestamp: int):
        self.userId = userId
        self.movieId = movieId
        self.tag = tag
        self.timestamp = timestamp




def fetch_data(table_name, model_class):
    results = []
    with sqlite3.connect(DB_NAME) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()

        for row in rows:

            obj = model_class(**dict(row))
            results.append(obj.__dict__)

    return results




@app.get("/movies")
def get_movies():
    return fetch_data("movies", Movie)


@app.get("/links")
def get_links():
    return fetch_data("links", Link)


@app.get("/ratings")
def get_ratings():
    return fetch_data("ratings", Rating)


@app.get("/tags")
def get_tags():
    return fetch_data("tags", Tag)




if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)