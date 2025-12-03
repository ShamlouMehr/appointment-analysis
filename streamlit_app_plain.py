import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from PIL import Image


st.set_page_config(page_title="NCH Ambulatory Dashboard", layout="wide")


@st.cache_data
def load_data():
    df = pd.read_csv("NCH_ambulatory_appointments.csv")

    # --- wait_days ---
    df["appointment_date"] = pd.to_datetime(df["appointment_date"])
    df["scheduled_date"] = pd.to_datetime(df["scheduled_date"])
    df["wait_days"] = (df["appointment_date"] - df["scheduled_date"]).dt.days
    # ---------------------------

    # Define flags
    df["within_14"] = df["wait_days"] <= 14
    df["no_show_flag"] = df["status"] == "No-show"
    df["cancel_flag"] = df["status"].isin(
        ["Cancelled by Patient", "Cancelled by Clinic"]
    )

    # Build summary table
    summary = df.groupby("specialty").agg(
        total_appointments=("specialty", "count"),
        avg_wait_days=("wait_days", "mean"),
        median_wait_days=("wait_days", "median"),
        pct_within_14=("within_14", "mean"),
        pct_no_show=("no_show_flag", "mean"),
        pct_cancelled=("cancel_flag", "mean")
    ).reset_index()

    summary[["pct_within_14", "pct_no_show", "pct_cancelled"]] *= 100
    return df, summary

df, summary_table = load_data()


#Layout

st.set_page_config(page_title="NCH Ambulatory Dashboard", layout="wide")

st.title("Nationwide Children’s Hospital — Ambulatory Access Dashboard")
st.write("This dashboard analyzes access to care, wait times, and scheduling outcomes for ambulatory clinics.")

# Sidebar Navigation
# st.sidebar.image(logo, width=250)

page = st.sidebar.radio(
    "Navigate",
    ["Access Goal (14 Days)", "Wait Time Distribution", "Specialty Metrics Table"]
)


# Page 1 — % Seen Within 14 Days

if page == "Access Goal (14 Days)":
    st.header("Percent of Patients Seen Within 14 Days")

    chart_data = summary_table.sort_values("pct_within_14", ascending=False)

    fig = px.bar(
        chart_data,
        x="specialty",
        y="pct_within_14",
        color="specialty",
        title="Percent of Patients Seen Within 14 Days by Specialty"
    )

    fig.add_hline(
        y=85,
        line_dash="dash",
        line_color="red",
        annotation_text="85% Target",
        annotation_position="top left"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.write("""
    **Interpretation**  
    - Specialties below the **85% target** require access-improvement strategies.  
    - This metric directly reflects NCH’s organizational goal:  
      > *“85% of patients should access care within two weeks.”*
    """)


# Page 2 — Wait Time Distribution

elif page == "Wait Time Distribution":
    st.header(" Wait Time Distribution by Specialty")

    fig = px.box(
        df,
        x="specialty",
        y="wait_days",
        color="specialty",
        title="Wait Time Distribution by Specialty"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.write("""
    **What this shows:**  
    - High medians or long tails indicate access bottlenecks.  
    - Useful for identifying *which clinics have unstable scheduling patterns*.  
    """)


# Page 3 — Specialty Metrics Table

elif page == "Specialty Metrics Table":
    st.header("Specialty Access Metrics Table")

    st.dataframe(summary_table.style.format({
        "avg_wait_days": "{:.1f}",
        "median_wait_days": "{:.1f}",
        "pct_within_14": "{:.1f}%",
        "pct_no_show": "{:.1f}%",
        "pct_cancelled": "{:.1f}%"
    }), use_container_width=True)

    st.write("""
    **Metrics Explained:**  
    - **Avg/Median Wait Days:** Access performance.  
    - **% Within 14 Days:** Alignment with the hospital’s 85% goal.  
    - **No-show %:** Impacts capacity and scheduling.  
    - **Cancellation %:** Indicates operational or communication issues.  
    """)
