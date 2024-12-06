import streamlit as st
from db_connection import init_connection
from datetime import date


# Insert new user into the database
def create_user(first_name, last_name, email, password, role_id, start_date, end_date):
    conn = init_connection()
    if not conn:
        return False, "Unable to connect to the database."
    try:
        cursor = conn.cursor()

        # Check if the email already exists
        cursor.execute(
            "SELECT COUNT(*) FROM USER_INFORMATION WHERE UserEmailAddress = %s", (email,)
        )
        if cursor.fetchone()[0] > 0:
            return False, "Email already exists. Please use a different email."

        # Insert the new user
        cursor.execute(
            """
            INSERT INTO USER_INFORMATION (RoleId, UserFirstName, UserLastName, UserEmailAddress, UserPassword, UserAccessStartDate, UserAccessEndDate)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """,
            (role_id, first_name, last_name, email, password, start_date, end_date),
        )
        conn.commit()
        return True, "User created successfully!"
    except Exception as e:
        return False, f"Error: {e}"
    finally:
        conn.close()


# Sign-up page
def signup_page():
    st.title("Sign Up")

    # Role options
    role_options = {
        1: "Editor",
        2: "DataEntry",
        3: "Referee",
        4: "GeneralUser"
    }

    # Default dates
    today = date.today()
    default_end_date = "2999-12-31"

    # Form for sign-up
    with st.form("signup_form"):
        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")
        email = st.text_input("Email Address")
        password = st.text_input("Password", type="password")
        role_id = st.selectbox(
            "Access Level",
            options=role_options.keys(),
            format_func=lambda x: role_options[x],
            index=3  # Default to GeneralUser (RoleId = 4)
        )
        start_date = st.date_input("Access Start Date", value=today)
        end_date = st.date_input("Access End Date", value=date.fromisoformat(default_end_date))
        submit_button = st.form_submit_button("Sign Up")

    if submit_button:
        if not (first_name and last_name and email and password):
            st.error("All fields are required.")
        else:
            success, message = create_user(
                first_name, last_name, email, password,
                role_id, start_date, end_date
            )
            if success:
                st.success(message)
            else:
                st.error(message)


# Display the sign-up page
signup_page()
