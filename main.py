import streamlit as st
from streamlit_cookies_manager import EncryptedCookieManager

from settings.config import cfg
from pages.home import home_page
from pages.login import login_page
from call_api.auth.login import *
from pages.form.manga import add_new_manga

cookies = EncryptedCookieManager(prefix='my_app_', password='jhasjhchasjhsa_1133_ahhsacsa')

if not cookies.ready():
    st.stop()


def main():
    st.sidebar.title("Main Menu")

    st.sidebar.image(cfg.image_path, use_column_width=True)
    if cookies.get('logged_in') == 'True' and check_login_available(cookies['token']):
        if check_permission(cookies['token']):
            menu_admin = ["Quản lý Manga", "Quản lý User"]
            choice_admin = st.sidebar.selectbox("Quản Lý", menu_admin)

            if choice_admin == "Quản lý Manga":
                add_new_manga(cookies)
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


if __name__ == "__main__":
    main()
