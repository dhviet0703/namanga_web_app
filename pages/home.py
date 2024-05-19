from pages import *


def home_page(cookies):
    st.write("Welcome to the home page!")
    load_mangas(cookies)


def load_mangas(cookies):
    manga = get_manga_data()

    st.markdown(
        """
        <style>
        .grid-container {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            gap: 10px;  /* Giảm khoảng cách giữa các phần tử */
            padding: 10px;
        }
        .grid-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            padding: 10px;
            border-radius: 8px;  /* Tùy chọn: Bo tròn góc cạnh */
        }
        .grid-item img {
            width: 100%;
            height: auto;
            max-height: 200px;  /* Điều chỉnh chiều cao tối đa của hình ảnh */
            object-fit: cover;  /* Giúp hình ảnh vừa với khung mà không bị biến dạng */
            border-radius: 4px;  /* Tùy chọn: Bo tròn góc hình ảnh */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="grid-container">', unsafe_allow_html=True)

    for item in manga.itertuples():
        name = item.name
        image_src = item.image

        st.markdown('<div class="grid-item">', unsafe_allow_html=True)
        image = Image.open(image_src)
        image.thumbnail((200, 200))
        st.image(image, use_column_width=False)
        st.write(f"{name}")
        st.write(f"{item.id}")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
