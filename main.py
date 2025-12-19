import sqlite3
from fastapi import FastAPI
import uvicorn

app = FastAPI()
DB_NAME = "movies.db"


class Movie:
    def __init__(self, movieId, title, genres):
        self.movieId = movieId
        self.title = title
        self.genres = genres


class Link:
    def __init__(self, movieId, imdbId, tmdbId):
        self.movieId = movieId
        self.imdbId = imdbId
        self.tmdbId = tmdbId


class Rating:
    def __init__(self, userId, movieId, rating, timestamp):
        self.userId = userId
        self.movieId = movieId
        self.rating = rating
        self.timestamp = timestamp


class Tag:
    def __init__(self, userId, movieId, tag, timestamp):
        self.userId = userId
        self.movieId = movieId
        self.tag = tag
        self.timestamp = timestamp


def get_rows_from_db(table_name):
    connection = sqlite3.connect(DB_NAME)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()

    connection.close()
    return rows


@app.get("/movies")
def get_movies():
    rows = get_rows_from_db("movies")
    results = []

    for row in rows:
        genres_list = row["genres"].split("|")
        movie = Movie(row["movieId"], row["title"], genres_list)
        results.append(movie.__dict__)

    return results


@app.get("/links")
def get_links():
    rows = get_rows_from_db("links")
    results = []

    for row in rows:
        link = Link(row["movieId"], row["imdbId"], row["tmdbId"])
        results.append(link.__dict__)

    return results


@app.get("/ratings")
def get_ratings():
    rows = get_rows_from_db("ratings")
    results = []

    for row in rows:
        rating = Rating(row["userId"], row["movieId"], row["rating"], row["timestamp"])
        results.append(rating.__dict__)

    return results


@app.get("/tags")
def get_tags():
    rows = get_rows_from_db("tags")
    results = []

    for row in rows:
        tag = Tag(row["userId"], row["movieId"], row["tag"], row["timestamp"])
        results.append(tag.__dict__)

    return results


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)