import requests
import streamlit as st


def add_manga_api(name, author, introduction, genres, image_file, cookies):
    url = "http://localhost:8000/api/manga/post/"
    token = cookies['token']
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    files = {
        'image_data': (image_file.name, image_file, image_file.type)
    }
    data = {
        'name': name,
        'author': author,
        'introduction': introduction,
        'genres': ' - '.join(genres)
    }

    response = requests.post(url, headers=headers, files=files, data=data)

    if response.status_code == 200:
        st.success("Manga added successfully!")
    else:
        st.error(f"Failed to add manga. Status code: {response.status_code}, Response: {response.text}")


