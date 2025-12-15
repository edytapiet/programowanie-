import csv
from database.db import Base, engine, SessionLocal
from database.models import Movie, Link, Rating, Tag

Base.metadata.create_all(bind=engine)

session = SessionLocal()

# movies.csv
with open("database/movies.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        movie = Movie(movieId=row["movieId"], title=row["title"], genres=row["genres"])
        session.add(movie)

# podobnie links.csv, ratings.csv, tags.csv

session.commit()
session.close()
print("Dane załadowane do SQLite")
