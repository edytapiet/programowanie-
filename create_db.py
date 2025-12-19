import sqlite3
import csv


def make_database():
    print("Starting database creation...")

    connection = sqlite3.connect("movies.db")
    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS movies")
    cursor.execute("CREATE TABLE movies (movieId INTEGER, title TEXT, genres TEXT)")
    print("Created table: movies")

    cursor.execute("DROP TABLE IF EXISTS links")
    cursor.execute("CREATE TABLE links (movieId INTEGER, imdbId TEXT, tmdbId TEXT)")
    print("Created table: links")

    cursor.execute("DROP TABLE IF EXISTS ratings")
    cursor.execute("CREATE TABLE ratings (userId INTEGER, movieId INTEGER, rating REAL, timestamp INTEGER)")
    print("Created table: ratings")

    cursor.execute("DROP TABLE IF EXISTS tags")
    cursor.execute("CREATE TABLE tags (userId INTEGER, movieId INTEGER, tag TEXT, timestamp INTEGER)")
    print("Created table: tags")

    def insert_data(file_name, table_name, columns):
        try:
            with open(file_name, "r", encoding="utf-8") as file:
                reader = csv.reader(file)
                next(reader)

                placeholders = ",".join(["?"] * columns)
                sql = f"INSERT INTO {table_name} VALUES ({placeholders})"

                cursor.executemany(sql, reader)
                print(f"Loaded data from {file_name}")
        except FileNotFoundError:
            print(f"File not found: {file_name}")

    insert_data("movies.csv", "movies", 3)
    insert_data("links.csv", "links", 3)
    insert_data("ratings.csv", "ratings", 4)
    insert_data("tags.csv", "tags", 4)

    connection.commit()
    connection.close()
    print("Database is ready.")


if __name__ == "__main__":
    make_database()