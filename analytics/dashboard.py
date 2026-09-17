import sqlite3
import pandas as pd
import streamlit as st
import plotly.express as px

DB_PATH = "storage/detections.db"

st.set_page_config(
    page_title="Road Sign Analytics",
    layout="wide"
)

st.title("🚦 Road Sign Detection Analytics")
st.write("Analytics dashboard for the Real-Time Road Sign Detection System")

# Connect to database
conn = sqlite3.connect(DB_PATH)

df = pd.read_sql_query(
    "SELECT * FROM detections ORDER BY timestamp DESC",
    conn
)

conn.close()

# Check for data
if df.empty:
    st.info("No detections recorded yet.")
    st.stop()

# Convert timestamp
df["timestamp"] = pd.to_datetime(df["timestamp"], utc=True)
df["timestamp"] = df["timestamp"].dt.tz_convert("Asia/Kolkata")

# Metrics
total_detections = len(df)
average_confidence = df["confidence"].mean()
stop_count = len(df[df["class_name"] == "stop"])

col1, col2, col3 = st.columns(3)

col1.metric("Total Detections", total_detections)
col2.metric("Average Confidence", f"{average_confidence:.2f}")
col3.metric("Stop Sign Detections", stop_count)

st.divider()

# Detection count by class
st.subheader("Detections by Sign Class")

class_counts = df["class_name"].value_counts().reset_index()
class_counts.columns = ["class_name", "count"]

fig1 = px.bar(
    class_counts,
    x="class_name",
    y="count",
    title="Number of Detections per Class"
)

st.plotly_chart(fig1, use_container_width=True)

# Detection timeline
st.subheader("Detection Timeline")

time_counts = (
    df.groupby("timestamp")
    .size()
    .reset_index(name="count")
)

fig2 = px.line(
    time_counts,
    x="timestamp",
    y="count",
    title="Detections Over Time"
)

st.plotly_chart(fig2, use_container_width=True)

# Recent detections
st.subheader("Recent Detections")

st.dataframe(
    df.head(20),
    use_container_width=True
)
