import streamlit as st

from settings.config import cfg
from pages.home import home_page
from call_api.auth.login import *
from pages.login import login_page
from pages.form.manga import add_new_manga, update_manga, delete_manga


def load_main(cookies):
    st.sidebar.image(cfg.image_path, use_column_width=True)
    if cookies.get('logged_in') == 'True' and check_login_available(cookies['token']):
        if check_permission(cookies['token']):
            if st.sidebar.button('Reset cache'):
                st.cache_data.clear()
                st.experimental_rerun()

            menu_admin = ["Ẩn", "Quản lý Manga", "Quản lý User"]
            choice_admin = st.sidebar.selectbox("Quản Lý", menu_admin)

            if choice_admin == "Ẩn":
                pass

            elif choice_admin == "Quản lý Manga":
                menu_manga_admin = ["Thêm manga", "Sửa manga", "Xóa manga"]

                choice_manga_admin = st.sidebar.selectbox("Quản lý Manga", menu_manga_admin)
                if choice_manga_admin == "Thêm manga":
                    add_new_manga(cookies)
                elif choice_manga_admin == "Sửa manga":
                    update_manga(cookies)
                elif choice_manga_admin == "Xóa manga":
                    delete_manga(cookies)

            elif choice_admin == "Quản lý User":
                pass

        menu = ["Home", "Thông tin cá nhân", "Logout"]
        choice = st.sidebar.selectbox("Menu", menu)
        if choice == "Home":
            home_page(cookies)
        elif choice == "Thông tin cá nhân":
            pass
        elif choice == "Logout":
            cookies['logged_in'] = 'False'
            cookies.save()
            st.experimental_rerun()
    else:
        login_page(cookies)
