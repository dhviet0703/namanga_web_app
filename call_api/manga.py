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


def update_manga_api(id_manga, name, author, introduction, genres, image_file, cookies):
    url = "http://localhost:8000/api/manga/put/"
    token = cookies['token']
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {token}'
    }
    data = {'manga_id': id_manga}
    if name:
        data['name'] = name
    if author:
        data['author'] = author
    if introduction:
        data['introduction'] = introduction
    if genres:
        data['genres'] = genres
    if image_file:
        files = {'image_data': (image_file.name, image_file, image_file.type)}
        response = requests.put(url, headers=headers, files=files, data=data)
    else:
        response = requests.put(url, headers=headers, data=data)

    if response.status_code == 200:
        st.success("Manga update successfully!")
    else:
        st.error(f"Failed to update manga. Status code: {response.status_code}, Response: {response.text}")


def delete_manga_api(id_manga, cookies):
    url = f"http://localhost:8000/api/manga/delete/?manga_id={id_manga}"
    token = cookies['token']
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {token}'
    }
    response = requests.delete(url, headers=headers)
    if response.status_code == 200:
        st.success("Manga delete successfully!")
    else:
        st.error(f"Failed to delete manga. Status code: {response.status_code}, Response: {response.text}")
