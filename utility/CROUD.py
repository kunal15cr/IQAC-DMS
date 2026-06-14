import os

import psycopg
from dotenv import load_dotenv



def create_table(Table_name):
    # Load environment variables from .env file
    load_dotenv()

    # Get the connection string from the environment variable
    conn_string = os.getenv("DATABASE_URL")

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

                
    except Exception as e:
        print("Connection failed.")
        print(e)

def insert_data(Table_name, books_to_insert):
    # Load environment variables from .env file
    load_dotenv()

    # Get the connection string from the environment variable
    conn_string = os.getenv("DATABASE_URL")

    try:
        with psycopg.connect(conn_string) as conn:
            print("Connection established")

            # Open a cursor to perform database operations
            with conn.cursor() as cur:
                # Insert multiple books at once
                cur.executemany(
                    f"INSERT INTO {Table_name} (title, author, publication_year, in_stock) VALUES (%s, %s, %s, %s);",
                    books_to_insert,
                )

                print(f"Inserted {len(books_to_insert)} rows of data.")
                # The transaction is committed automatically when the 'with' block exits in psycopg (v3)

    except Exception as e:
        print("Connection failed.")
        print(e)
create_table("books1")  # Call the function to create the table