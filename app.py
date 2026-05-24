

import streamlit as st
import requests
import pandas as pd

server_location = "http://127.0.0.1:8000"

st.title("CRUD OPERATION USING THE API")

opt = st.sidebar.selectbox("Select an operation", ["add_employee", "view_employee", "Update_employee", "Delete_employee"])

if opt == "add_employee":
    st.header("Add Employee")
    with st.form("adding"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        dept = st.selectbox("Department", options=[" ", "dev", "tester", "HR", "IT", "Finance", "Marketing"])
        btn = st.form_submit_button("Submit")

        if btn:
            new_data = {"n": name, "e": email, "d": dept}
            response = requests.post(f"{server_location}/employees", json=new_data)
            st.write(response.json())

                                                       
elif opt == "view_employee":
    st.header("View Employee")
    response = requests.get(f"{server_location}/employees")
    data = response.json()
    df = pd.DataFrame(data)
    st.dataframe(df)
elif opt == "Update_employee":
    st.header("Update Employee")
    employee_id = st.number_input("Employee ID",min_value=1)
    name = st.text_input("new_Name")
    email = st.text_input("new_Email")
    dept = st.selectbox("new_Department", options=[" ", "dev", "tester", "HR", "IT", "Finance", "Marketing"])
    btn = st.form_submit_button("Update")
    if btn:
        new_data = {"n": name, "e": email, "d": dept}
        response = requests.put(f"{server_location}/employees/{employee_id}", json=new_data)
        st.write(response.json())
elif opt == "Delete_employee":
    st.header("Delete Employee")
    employee_id = st.number_input("Employee ID", min_value=1)
    btn = st.form_submit_button("Delete")
    if btn:
        response = requests.delete(f"{server_location}/employees/{employee_id}")
        st.write(response.json())


        