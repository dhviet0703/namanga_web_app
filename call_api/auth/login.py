import requests


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


def detail_user(access_token):
    url = f"http://localhost:8000/api/user/me/"
    headers = {'Accept': 'application/json',
               'Content-Type': 'application/json',
               'Authorization': f'Bearer {access_token}'}
    response = requests.get(url, headers=headers)
    return response


def check_permission(access_token):
    response = detail_user(access_token)
    if response.status_code == 200:
        if response.json()['role'] == 'SUPER_ADMIN':
            return True
        return False
    return response.json()


def check_login_available(access_token):
    response = detail_user(access_token)
    if response.status_code == 200:
        return True
    return False
