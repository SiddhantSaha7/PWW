import streamlit as st
import pandas as pd
import mysql.connector
from mysql.connector import Error
from db_connection import init_connection

def load_data(connection):
    """Load data from the PUBLIC_ACCESS_VIEW"""
    try:
        if connection is None:
            return None
            
        with st.spinner('Loading data...'):
            query = "SELECT * FROM PUBLIC_ACCESS_VIEW"
            df = pd.read_sql(query, connection)
            df.drop('PWWEntryId', axis=1, inplace= True)
            if df is not None and not df.empty:
                return df
            else:
                st.warning("No data found in the view.")
                return None
    except Error as e:
        st.error(f"Error loading data: {e}")
        st.info("Please verify that:")
        st.info("1. The XAMPP MySQL service is running")
        st.info("2. The PWW_DATABASE exists")
        st.info("3. The PUBLIC_ACCESS_VIEW exists in the database")
        return None
    except Exception as e:
        st.error(f"Unexpected error: {e}")
        return None

def display_data(df):
    """Display the data with filtering and search options"""
    st.subheader("Data View")
    
    if df is not None:
        # Add search functionality
        search_term = st.text_input("Search in any column:", "")
        
        if search_term:
            # Create a mask for searching across all columns
            mask = df.astype(str).apply(
                lambda x: x.str.contains(search_term, case=False)
            ).any(axis=1)
            filtered_df = df[mask]
        else:
            filtered_df = df
            
        # Display row count
        st.write(f"Showing {len(filtered_df)} records")
        
        # Display the dataframe with sorting enabled
        st.dataframe(
            filtered_df,
            use_container_width=True,
            hide_index=True
        )

def main():
    # Set page config
    st.set_page_config(
        page_title="PWW Database Viewer",
        page_icon="📊",
        layout="wide"
    )
    
    # Main title
    st.title("PWW Database Viewer")
    
    try:
        # Initialize connection
        conn = init_connection()
        
        if conn:
            # Load data
            df = load_data(conn)
            
            # Display data with search and filtering
            if df is not None:
                display_data(df)
                
                # Add export functionality
                if st.button("Export to CSV"):
                    csv = df.to_csv(index=False)
                    st.download_button(
                        label="Download CSV",
                        data=csv,
                        file_name="pww_data.csv",
                        mime="text/csv"
                    )
                    
            # Close connection
            conn.close()
                
    except Exception as e:
        st.error(f"Application error: {e}")
        st.info("Please check your database connection settings and try again.")

if __name__ == "__main__":
    main()