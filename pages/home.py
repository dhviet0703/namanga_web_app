import streamlit as st
from PIL import Image
from settings.connect import conn


@st.cache_data(ttl=5)
def get_manga_data():
    return conn.query('SELECT * FROM public.engine_manga;')


def home_page():
    st.write("Welcome to the home page!")
    load_mangas()


def load_mangas():
    manga = get_manga_data()

    st.markdown('<div style="display: flex; flex-wrap: wrap;">', unsafe_allow_html=True)

    for row in manga.itertuples():
        name = row.name
        author = row.author
        # intro = row.introduction
        image_src = row.image

        st.markdown('<div style="display: flex; flex-direction: row;">', unsafe_allow_html=True)

        st.markdown('<div style="margin-right: 20px;">', unsafe_allow_html=True)
        try:
            image = Image.open(image_src)
            image.thumbnail((200, 200))
            st.image(image, use_column_width=False)
        except FileNotFoundError:
            st.warning("Image not found.")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div style="flex-grow: 1;">', unsafe_allow_html=True)
        st.write(f"Name: {name}")
        st.write(f"Author: {author}")
        # st.write(f"Introduction: {intro}")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
