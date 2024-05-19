from pages.form import *


def add_new_manga(cookies):
    st.title("Thêm mới manga")

    with st.form("new_manga_form"):
        name = st.text_input("Name", None)
        author = st.text_input("Author", None)
        introduction = st.text_area("Introduction", None)
        genres = st.text_input("Genres (comma separated)", None)
        image_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

        if st.form_submit_button(label="Add Manga"):
            # genres_list = [genre.strip() for genre in genres.split(",")]
            add_manga_api(name, author, introduction, genres, image_file, cookies)
            # st.write(name, author, introduction, genres, image_file)


def update_manga(cookies):
    st.title("Cập nhật Manga")

    with st.form("update_manga_form"):
        id_manga = st.text_input("ID Manga")
        name = st.text_input("Name", None)
        author = st.text_input("Author", None)
        introduction = st.text_area("Introduction", None)
        genres = st.text_input("Genres (comma separated)", None)
        image_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

        if st.form_submit_button(label="Update Manga"):
            update_manga_api(id_manga, name, author, introduction, genres, image_file, cookies)


def delete_manga(cookies):
    st.title("Xóa Manga")

    if 'confirm_delete' not in st.session_state:
        st.session_state.confirm_delete = False
        st.session_state.id_manga_to_delete = None

    with st.form("delete_manga_form"):
        id_manga = st.text_input("ID Manga", None)
        submit_button = st.form_submit_button(label="Delete Manga")

        if submit_button:
            if not id_manga:
                st.error("Vui lòng điền vào ô ID Manga")
            else:
                st.session_state.confirm_delete = True
                st.session_state.id_manga_to_delete = id_manga

    if st.session_state.confirm_delete:
        st.warning(f"Bạn có chắc chắn muốn xóa manga với ID: {st.session_state.id_manga_to_delete}?")
        confirm_button = st.button("Có")
        cancel_button = st.button("Không")

        if confirm_button:
            delete_manga_api(st.session_state.id_manga_to_delete, cookies)
            st.session_state.confirm_delete = False  # Reset trạng thái sau khi xóa
        elif cancel_button:
            st.info("Hành động xóa đã bị hủy")
            st.session_state.confirm_delete = False  # Reset trạng thái khi hủy



