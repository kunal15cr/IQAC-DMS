import os
import psycopg
from dotenv import load_dotenv


def create_tables():
    load_dotenv()

    conn_string = os.getenv("DATABASE_URL")

    try:
        with psycopg.connect(conn_string) as conn:
            with conn.cursor() as cur:

                # =====================================
                # 1. Research Projects Table
                # =====================================
                cur.execute("""
                CREATE TABLE IF NOT EXISTS research_projects (
                    id SERIAL PRIMARY KEY,
                    division VARCHAR(255),
                    school VARCHAR(255),
                    department VARCHAR(255),
                    pi_co_pi VARCHAR(255),
                    project_title TEXT,
                    funding_agency VARCHAR(255),
                    grant_year INT,
                    abstract TEXT,
                    sanction_date DATE,
                    sanctioned_grant NUMERIC(15,2),
                    sanction_letter_link TEXT
                );
                """)

                # =====================================
                # 2. PhD Scholars Table
                # =====================================
                cur.execute("""
                CREATE TABLE IF NOT EXISTS phd_scholars (
                    id SERIAL PRIMARY KEY,
                    division VARCHAR(255),
                    school VARCHAR(255),
                    department VARCHAR(255),
                    scholar_name VARCHAR(255),
                    supervisor_name VARCHAR(255),
                    registration_year INT,
                    completion_year INT,
                    academic_year VARCHAR(50),
                    pdf_link TEXT
                );
                """)

                # =====================================
                # 3. Consultancy Projects Table
                # =====================================
                cur.execute("""
                CREATE TABLE IF NOT EXISTS consultancy_projects (
                    id SERIAL PRIMARY KEY,
                    division VARCHAR(255),
                    school VARCHAR(255),
                    department VARCHAR(255),
                    faculty_consultant VARCHAR(255),
                    month VARCHAR(20),
                    year INT,
                    organization_name VARCHAR(255),
                    project_title TEXT,
                    consultancy_duration VARCHAR(255),
                    amount_generated NUMERIC(15,2),
                    consultancy_proof_link TEXT,
                    payment_proof_link TEXT
                );
                """)

                conn.commit()
                print("All tables created successfully.")

    except Exception as e:
        print("Error:", e)


create_tables()