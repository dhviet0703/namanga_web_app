from pages import *
from pages.form.chapter import *
from pages.form.manga import *


def home_page(cookies):
    menu_home = ['Manga Mới Nhất', 'Theo thể loại']
    choice_home = st.sidebar.selectbox("Menu home", menu_home)
    if choice_home == 'Manga Mới Nhất':
        load_mangas(cookies)
    elif choice_home == 'Theo thể loại':
        choice_genre = st.sidebar.selectbox("Chọn thể loại", cfg.genres)

        if st.sidebar.button(label="Tìm"):
            total_with_genre = get_manga_with_genre(choice_genre)
            load_manga_with_genre(total_with_genre, cookies)


def load_mangas(cookies):
    manga = get_manga_data()
    query_params = st.experimental_get_query_params()
    if 'name' in query_params and 'chapter' in query_params:
        display_chapter_details(query_params['name'][0], query_params['chapter'][0], manga, cookies)
    elif 'name' in query_params and 'manga_id' in query_params:
        add_new_chapter(query_params['name'][0], query_params['manga_id'][0], cookies)
    elif 'name' in query_params:
        st.title('Chi tiết Manga')
        display_manga_details(query_params['name'][0], manga, cookies)
    else:
        st.title('Danh sách Manga')
        display_manga_info(manga, cookies)


def load_manga_with_genre(manga, cookies):
    query_params = st.experimental_get_query_params()
    if 'name' in query_params and 'chapter' in query_params:
        display_chapter_details(query_params['name'][0], query_params['chapter'][0], manga, cookies)
    elif 'name' in query_params and 'manga_id' in query_params:
        add_new_chapter(query_params['name'][0], query_params['manga_id'][0], cookies)
    elif 'name' in query_params:
        st.title('Chi tiết Manga')
        display_manga_details(query_params['name'][0], manga, cookies)
    else:
        st.title('Danh sách Manga')
        display_manga_info(manga, cookies)
