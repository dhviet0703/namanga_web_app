import streamlit as st
from auth.register import signup


# conn = st.connection("postgresql", type="sql")
#
# df = conn.query('SELECT * FROM public.engine_user;', ttl="10m")
#
# for row in df.itertuples():
#     st.write(f"{row.email} has password :{row.password}")


st.title("Ứng dụng đăng nhập")

menu = ["Đăng ký", "Đăng nhập"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Đăng ký":
    st.subheader("Đăng ký")
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    re_password = st.text_input("Re Password", type="password")
    if st.button("Đăng ký"):
        st.write(signup(username, email, password, re_password))
        # st.success("Đăng ký thành công")

# elif choice == "Đăng nhập":
#     st.subheader("Đăng nhập")
#     email = st.text_input("Email")
#     password = st.text_input("Mật khẩu", type="password")
#     if st.button("Đăng nhập"):
#         if login(email, password):
#             st.success("Đăng nhập thành công")
#         else:
#             st.error("Email hoặc mật khẩu không chính xác")

# st.title("Hello World")
# st.write("This is a sample app")
# x = st.text_input("Enter a text")
# if x:
#     st.write(x)
#
