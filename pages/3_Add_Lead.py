import streamlit as st
from database import get_connection

st.title("➕ Add New Lead")

name = st.text_input("Name")
phone = st.text_input("Phone")
source = st.selectbox("Source", ["Instagram", "Website", "Call", "Walk-in"])

priority = st.selectbox("Priority", ["Hot 🔥", "Warm 🌤️", "Cold ❄️"])
status = st.selectbox("Status", ["New", "Contacted", "Visit Scheduled", "Negotiation", "Closed"])

assigned_to = st.text_input("Assign To")

follow_up_date = st.date_input("Follow-up Date")

if st.button("Save Lead"):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO leads (name, phone, source, status, priority, assigned_to, follow_up_date)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (name, phone, source, status, priority, assigned_to, str(follow_up_date)))

    conn.commit()
    conn.close()

    st.success("Lead added successfully!")