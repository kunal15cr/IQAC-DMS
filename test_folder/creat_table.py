import os

import psycopg
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the connection string from the environment variable
conn_string = os.getenv("DATABASE_URL")
Table_name  = "books"  # Table name
try:
    with psycopg.connect(conn_string) as conn:
        print("Connection established")

        # Open a cursor to perform database operations
        with conn.cursor() as cur:
            # Drop the table if it already exists
            cur.execute(f"DROP TABLE IF EXISTS {Table_name};")
            print("Finished dropping table (if it existed).")

            # Create a new table
            cur.execute(f"""
                CREATE TABLE {Table_name} (
                    id SERIAL PRIMARY KEY,
                    title VARCHAR(255) NOT NULL,
                    author VARCHAR(255),
                    publication_year INT,
                    in_stock BOOLEAN DEFAULT TRUE
                );
            """)
            print("Finished creating table.")

            # Insert a single book record
            cur.execute(
                f"INSERT INTO {Table_name} (title, author, publication_year, in_stock) VALUES (%s, %s, %s, %s);",
                ("The Catcher in the Rye", "J.D. Salinger", 1951, True),
            )
            print("Inserted a single book.")

            # Data to be inserted
            books_to_insert = [
                ("The Hobbit", "J.R.R. Tolkien", 1937, True),
                ("1984", "George Orwell", 1949, True),
                ("Dune", "Frank Herbert", 1965, False),
            ]

            # Insert multiple books at once
            cur.executemany(
                "INSERT INTO books (title, author, publication_year, in_stock) VALUES (%s, %s, %s, %s);",
                books_to_insert,
            )

            print("Inserted 3 rows of data.")
            # The transaction is committed automatically when the 'with' block exits in psycopg (v3)

except Exception as e:
    print("Connection failed.")
    print(e)