import csv
from fastapi import FastAPI

app = FastAPI()


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



@app.get("/movies")
def get_movies():
    movies_list = []
    with open('movies.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:

            movie_obj = Movie(row['movieId'], row['title'], row['genres'])
            # Serializacja za pomocą __dict__ i dodanie do listy
            movies_list.append(movie_obj.__dict__)
    return movies_list

@app.get("/links")
def get_links():
    links_list = []
    with open('links.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            link_obj = Link(row['movieId'], row['imdbId'], row['tmdbId'])
            links_list.append(link_obj.__dict__)
    return links_list

@app.get("/ratings")
def get_ratings():
    ratings_list = []
    with open('ratings.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            rating_obj = Rating(row['userId'], row['movieId'], row['rating'], row['timestamp'])
            ratings_list.append(rating_obj.__dict__)
    return ratings_list

@app.get("/tags")
def get_tags():
    tags_list = []
    with open('tags.csv', mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            tag_obj = Tag(row['userId'], row['movieId'], row['tag'], row['timestamp'])
            tags_list.append(tag_obj.__dict__)
    return tags_list


