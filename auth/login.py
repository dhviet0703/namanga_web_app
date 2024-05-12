from db.connect import conn

import streamlit as st
import psycopg2
from passlib.hash import bcrypt


# Định nghĩa chức năng đăng nhập
def login(email, password):
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE email = %s", (email,))
    user = cursor.fetchone()
    cursor.close()
    if user and bcrypt.verify(password, user[0]):  # So sánh mật khẩu đã băm với mật khẩu người dùng cung cấp
        return True
    else:
        return False
