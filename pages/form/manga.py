from pages.form import *


def add_new_manga(cookies):
    st.title("Add New Manga")

    with st.form("new_manga_form"):
        name = st.text_input("Name")
        author = st.text_input("Author")
        introduction = st.text_area("Introduction")
        genres = st.text_input("Genres (comma separated)")
        image_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

        if st.form_submit_button(label="Add Manga"):
            # genres_list = [genre.strip() for genre in genres.split(",")]
            add_manga_api(name, author, introduction, genres, image_file, cookies)
