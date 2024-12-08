import streamlit as st
import pandas as pd
from mysql.connector import Error
from db_connection import init_connection
from streamlit import session_state as ss
import base64  # For rendering PDFs
from datetime import datetime

# Initialize session state variables
if 'selected_file' not in ss:
    ss.selected_file = None

if 'selected_bibtex_entry' not in ss:
    ss.selected_bibtex_entry = None

st.set_page_config(
    page_title="PWW Database Viewer",
    page_icon="📊",
    layout="wide"
)

# Load data from the PUBLIC_ACCESS_VIEW
def load_data(connection, state='public'):
    try:
        if connection is None:
            return None

        with st.spinner('Loading data...'):
            if state == 'private':
                query = "SELECT * FROM PRIVATE_ACCESS_VIEW"
            else:
                query = "SELECT * FROM PUBLIC_ACCESS_VIEW"
            df = pd.read_sql(query, connection)

            # Drop PWWEntryId column, not needed for public view
            df.drop('PWWEntryId', axis=1, inplace=True)

            # Add View column for user interaction
            if df is not None and not df.empty:
                df['View'] = False
                return df

            st.warning("No data found in the view.")
            return None
    except Error as e:
        st.error(f"Error loading data: {e}")
        return None
    except Exception as e:
        st.error(f"Unexpected error: {e}")
        return None


# Render a PDF file in the app
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
        pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width={width} height={height} type="application/pdf">'
        st.markdown(pdf_display, unsafe_allow_html=True)


# Generate BibTeX entry for the selected proof
def generate_bibtex(entry):
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


# Callback for data editor changes
def change(df):
    delta = ss.pdf

    # Save the index that has true value on the View column.
    true_index = []
    for k, v in delta['edited_rows'].items():
        for k1, v1 in v.items():
            if k1 == 'View' and v1:
                true_index.append(k)

    # Handle single-selection requirement for PDF and BibTeX
    if not true_index or len(true_index) > 1:
        ss.selected_file = None
        ss.selected_bibtex_entry = None
        return

    selected_row = df.iloc[true_index[0]]
    ss.selected_file = f"./static/pdf/{selected_row['ProofPdf']}"
    ss.selected_bibtex_entry = selected_row.to_dict()


def main():
    try:
        # Initialize connection
        conn = init_connection()

        if conn:
            # Load data
            df = load_data(conn, 'public')
            st.title("Proofs Without Words: MAA Public Database")

            if df is not None:
                cols = st.columns([1, 1])

                # Dataframe display with filtering and search
                with cols[0]:
                    st.subheader("Proof Without Words Database Explorer")

                    # Topics filter
                    all_tags = df["TOPICS"].tolist()
                    selected_topics = st.multiselect("Filter by Topic:", options=all_tags)

                    # Theorems filter
                    all_theorems = df["THEOREMS"].tolist()
                    selected_theorems = st.multiselect("Filter by Theorem:", options=all_theorems)

                    # MSC Code filter
                    all_msc = df["PRIMARY_MSC_CODE"].unique().tolist() + df["SECONDARY_MSC_CODE"].unique().tolist()
                    selected_msc = st.multiselect("Filter by MSC Code:", options=all_msc)

                    # Search functionality
                    search_term = st.text_input("Search in any column:", "")

                    # Year filter
                    min_year = int(df["CitationYear"].min())
                    max_year = int(df["CitationYear"].max())
                    selected_years = st.slider("Years:", min_year, max_year, (min_year, max_year))

                    # Start filtering
                    filtered_df = df.copy()

                    if search_term.strip():
                        mask = filtered_df.astype(str).apply(
                            lambda x: x.str.contains(search_term, case=False, na=False)
                        ).any(axis=1)
                        filtered_df = filtered_df[mask]

                    if selected_topics:
                        filtered_df = filtered_df[filtered_df["TOPICS"].isin(selected_topics)]

                    if selected_theorems:
                        filtered_df = filtered_df[filtered_df["THEOREMS"].isin(selected_theorems)]

                    if selected_msc:
                        filtered_df = filtered_df[
                            filtered_df["PRIMARY_MSC_CODE"].isin(selected_msc) |
                            filtered_df["SECONDARY_MSC_CODE"].isin(selected_msc)
                        ]

                    filtered_df = filtered_df[filtered_df["CitationYear"].between(selected_years[0], selected_years[1])]

                    st.write(f"Showing {len(filtered_df)} records")
                    st.data_editor(
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
                            "ProofPdf": None
                        },
                        use_container_width=True,
                        hide_index=True,
                        key='pdf',
                        on_change=change,
                        args=(df,)
                    )

                    # Export CSV functionality
                    if st.button("Export to CSV"):
                        csv = df.to_csv(index=False)
                        st.download_button(
                            label="Download CSV",
                            data=csv,
                            file_name="pww_data.csv",
                            mime="text/csv"
                        )

                # PDF and BibTeX display
                with cols[1]:
                    if ss.selected_file:
                        display_pdf(ss.selected_file, width=700, height=700)

                        if ss.selected_bibtex_entry:
                            title = ss.selected_bibtex_entry['PWWTitle'].replace(" ", "_").replace("/", "_")
                            author = ss.selected_bibtex_entry['Authors'].split(",")[0].replace(" ", "_")
                            filename = f"{title}_{author}.bib"

                            if st.button("Export to BibTeX"):
                                bibtex = generate_bibtex(ss.selected_bibtex_entry)
                                st.download_button(
                                    label="Download BibTeX",
                                    data=bibtex,
                                    file_name=filename,
                                    mime="text/plain"
                                )
                    else:
                        st.info('Check a single checkbox under the View column on the dataframe in the left side.')

            conn.close()

    except Exception as e:
        st.error(f"Application error: {e}")
        st.info("Please check your database connection settings and try again.")


if __name__ == "__main__":
    main()
