# Reworked Login Logic in 2_User_Access.py
import streamlit as st
from db_connection import init_connection

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "user" not in st.session_state:
    st.session_state["user"] = {}


def authenticate_user(email, password):
    conn = init_connection()
    if not conn:
        return None, "Unable to connect to the database!"
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            """
            SELECT UserId, UserFirstName, UserLastName, RoleId
            FROM USER_INFORMATION
            WHERE UserEmailAddress=%s AND UserPassword=%s
            """,
            (email, password),
        )
        user = cursor.fetchone()
        return user, None
    except Exception as e:
        return None, str(e)
    finally:
        conn.close()


def restrict_access(required_role):
    """
    Restrict access to users with specific roles.
    - required_role: List of RoleIds allowed to access the resource.
    """
    user = st.session_state.get("user")
    if not user or user["RoleId"] not in required_role:
        st.error("You do not have permission to access this page.")
        st.stop()  # Stop further execution


# Login page
def login_page():
    st.title("Login")
    email = st.text_input("Email Address")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        user, error = authenticate_user(email, password)
        if user:
            st.session_state["logged_in"] = True
            st.session_state["user"] = user
            st.success(f"Welcome, {user['UserFirstName']}!")
        else:
            st.error(error or "Invalid credentials.")

# TODO: this could be where you could implement a private session
def private_session():
    # example implementation of restrict access, if i only want editors and data entry staff
    restrict_access([1,2,4])
    st.title("Logged In")
    user = st.session_state["user"]
    st.write(f"Hello, {user['UserFirstName']} {user['UserLastName']}!")
    if st.button("Logout"):
        st.session_state["logged_in"] = False
        st.session_state["user"] = {}


# Navigation
if st.session_state["logged_in"]:
    private_session()
else:
    login_page()
