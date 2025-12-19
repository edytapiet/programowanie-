import sqlite3
import csv

DB_NAME = "movies.db"

def setup_database():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()

        schemas = {
            "movies": "movieId INTEGER PRIMARY KEY, title TEXT, genres TEXT",
            "links":  "movieId INTEGER, imdbId TEXT, tmdbId TEXT",
            "ratings": "userId INTEGER, movieId INTEGER, rating REAL, timestamp INTEGER",
            "tags":    "userId INTEGER, movieId INTEGER, tag TEXT, timestamp INTEGER"
        }

        print("--- Setting up Database ---")

        for table, columns in schemas.items():
            cursor.execute(f"DROP TABLE IF EXISTS {table}")
            cursor.execute(f"CREATE TABLE {table} ({columns})")
            print(f"Table '{table}' created.")

        print("\n--- Loading Data ---")

        files_map = [
            ("movies.csv", "movies", 3),
            ("links.csv", "links", 3),
            ("ratings.csv", "ratings", 4),
            ("tags.csv", "tags", 4)
        ]

        for filename, table, col_count in files_map:
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    reader = csv.reader(f)
                    next(reader)
                    placeholders = ",".join(["?"] * col_count)
                    cursor.executemany(f"INSERT INTO {table} VALUES ({placeholders})", reader)
                    print(f"Data loaded into '{table}'")
            except FileNotFoundError:
                print(f"Error: File '{filename}' not found.")

        print("\nDatabase setup completed.")

if __name__ == "__main__":
    setup_database()