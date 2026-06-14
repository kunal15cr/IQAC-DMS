import os
import psycopg
from dotenv import load_dotenv

load_dotenv()
conn_string = os.getenv("DATABASE_URL")

def read_table_projects(table_name):
    try:
        with psycopg.connect(conn_string) as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT * FROM {table_name};")
                projects = cur.fetchall()
                return projects

    except Exception as e:
        print(f"Error reading table projects: {e}")
        return []

print(read_table_projects("research_projects") )