import streamlit as st
from db_connection import init_connection


# this function inserts into the db
def create_user(first_name, last_name, email, password):
    conn = init_connection()
    if not conn:
        return False, "Unable to connect to the database."
    try:
        cursor = conn.cursor()

        # first checks to make sure user doesn't already exist in db
        cursor.execute(
            "SELECT COUNT(*) FROM USER_INFORMATION WHERE UserEmailAddress = %s", (email,)
        )
        if cursor.fetchone()[0] > 0:
            return False, "Email already exists. Please use a different email."

        # inset new user
        cursor.execute(
            """
            INSERT INTO USER_INFORMATION (RoleId, UserFirstName, UserLastName, UserEmailAddress, UserPassword, UserAccessStartDate)
            VALUES (%s, %s, %s, %s, %s, CURDATE())
            """,
            (4, first_name, last_name, email, password),  # default to the gen user role
        )
        conn.commit()
        return True, "User created successfully!"
    except Exception as e:
        return False, f"Error: {e}"
    finally:
        conn.close()


# sign up page
def signup_page():
    st.title("Sign Up")

    # form to sign up 
    with st.form("signup_form"):
        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")
        email = st.text_input("Email Address")
        password = st.text_input("Password", type="password")
        submit_button = st.form_submit_button("Sign Up")

    if submit_button:
        if not (first_name and last_name and email and password):
            st.error("All fields are required.")
        else:
            success, message = create_user(first_name, last_name, email, password)
            if success:
                st.success(message)
            else:
                st.error(message)



signup_page()
