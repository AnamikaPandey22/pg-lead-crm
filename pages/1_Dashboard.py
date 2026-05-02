import streamlit as st
import pandas as pd
from database import get_connection
from datetime import date

# ------------------ PAGE CONFIG ------------------
st.title("📊 Dashboard")

conn = get_connection()

# Load data safely
try:
    df = pd.read_sql("SELECT * FROM leads", conn)
except:
    df = pd.DataFrame()

today = date.today()

# ------------------ EMPTY STATE ------------------
if df.empty:
    st.info("No leads available. Please add leads to see insights 🚀")
    conn.close()
    st.stop()

# ------------------ METRICS ------------------
total_leads = len(df)
closed_leads = len(df[df["status"] == "Closed"])
conversion_rate = (closed_leads / total_leads * 100) if total_leads > 0 else 0

st.markdown("### 📊 Overview")

col1, col2, col3 = st.columns(3)
col1.metric("Total Leads", total_leads)
col2.metric("Closed Leads", closed_leads)
col3.metric("Conversion Rate (%)", f"{conversion_rate:.2f}")

st.divider()

# ------------------ DATE SAFE FUNCTIONS ------------------
def safe_date(x):
    try:
        return pd.to_datetime(x).date()
    except:
        return None

# ------------------ OVERDUE LEADS ------------------
def is_overdue(follow_date):
    d = safe_date(follow_date)
    return d is not None and d < today

overdue_leads = df[df["follow_up_date"].apply(is_overdue)]

# Sort by oldest first (important)
overdue_leads = overdue_leads.copy()
if not overdue_leads.empty:
    overdue_leads["parsed_date"] = overdue_leads["follow_up_date"].apply(safe_date)
    overdue_leads = overdue_leads.sort_values(by="parsed_date")

st.markdown("### 🚨 Attention Needed")

if not overdue_leads.empty:
    st.dataframe(
        overdue_leads[["name", "phone", "follow_up_date", "assigned_to"]],
        use_container_width=True
    )
else:
    st.success("No overdue leads 🎉")

st.divider()

# ------------------ PIPELINE INSIGHTS ------------------
st.markdown("### 📈 Pipeline Insights")

status_counts = df["status"].value_counts()
st.bar_chart(status_counts)

st.divider()

# ------------------ UPCOMING FOLLOW-UPS ------------------
def is_upcoming(follow_date):
    d = safe_date(follow_date)
    return d is not None and d >= today

upcoming_followups = df[df["follow_up_date"].apply(is_upcoming)]

# Sort upcoming by nearest date
upcoming_followups = upcoming_followups.copy()
if not upcoming_followups.empty:
    upcoming_followups["parsed_date"] = upcoming_followups["follow_up_date"].apply(safe_date)
    upcoming_followups = upcoming_followups.sort_values(by="parsed_date")

st.markdown("### 📅 Follow-up Tracker")

if not upcoming_followups.empty:
    st.dataframe(
        upcoming_followups[["name", "phone", "follow_up_date", "status"]],
        use_container_width=True
    )
else:
    st.info("No upcoming follow-ups")

conn.close()