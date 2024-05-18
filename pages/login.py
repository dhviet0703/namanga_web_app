import streamlit as st

from settings.config import cfg
from call_api.auth import login
from call_api.auth.register import signup, verify


def login_page(cookies):
    col1, col2 = st.columns([1, 2])

    with col1:
        st.image(cfg.image_path, use_column_width=True)

    with col2:
        st.title("Ứng dụng đăng nhập")

        menu = ["Đăng nhập", "Đăng ký"]
        choice = st.sidebar.selectbox("Menu", menu)

        if choice == "Đăng nhập":
            st.subheader("Đăng nhập")
            email = st.text_input("Email")
            password = st.text_input("Mật khẩu", type="password")
            if st.button("Đăng nhập"):
                result_login = login(email, password)
                if result_login.status_code == 200:
                    response = result_login.json()
                    token = response['access']
                    refresh_token = response['refresh']
                    cookies['token'] = token
                    cookies['refresh_token'] = refresh_token
                    cookies['logged_in'] = 'True'
                    cookies.save()
                    st.experimental_rerun()
                else:
                    st.error("Invalid email or password!")

        elif choice == "Đăng ký":
            st.subheader("Đăng ký")
            username = st.text_input("Username")
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            re_password = st.text_input("Re Password", type="password")
            if st.button("Đăng ký"):
                if password != re_password:
                    st.error("Passwords do not match!")
                else:
                    result_register = signup(username, email, password, re_password)
                    if result_register.status_code == 200:
                        cookies['email_for_verification'] = email  # Store email to cookie
                        st.success("Please check your mail for the verification code.")
                        cookies['verification_pending'] = 'True'
                        cookies.save()
                    else:
                        st.error("Failed to register. Please check the input.")

            if cookies.get('verification_pending') == 'True':
                verify_code = st.text_input("Enter the verification code")
                if st.button("Verify"):
                    result_verification = verify(cookies.get('email_for_verification'), verify_code)
                    if result_verification.status_code == 200:
                        st.success("Account successfully verified!")
                        cookies['verification_pending'] = 'False'  # Cleanup cookie state
                        del cookies['email_for_verification']
                        cookies.save()
                    else:
                        st.error("Invalid or expired verification code.")
