import streamlit as st
import mysql.connector
from mysql.connector import Error

def init_connection():
    """Initialize database connection using mysql-connector-python"""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="dev",
            database="PWW_DATABASE",
            unix_socket="/Applications/XAMPP/xamppfiles/var/mysql/mysql.sock"
        )
        return connection
    except Error as e:
        st.error(f"Error connecting to MySQL: {e}")
        return None