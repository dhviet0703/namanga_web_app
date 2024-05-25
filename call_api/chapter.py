import requests
import streamlit as st


def add_chapter_api(manga_id, number, title, images_zip, cookies):
    url = f"http://localhost:8000/api/chapter/post/?number={number}&title={title}&manga_id={manga_id}"
    token = cookies['token']
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    files = {
        'data_chapter': (images_zip.name, images_zip, 'application/zip')
    }

    response = requests.post(url, headers=headers, files=files)

    if response.status_code == 200:
        st.success("Chapter added successfully!")
    else:
        st.error(f"Failed to add chapter. Status code: {response.status_code}, Response: {response.text}")


def update_chapter_api(id_chapter, name, number, title, genres, images_zip, cookies):
    url = "http://localhost:8000/api/chapter/put/"
    token = cookies['token']
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {token}'
    }
    data = {'chapter_id': id_chapter}
    if name:
        data['name'] = name
    if number:
        data['number'] = number
    if title:
        data['title'] = title
    if genres:
        data['genres'] = genres
    if images_zip:
        files = {'image_data': (images_zip.name, images_zip, images_zip.type)}
        response = requests.put(url, headers=headers, files=files, data=data)
    else:
        response = requests.put(url, headers=headers, data=data)

    if response.status_code == 200:
        st.success("Manga update successfully!")
    else:
        st.error(f"Failed to update chapter. Status code: {response.status_code}, Response: {response.text}")


def update_views_chapter(chapter_id, cookies):
    url = f"http://localhost:8000/api/chapter/put/?chapter_id={chapter_id}"
    token = cookies['token']
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    response = requests.put(url, headers=headers)

    if response.status_code == 200:
        st.success("Chapter updated successfully!")
    else:
        st.error(f"Failed to update chapter. Status code: {response.status_code}, Response: {response.text}")


def delete_chapter_api(id_chapter, cookies):
    url = f"http://localhost:8000/api/chapter/delete/?chapter_id={id_chapter}"
    token = cookies['token']
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {token}'
    }
    response = requests.delete(url, headers=headers)
    if response.status_code == 200:
        st.success("Manga delete successfully!")
    else:
        st.error(f"Failed to delete chapter. Status code: {response.status_code}, Response: {response.text}")