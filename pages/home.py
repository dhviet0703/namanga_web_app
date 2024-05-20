from pages import *


def home_page(cookies):
    load_mangas(cookies)


def load_mangas(cookies):
    manga = get_manga_data()

    query_params = st.experimental_get_query_params()
    if 'name' in query_params and 'chapter' in query_params:
        display_chapter_details(query_params['name'][0], query_params['chapter'][0], manga, cookies)
    elif 'name' in query_params:
        st.title('Chi tiết Manga')
        display_manga_details(query_params['name'][0], manga, cookies)
    else:
        st.title('Danh sách Manga')
        display_manga_info(manga, cookies)
