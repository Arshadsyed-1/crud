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
# add employee
@app.post("/employees")
def add_employee(new_data: dict):
    name = new_data["n"]
    email = new_data["e"]
    dept = new_data["d"]
    query = """ insert into employees(name,email,department)values(%s,%s,%s)"""
    values = (name,email,dept)
    cur_obj.execute(query,values)
    conn_obj.commit()
    return {"message ": "employee added successfully"}
#view employee
@app.get("/employees")
def view_employee():
    query = "select * from employees "
    cur_obj.execute(query)
    data = cur_obj.fetchall()
    return data
#update employee
@app.put("/employees/{emp_id}")
def update_employee(emp_id:int,update_data:dict):
    name = update_data["n"]
    email = update_data["e"]
    dept = update_data["d"]
    query = """ update employees set name = %s,email = %s,department=%s where id =%s"""
    values = (name,email,dept,emp_id)
    cur_obj.execute(query,values)
    conn_obj.commit()
    return {"message":"employee update successfully"}
#delete employee
@app.delete("/employees/{emp_id}")
def delete_employee(emp_id:int):
    query = "delete from employees where id = %s"
    values = (emp_id,)
    cur_obj.execute(query,values)
    conn_obj.commit()
    return {"message":"employee deleted succesfully"}



