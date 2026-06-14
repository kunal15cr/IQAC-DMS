import os
import psycopg
from dotenv import load_dotenv
import streamlit as st  

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

data =read_table_projects("research_projects") 

def data_Fream(data):
    product_data = {
    "ID": [row[0] for row in data],
    "Division": [row[1] for row in data],
    "School": [row[2] for row in data],
    "Department": [row[3] for row in data],
    "Principal Investigator": [row[4] for row in data],
    "Project Title": [row[5] for row in data],
    "Funding Agency": [row[6] for row in data],
    "Year": [row[7] for row in data],
    "Abstract": [row[8] for row in data],
    "Sanction Date": [row[9].strftime("%d-%m-%Y") for row in data],
    "Amount": [float(row[10]) for row in data],
    "Document": [row[11] for row in data],
}
    return product_data

result = data_Fream(data)

st.table(result)

def Get_data():
    data =read_table_projects("research_projects") 
    result = data_Fream(data)
    return result