import streamlit as st
from database import create_tables

st.set_page_config(page_title="PG CRM", layout="wide")

st.markdown("""
    <h1 style='margin-bottom:0;'>🏠 PG Lead Management CRM</h1>
    <p style='color:gray;'>Manage leads, follow-ups, and conversions efficiently</p>
""", unsafe_allow_html=True)

create_tables()

st.write("Use the sidebar to navigate.")
