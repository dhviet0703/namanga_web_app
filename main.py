import streamlit as st
from streamlit_cookies_manager import EncryptedCookieManager

from settings.config import cfg
from pages.home import home_page
from pages.login import login_page
from call_api.auth.login import *

cookies = EncryptedCookieManager(prefix='my_app_', password='jhasjhchasjhsa_1133_ahhsacsa')

if not cookies.ready():
    st.stop()


def main():
    st.sidebar.title("Main Menu")

    st.sidebar.image(cfg.image_path, use_column_width=True)
    if cookies.get('logged_in') == 'True' and check_login_available(cookies['token']):
        if check_permission(cookies['token']):
            menu = ["Home", "Quản lý Manga", "Quản lý User"]
            choice = st.sidebar.selectbox("Quản Lý", menu)

            if choice == "Home":
                home_page(cookies)
            elif choice == "Quản lý Manga":
                pass
            elif choice == "Quản lý User":
                pass

        if st.sidebar.button('Logout'):
            cookies['logged_in'] = 'False'
            cookies.save()
            st.experimental_rerun()

    else:
        login_page(cookies)


if __name__ == "__main__":
    main()
