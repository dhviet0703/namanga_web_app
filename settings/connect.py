import streamlit as st
from sqlalchemy import create_engine

conn_str = "postgresql://postgres:123456@localhost:5432/namanga"
engine = create_engine(conn_str)
