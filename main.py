from fastapi import FastAPI
import mysql.connector

conn_obj=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Syed@0756",
    database="api_crud_db"
)
cur_obj = conn_obj.cursor()

app = FastAPI()
@app.post("/employees")
def add_employee(new_data: dict):
    name = new_data["n"]
    email = new_data["e"]
    dept = new_data["d"]