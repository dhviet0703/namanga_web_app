import streamlit as st


st.title("Hello World")
st.write("This is a sample app")
x = st.text_input("Enter a text")
if x:
    st.write(x)
