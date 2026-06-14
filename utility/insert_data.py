import os
import psycopg
from dotenv import load_dotenv

load_dotenv()
conn_string = os.getenv("DATABASE_URL")


# ==========================================
# 1. INSERT INTO RESEARCH PROJECTS
# ==========================================
def insert_research_project(
    division,
    school,
    department,
    pi_co_pi,
    project_title,
    funding_agency,
    grant_year,
    abstract,
    sanction_date,
    sanctioned_grant,
    sanction_letter_link
):
    try:
        with psycopg.connect(conn_string) as conn:
            with conn.cursor() as cur:

                cur.execute("""
                    INSERT INTO research_projects (
                        division,
                        school,
                        department,
                        pi_co_pi,
                        project_title,
                        funding_agency,
                        grant_year,
                        abstract,
                        sanction_date,
                        sanctioned_grant,
                        sanction_letter_link
                    )
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                """, (
                    division,
                    school,
                    department,
                    pi_co_pi,
                    project_title,
                    funding_agency,
                    grant_year,
                    abstract,
                    sanction_date,
                    sanctioned_grant,
                    sanction_letter_link
                ))

                print("Research Project inserted successfully")

    except Exception as e:
        print("Error:", e)


# ==========================================
# 2. INSERT INTO PHD SCHOLARS
# ==========================================
def insert_phd_scholar(
    division,
    school,
    department,
    scholar_name,
    supervisor_name,
    registration_year,
    completion_year,
    academic_year,
    pdf_link
):
    try:
        with psycopg.connect(conn_string) as conn:
            with conn.cursor() as cur:

                cur.execute("""
                    INSERT INTO phd_scholars (
                        division,
                        school,
                        department,
                        scholar_name,
                        supervisor_name,
                        registration_year,
                        completion_year,
                        academic_year,
                        pdf_link
                    )
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
                """, (
                    division,
                    school,
                    department,
                    scholar_name,
                    supervisor_name,
                    registration_year,
                    completion_year,
                    academic_year,
                    pdf_link
                ))

                print("PhD Scholar inserted successfully")

    except Exception as e:
        print("Error:", e)


# ==========================================
# 3. INSERT INTO CONSULTANCY PROJECTS
# ==========================================
def insert_consultancy_project(
    division,
    school,
    department,
    faculty_consultant,
    month,
    year,
    organization_name,
    project_title,
    consultancy_duration,
    amount_generated,
    consultancy_proof_link,
    payment_proof_link,
):
    try:
        with psycopg.connect(conn_string) as conn:
            with conn.cursor() as cur:

                cur.execute("""
                    INSERT INTO consultancy_projects (
                        division,
                        school,
                        department,
                        faculty_consultant,
                        month,
                        year,
                        organization_name,
                        project_title,
                        consultancy_duration,
                        amount_generated,
                        consultancy_proof_link,
                        payment_proof_link
                       
                    )
                    VALUES (
                        %s, %s, %s, %s, %s, %s, %s,
                        %s, %s, %s, %s, %s
                    );
                """, (
                    division,
                    school,
                    department,
                    faculty_consultant,
                    month,
                    year,
                    organization_name,
                    project_title,
                    consultancy_duration,
                    amount_generated,
                    consultancy_proof_link,
                    payment_proof_link
                ))

                print("Consultancy Project inserted successfully")

    except Exception as e:
        print("Error:", e)


# insert_research_project(
#     "Engineering",
#     "School of Technology",
#     "Computer Science",
#     "Dr. Shahbaz Dandin",
#     "AI Analytics Platform",
#     "UGC",
#     2025,
#     "Research on AI-based analytics.",
#     "2025-05-10",
#     500000,
#     "https://example.com/sanction.pdf"
# )


# insert_phd_scholar(
#     "Engineering",
#     "School of Technology",
#     "Computer Science",
#     "Kapil Patil",
#     "Dr. Shahbaz Dandin",
#     2022,
#     2026,
#     "2025-26",
#     "https://example.com/thesis.pdf"
# )

# insert_consultancy_project(
#     "Engineering",
#     "School of Technology",
#     "Computer Science",
#     "Prof. ABC",
#     "June",
#     2025,
#     "XYZ Pvt Ltd",
#     "Data Analytics Consulting",
#     "3 Months",
#     150000,
#     "https://example.com/proof1.pdf",
#     "https://example.com/proof2.pdf"
# )