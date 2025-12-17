import csv
from database.db import Base, engine, SessionLocal
from database.models import Movie, Link, Rating, Tag


Base.metadata.create_all(bind=engine)
session = SessionLocal()


with open("database/movies.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        session.add(Movie(movieId=row["movieId"], title=row["title"], genres=row["genres"]))


with open("database/links.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        session.add(Link(movieId=row["movieId"], imdbId=row["imdbId"], tmdbId=row["tmdbId"]))


with open("database/ratings.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        session.add(Rating(userId=row["userId"], movieId=row["movieId"],
                           rating=float(row["rating"]), timestamp=row["timestamp"]))


with open("database/tags.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        session.add(Tag(userId=row["userId"], movieId=row["movieId"],
                        tag=row["tag"], timestamp=row["timestamp"]))

session.commit()
session.close()
print("Wszystkie dane załadowane!")