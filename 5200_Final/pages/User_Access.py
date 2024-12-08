# Reworked Login Logic in 2_User_Access.py
import streamlit as st
from db_connection import init_connection
from Home import load_data, display_pdf, generate_bibtex, change, main_page
import bcrypt

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
            "SELECT UserId, UserFirstName, UserLastName, RoleId, UserPassword FROM USER_INFORMATION WHERE UserEmailAddress = %s",
            (email,),
        )
        user = cursor.fetchone()
        if user and bcrypt.checkpw(password.encode('utf-8'), user['UserPassword'].encode('utf-8')):
            return user, None
        else:
            return None, "Invalid email or password."
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

def referee():
    '''
    Referee logged in, see all proofs
    '''
    main_page("private")



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
            st._rerun()
        else:
            st.error(error or "Invalid credentials.")


# TODO: this could be where you could implement a private session
def private_session():
    user = st.session_state.get("user")
    access_level = user['RoleId']

    # IF USER IS EDITOR
    if access_level == 1:
        pass
    # if user is data entry staff
    elif access_level == 2:
        pass

    # if user is referee
    elif access_level == 3:
        referee()

    else:
        st.error("You do not have the necessary permissions to access this page.")
        st.stop()

        # Add logout button
    if st.button("Logout"):
        st.session_state["logged_in"] = False
        st.session_state["user"] = {}
        st.experimental_rerun()


# Navigation
if st.session_state["logged_in"]:
    private_session()
else:
    login_page()
