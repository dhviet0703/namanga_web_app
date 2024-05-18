import requests
import streamlit as st


def login(email, password):
    url = f"http://localhost:8000/api/auth/login/"
    headers = {'Accept': 'application/json',
               'Content-Type': 'application/json'}
    payload = {
        'email': email,
        'password': password
    }
    response = requests.post(url, headers=headers, json=payload)
    return response
