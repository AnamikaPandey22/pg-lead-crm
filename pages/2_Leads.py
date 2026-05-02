import streamlit as st
import pandas as pd
from database import get_connection
from datetime import date

st.title("📋 Leads")

conn = get_connection()

# Load data
df = pd.read_sql("SELECT * FROM leads", conn)

# 🔍 SEARCH
search = st.text_input("Search by Name or Phone")

if search:
    df = df[df["name"].str.contains(search, case=False) | df["phone"].str.contains(search, case=False)]

# 🎯 FILTERS
col1, col2, col3 = st.columns(3)

with col1:
    status_filter = st.selectbox("Filter by Status", ["All"] + df["status"].dropna().unique().tolist())

with col2:
    priority_filter = st.selectbox("Filter by Priority", ["All"] + df["priority"].dropna().unique().tolist())

with col3:
    agent_filter = st.selectbox("Filter by Assigned To", ["All"] + df["assigned_to"].dropna().unique().tolist())

# Apply filters
if status_filter != "All":
    df = df[df["status"] == status_filter]

if priority_filter != "All":
    df = df[df["priority"] == priority_filter]

if agent_filter != "All":
    df = df[df["assigned_to"] == agent_filter]

# ⏰ FOLLOW-UP STATUS LOGIC
def get_followup_status(follow_date):
    if not follow_date:
        return "—"
    
    follow_date = pd.to_datetime(follow_date).date()
    today = date.today()

    if follow_date < today:
        return "🔴 Overdue"
    elif follow_date == today:
        return "🟡 Due Today"
    else:
        return "🟢 Upcoming"

df["Follow-up Status"] = df["follow_up_date"].apply(get_followup_status)

if df.empty:
    st.info("No leads found. Add some leads to get started 🚀")
else:
    st.dataframe(df, use_container_width=True)

# Display
def highlight_followup(row):
    status = row["Follow-up Status"]
    if "Overdue" in status:
        return ['background-color: #ffcccc'] * len(row)
    elif "Due Today" in status:
        return ['background-color: #fff3cd'] * len(row)
    else:
        return [''] * len(row)

styled_df = df.style.apply(highlight_followup, axis=1)

st.dataframe(styled_df, use_container_width=True)



conn.close()