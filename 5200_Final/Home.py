import streamlit as st
import pandas as pd
from mysql.connector import Error
from db_connection import init_connection
from streamlit import session_state as ss
import base64  # forRenderingPDF

# Check if selected-file 'key' for pdf viewer already exists in session_state
# If not, then initialize it
if 'selected_file' not in ss:
    ss.selected_file = None

st.set_page_config(
    page_title="PWW Database Viewer",
    page_icon="📊",
    layout="wide"
)


# """Load data from the PUBLIC_ACCESS_VIEW"""
def load_data(connection):
    try:
        # test connection
        if connection is None:
            return None

        # load data via query
        with st.spinner('Loading data...'):
            query = "SELECT * FROM PUBLIC_ACCESS_VIEW"
            df = pd.read_sql(query, connection)

            # drop PWWEntryId column, not needed for public view
            df.drop('PWWEntryId', axis=1, inplace=True)

            # if dataframe is not empty return it
            if df is not None and not df.empty:
                df['View'] = False
                return df

            # if dataframe empty, return none
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


def display_pdf(file, width=600, height=600):
    if file is None:
        st.error("No PDF file selected")
        return
    try:
        with open(file, "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    except FileNotFoundError:
        st.error(f"No Current PDF to show for this proof.")
    except IOError:
        st.error("Error reading the PDF file")
    except Exception as err:
        st.error(f"An unexpected error occurred: {err}")
    else:
        pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" width={width} height={height} type="application/pdf">'
        st.markdown(pdf_display, unsafe_allow_html=True)


def change(df):
    """A callback from data editor."""
    delta = ss.pdf

    # Save the index that has true value on the View column.
    # 'edited_rows': {0: {'View': False}, 1: {'View': True}}
    true_index = []
    for k, v in delta['edited_rows'].items():
        for k1, v1 in v.items():
            if k1 == 'View' and v1:
                true_index.append(k)

    # Save the pdf file based on the index.
    # If there are more than 1 true index, set the selected to None to
    # not display any pdf.
    if not true_index or len(true_index) > 1:
        ss.selected_file = None
        return

    ss.selected_file = f"./static/pdf/{df.loc[true_index[0], 'ProofPdf']}"

def generate_bibtex(entry):
    """
    Generate a BibTeX entry string for the selected proof.
    """
    bibtex = f"""@article{{PWW_{entry['CitationDOI'] or entry['PWWTitle'][:10].replace(' ', '_')},
  author = {{{entry['Authors']}}},
  title = {{{entry['PWWTitle']}}},
  year = {{{entry['CitationYear']}}},
  journal = {{{entry['CitationMediaType']}}},
  pages = {{{entry['CitationPageStart']}-{entry['CitationPageEnd']}}},
  doi = {{{entry['CitationDOI']}}},
  url = {{{entry['PWWSourceUrl']}}}
}}"""
    return bibtex


def change(df):
    """A callback from data editor."""
    delta = ss.pdf

    # Save the index that has true value on the View column.
    true_index = []
    for k, v in delta['edited_rows'].items():
        for k1, v1 in v.items():
            if k1 == 'View' and v1:
                true_index.append(k)

    # If there are more than 1 true index, set the selected to None
    # to not display any pdf or allow BibTeX export.
    if not true_index or len(true_index) > 1:
        ss.selected_file = None
        ss.selected_bibtex_entry = None
        return

    selected_row = df.iloc[true_index[0]]
    ss.selected_file = f"./static/pdf/{selected_row['ProofPdf']}"
    ss.selected_bibtex_entry = selected_row.to_dict()



def main():
    # Set page config

    try:
        # Initialize connection
        conn = init_connection()

        if conn:
            # Load data
            df = load_data(conn)

            st.title("Proofs Without Words: MAA Public Database")

            # Display data with search and filtering
            if df is not None:

                cols = st.columns([1, 1])

                # Dataframe on the left side.
                with cols[0]:
                    # Main title

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

                        edited_df = st.data_editor(
                            filtered_df,
                            column_order=['View', 'CitationYear', 'PWWTitle', 'Authors', 'PWWShortDescription',
                                          'PWWAdditionalNotes', 'PWWSourceUrl', 'CitationDOI', 'CitationMediaType',
                                          'CitationPageStart', "CitationPageEnd", "ProofPdf"],
                            column_config={
                                'CitationYear': st.column_config.TextColumn("Year Published", disabled=True),
                                'PWWTitle': st.column_config.TextColumn("Proof Without Words Title", disabled=True),
                                'Authors': st.column_config.TextColumn("Author(s) of PWW", disabled=True),
                                'PWWShortDescription': st.column_config.TextColumn("Short Description of PWW",
                                                                                   disabled=True),
                                'PWWAdditionalNotes': st.column_config.TextColumn("Additional Notes", disabled=True),
                                "PWWSourceUrl": st.column_config.LinkColumn("PWW Stable URL", disabled=True),
                                "CitationDOI": st.column_config.TextColumn("PWW DOI", disabled=True),
                                "CitationMediaType": st.column_config.TextColumn("Media Type", disabled=True),
                                "CitationPageStart": st.column_config.TextColumn("Citation Page Start", disabled=True),
                                "CitationPageEnd": st.column_config.TextColumn("Citation Page End", disabled=True),
                                # "PWWTaggedTopics": st.column_config.TextColumn("Tagged Topics", disabled=True),
                                "ProofPdf": None
                            },
                            use_container_width=True,
                            hide_index=True,
                            key='pdf',
                            on_change=change,
                            args=(df,)
                        )

                        # Add export functionality
                        if st.button("Export to CSV"):
                            csv = df.to_csv(index=False)
                            st.download_button(
                                label="Download CSV",
                                data=csv,
                                file_name="pww_data.csv",
                                mime="text/csv"
                            )

                    # pdf view on the right side
                    with cols[1]:
                        if ss.selected_file:
                            display_pdf(ss.selected_file, width=700, height=700)
                            if ss.selected_bibtex_entry:
                                if st.button("Export to BibTeX"):
                                    bibtex = generate_bibtex(ss.selected_bibtex_entry)
                                    st.download_button(
                                        label="Download BibTeX",
                                        data=bibtex,
                                        file_name="proof.bib",
                                        mime="text/plain"
                                    )
                        else:
                            st.info('Check a single checkbox under the View column on the dataframe in the left side.')
            # Close connection
            conn.close()

    except Exception as e:
        st.error(f"Application error: {e}")
        st.info("Please check your database connection settings and try again.")




if __name__ == "__main__":
    main()
