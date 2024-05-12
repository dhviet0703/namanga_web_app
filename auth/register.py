import requests
import streamlit as st
import psycopg2
from passlib.hash import bcrypt

from db.connect import conn


def signup(username, email, password, re_password):
    # hashed_password = bcrypt.hash(password)
    # cursor = conn.cursor()
    # cursor.execute("INSERT INTO users (email, password) VALUES (%s, %s)", (email, hashed_password))
    # conn.commit()
    # cursor.close()
    if password == re_password:
        url = f"http://localhost:8000/api/auth/register/"
        headers = {'Accept': 'application/json',
                   'Content-Type': 'application/json'}
        payload = {
            'username': username,
            'email': email,
            'password': password
        }

        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            st.write("Registered Successfully")
        return response.json()
