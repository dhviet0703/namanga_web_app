import streamlit as st
from streamlit_cookies_manager import EncryptedCookieManager

from settings.config import cfg
from pages.home import home_page
from call_api.auth.login import *
from pages.login import login_page
from pages.form.manga import add_new_manga
from pages.load_main import load_main

cookies = EncryptedCookieManager(prefix='my_app_', password='jhasjhchasjhsa_1133_ahhsacsa')

if not cookies.ready():
    st.stop()


def main():
    st.sidebar.title("Main Menu")

    load_main(cookies)


if __name__ == "__main__":
    main()
