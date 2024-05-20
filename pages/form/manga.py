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
            add_manga_api(name, author, introduction, genres, image_file, cookies)


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
            st.session_state.confirm_delete = False
        elif cancel_button:
            st.info("Hành động xóa đã bị hủy")
            st.session_state.confirm_delete = False


def display_manga_info(manga, cookies):
    for index, row in manga.iterrows():
        name = row['name']
        image = Image.open(row['image']).resize((300, 400))

        col1, col2 = st.columns([1, 2])

        with col1:
            st.image(image, use_column_width=True)

        with col2:
            st.write(f"**ID:** {row['id']}")
            st.write(f"**Tên:** {name}")
            st.write(f"**Tổng số chương:** {row['total_chapter']}")
            st.write(f"**Lượt thích:** {row['like']}")
            st.write(f"**Đánh giá:** {row['rating']}/5")
            st.write("---")
            if st.button("Show Details", key=index):
                st.experimental_set_query_params(name=name)


def display_manga_details(name, manga, cookies):
    row = manga[manga['name'] == name].iloc[0]
    image = Image.open(row['image']).resize((500, 800))
    if st.button("Back to List"):
        st.experimental_set_query_params()
    col1, col2, col3 = st.columns([1.5, 2, 3])

    with col1:
        st.image(image, use_column_width=True)

    with col2:
        st.write(f"**ID:** {row['id']}")
        st.write(f"**Tên:** {name}")
        st.write(f"**Tác giả :** {row['author']}")
        st.write(f"**Tổng số chương:** {row['total_chapter']}")
        st.write(f"**Lượt thích:** {row['like']}")
        st.write(f"**Đánh giá:** {row['rating']}/5")

    if check_permission(cookies['token']):
        with col3:
            if st.button("Sửa Manga", key=f"edit_{row['id']}"):
                pass
            if st.button("Xóa Manga", key=f"del_{row['id']}"):
                pass
            if st.button("Thêm vào Yêu thích"):
                pass
            if st.button("Thích Manga này"):
                pass
            if st.button("Chấm điểm (Tối đa 5)"):
                pass
    else:
        with col3:
            if st.button("Thêm vào Yêu thích"):
                pass
            if st.button("Thích Manga này"):
                pass
            if st.button("Chấm điểm (Tối đa 5)"):
                pass
        st.write("---")
    st.write(f"**Giới thiệu:** {row['introduction']}")

    chapter_data = get_chapter_list(row['id'])

    st.write("## Chapters")

    if check_permission(cookies['token']):
        for idx, chapter in chapter_data.iterrows():
            col1, col2, col3, col4 = st.columns([1, 2, 1, 1])
            col1.write(f"{chapter['number']}")
            col2.write(f"{chapter['title']}")
            if col3.button("Đọc", key=f"read_{idx}"):
                st.experimental_set_query_params(name=name, chapter=chapter['number'])
            col4.button("Sửa", key=f"edit_{idx}")
            col4.button("Xóa", key=f"delete_{idx}")
    else:
        for idx, chapter in chapter_data.iterrows():
            col1, col2, col3, col4 = st.columns([1, 2, 1, 1])
            col1.write(f"{chapter['number']}")
            col2.write(f"{chapter['title']}")
            if col3.button("Đọc", key=f"read_{idx}"):
                st.experimental_set_query_params(name=name, chapter=chapter['number'])


def display_chapter_details(name, chapter_number, manga, cookies):
    st.title(f"Bạn đang đọc Manga {name} chương {chapter_number}")

    row = manga[manga['name'] == name].iloc[0]
    chapter = get_chapter_list(row['id'])
    chapter = chapter[chapter['number'] == int(chapter_number)].iloc[0]

    images = get_image_chapter(chapter['id'])

    st.write(f"## {row['name']} - Chapter {chapter['number']}: {chapter['title']}")

    for idx, image in images.iterrows():
        image = Image.open(image['src'])
        st.image(image, use_column_width=True)

