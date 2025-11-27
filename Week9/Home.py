import streamlit as st

# ---------- Page Config ----------
st.set_page_config(
    page_title="Login / Register",
    page_icon="🔑",
    layout="centered"
)

# ---------- Initialise session state ----------
if "users" not in st.session_state:
    # Very simple in-memory "database": {username: password}
    st.session_state.users = {"Ali":"1234"}

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

# ---------- Title ----------
st.title("Welcome")

# If already logged in, go straight to dashboard
if st.session_state.logged_in:
    st.success(f"Already logged in as *{st.session_state.username}*.")

    if st.button("Go to dashboard"):
        st.switch_page("pages/1_Dashboard.py")

    st.stop()   # Don’t show login/register again


# ==========================================================
#                     TABS : LOGIN / REGISTER
# ==========================================================
tab_login, tab_register = st.tabs(["Login", "Register"])


# ---------------------- LOGIN TAB -------------------------
with tab_login:
    st.subheader("Login")

    login_username = st.text_input("Username", key="login_username")
    login_password = st.text_input("Password", type="password", key="login_password")

    if st.button("Log in", type="primary"):
        users = st.session_state.users

        if login_username in users and users[login_username] == login_password:
            st.session_state.logged_in = True
            st.session_state.username = login_username
            st.success(f"Welcome back, {login_username}! 🎉")

            st.switch_page("pages/1_Dashboard.py")
        else:
            st.error("Invalid username or password.")


# ---------------------- REGISTER TAB -------------------------
with tab_register:
    st.subheader("Register")

    new_username = st.text_input("Choose a username", key="register_username")
    new_password = st.text_input("Choose a password", type="password", key="register_password")
    confirm_password = st.text_input("Confirm password", type="password", key="register_confirm")

    if st.button("Create Account"):
        if new_username == "" or new_password == "" or confirm_password == "":
            st.warning("Please fill in all fields.")

        elif new_username in st.session_state.users:
            st.error("Username already exists.")

        elif new_password != confirm_password:
            st.error("Passwords do not match.")

        else:
            st.session_state.users[new_username] = new_password
            st.success("Account created successfully! You can log in now.")