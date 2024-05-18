import streamlit as st
from streamlit_cookies_manager import EncryptedCookieManager

from pages.home import home_page
from pages.login import login_page
from settings.config import cfg

cookies = EncryptedCookieManager(prefix='my_app_', password='jhasjhchasjhsa_1133_ahhsacsa')

if not cookies.ready():
    st.stop()


def main():
    st.sidebar.title("Main Menu")
    st.sidebar.image(cfg.image_path, use_column_width=True)
    if cookies.get('logged_in') == 'True':
        menu = ["Home", "Quản lý Manga", "Quản lý User"]
        choice = st.sidebar.selectbox("Menu", menu)

        if choice == "Home":
            home_page()
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
