import streamlit as st
import pandas as pd
import numpy as np

# ----------------------------
# INITIAL SETUP
# ----------------------------
st.set_page_config(page_title="Dashboard", page_icon="📊", layout="wide")

# Initialize session state variables ONLY once
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

# ----------------------------
# LOGIN CHECK
# ----------------------------
if not st.session_state.logged_in:
    st.error("You must be logged in to view the dashboard.")
    if st.button("Go to login page"):
        # Adjust path depending on your structure
        st.switch_page("Home.py")
    st.stop()

# ----------------------------
# DASHBOARD CONTENT
# ----------------------------
st.title("📊 Dashboard")
st.success(f"Hello, **{st.session_state.username}**! You are logged in.")

st.caption("This is demo content — replace with your own dashboard.")

# Sidebar filters
with st.sidebar:
    st.header("Filters")
    n_points = st.slider("Number of data points", 10, 200, 50)

# Fake data
data = pd.DataFrame(
    np.random.rand(n_points, 3),
    columns=["A", "B", "C"]
)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Line chart")
    st.line_chart(data)

with col2:
    st.subheader("Bar chart")
    st.bar_chart(data)

with st.expander("See raw data"):
    st.dataframe(data)

# ----------------------------
# LOGOUT
# ----------------------------
st.divider()
if st.button("Log out"):
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.info("You have been logged out.")
    st.switch_page("Home.py")

if not st.session_state.logged_in:
    st.error("You must be logged in...")
    st.switch_page("Home.py")
    st.stop()