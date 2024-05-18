import requests
import streamlit as st


def signup(username, email, password, re_password):
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
        return response


def verify(email, verify_code):
    url = f'http://localhost:8000/api/auth/verify-code/'
    headers = {'Accept': 'application/json',
               'Content-Type': 'application/json'}
    payload = {
        'email': email,
        'verify_code': verify_code
    }
    response = requests.post(url, headers=headers, json=payload)
    return response
