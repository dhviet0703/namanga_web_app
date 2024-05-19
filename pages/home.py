from pages import *


def home_page(cookies):
    st.write("Welcome to the home page!")
    if st.button('Reset Page'):
        st.cache_data.clear()
        st.experimental_rerun()
    load_mangas(cookies)


def load_mangas(cookies):
    manga = get_manga_data()

    st.markdown('<div style="display: flex; flex-wrap: wrap;">', unsafe_allow_html=True)

    for row in manga.itertuples():
        name = row.name
        author = row.author
        image_src = row.image

        st.markdown('<div style="display: flex; flex-direction: row;">', unsafe_allow_html=True)

        st.markdown('<div style="margin-right: 20px;">', unsafe_allow_html=True)
        image = Image.open(image_src)
        image.thumbnail((200, 200))
        st.image(image, use_column_width=False)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div style="flex-grow: 1;">', unsafe_allow_html=True)
        st.write(f"Name: {name}")
        st.write(f"Author: {author}")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
