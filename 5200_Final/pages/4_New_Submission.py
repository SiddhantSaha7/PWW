import streamlit as st
from datetime import datetime
from insert_table_scripts import insert_pwwEntry, insert_author, insert_keywords, insert_topics, insert_theorems, insert_cited_works, insert_author_pww_intersection, insert_cited_works_pww_intersection, insert_keyword_pww_intersection, insert_msc_code_pww_intersection, insert_theorem_pww_intersection, insert_topic_pww_intersection, insert_journal, insert_book
from db_connection import init_connection
st.title("Create New Proof Without Word")

def main():
    #for the main PWW Table
    title = st.text_input("Enter Name of the PWW Article", key="title")
    shortDescription = st.text_input("Article Short Description", key="shortDescription") 
    additionalNotes = st.text_input("Article Additional Notes", key="notes")
    publishStatus = 'NeedsReview'
    citationPageStart = st.text_input("Citation Starting Page, leave blank if not published yet", key="citPageStart") 
    citationPageEnd = st.text_input("Citation End Page, leave blank if not published yet", key="citPageEnd") 
    citationDOI = st.text_input("Citation DOI, leave blank if not published yet") 
    years = ['']
    years.extend(list(range(1970, datetime.now().year + 1)))
    citationYear = st.selectbox('Citation year, select None if not published yet', years, key="citYear") 
    sourceUrl = st.text_input("Source URL for the PWW article, leave blank if no URL", key="url")
    graphicRightsHolder = st.text_input("Graphic rights holder for the PWW article, leave blank if unknown", key="graphicRightsHolder")
    #proofGraphic = st.file_uploader("Upload image/pdf of the proof")
    # this will be changed
    proofPdf = 'pdf1213r41523'
    citationMediaType = st.selectbox('Select the media type where the article was published, leave blank if not published yet', ('', 'Book', 'Journal'), key="media") 

    if citationMediaType == "Book":
        bookAuthor = st.text_input("Enter the book author name", key="bookAuthor")
        bookTitle = st.text_input("Enter the book title", key="bookTitle")
        bookSeries = st.text_input("Enter the book series, leave blank if not known", key="bookSeries")
        bookIsbn = st.text_input("Enter the book ISBN", key="bookIsbn")
    elif citationMediaType == "Journal":
        journalTitle = st.text_input("Enter the journal title", key="journalTitle")
        journalVolume = st.text_input("Enter the journal volume", key="journalVolume")
        journalNumber = st.text_input("Enter the journal number, leave blank if not known", key="journalNumber")
        journalMonth = st.text_input("Enter the journal month of publishing as 2 digit number", key="journalMonth")
    
    #for the author table
    authors = st.text_input("Proof Authors (Format: lastname1, firstname1; lastname2, firstname2;...", key="authors").strip().split(';')[:-1]

    #for the msc code table
    primaryMscCodes = st.text_input("Primary MSC codes associated with this proof, no more than 2 MscCodes (Format: MscCode1; MscCode2)", key="mscPrimary").strip().split(';')[:-1]
    secondaryMscCodes = st.text_input("Secondary MSC codes associated with this proof(Format: MscCode1; MscCode2...)", key="mscSecondary").strip().split(';')[:-1]

    #for the keywords table
    keywords = st.text_input("Enter the keywords associated with this proof, (Format: keyword1; keyword2;...)", key="keywords").strip().split(';')[:-1]

    #for the topics table
    topics = st.text_input("Enter the topics associated with this proof, (Format: topic1; topic2;...)", key="topics").strip().split(';')[:-1]

    #for the theorems table
    theorems = st.text_input("Enter the theorems associated with this proof, (Format: theorem1; theorem2;...)", key="theorems").strip().split(';')[:-1]

    #for the cited works table
    citedWorks = st.text_input("Enter the cited works for this proof(Format: citedWork1; citedWork2; ...) ", key="citations").strip().split(';')[:-1]

    # Initialize session state for tracking the submit button and success state
    if "submit_successful" not in st.session_state:
        st.session_state.submit_successful = False
    if "submitted" not in st.session_state:
        st.session_state.submitted = False
    

    if st.button("Submit"):
        st.session_state.submitted = True
        # A connection is opened here to ensure atomicity.
        # It ensures that if insert fails on any 1 table, inserts do not happen on any table and the transaction is rolled back.
        # For eg, if author insert fails, then insert on PWWEntry table, topic table etc will also not happen
        conn = init_connection()
        if conn is None:
            st.write("Unable to connect to the database!")
            return None
        else:
            try:
                #insert into the main PWW ENTRY Table
                pwwEntryId = insert_pwwEntry(conn, title, shortDescription, additionalNotes, publishStatus , citationPageStart, citationPageEnd, citationMediaType, citationDOI, citationYear, sourceUrl, graphicRightsHolder, proofPdf)

                #insert into the author table and pww_author intersection table
                for author in authors:
                    authorLastName, authorFirstName = author.strip().split(',')
                    authorId = insert_author(conn, authorFirstName.strip(), authorLastName.strip())
                    insert_author_pww_intersection(conn, pwwEntryId, authorId)                
                    
                # insert into the book/journal tables
                if citationMediaType == "Book":
                    insert_book(conn, pwwEntryId, bookAuthor, bookTitle, bookSeries, bookIsbn)
                elif citationMediaType == "Journal":
                    insert_journal(conn, pwwEntryId, journalTitle, journalVolume, journalNumber, journalMonth)

                #insert into the keyword table and the pww_keyword intersection table
                for keyword in keywords:
                    keywordId = insert_keywords(conn, keyword)
                    insert_keyword_pww_intersection(conn, pwwEntryId, keywordId)    

                #insert into the topic table and the pww_topic intersection table
                for topic in topics:
                    topicId = insert_topics(conn, topic)
                    insert_topic_pww_intersection(conn, pwwEntryId, topicId)
                
                #insert into the theorem table and the pww_theorem intersection table
                for theorem in theorems:
                    theoremId = insert_theorems(conn, theorem)
                    insert_theorem_pww_intersection(conn, pwwEntryId, theoremId)
                
                #insert into the cited works table and the citedWorks_pww intersection table
                for citedWork in citedWorks:
                    citationId = insert_cited_works(conn, citedWork)
                    insert_cited_works_pww_intersection(conn, pwwEntryId, citationId)

                #insert the primary MSC code in the msc_pww intersction table
                if len(primaryMscCodes) >2:
                    raise Exception("You are not allowed to enter more than 2 primary MSC!")
                else:
                    for primaryMscCode in primaryMscCodes:
                        insert_msc_code_pww_intersection(conn, pwwEntryId, primaryMscCode, 1)
                
                #insert the primary MSC code in the msc_pww intersction table
                for secondaryMscCode in secondaryMscCodes:
                        insert_msc_code_pww_intersection(conn, pwwEntryId, secondaryMscCode, 0)

                
                conn.commit()
                st.session_state.submit_successful = True
                    
            except Exception as e:
                conn.rollback()
                st.session_state.submit_successful = False
                st.error(f"Error: {e}")
            
            finally:
                conn.close()

    if st.session_state.submit_successful and st.session_state.submitted:
        st.success("Your PWW Article is submitted successully!")
        st.session_state.submit_successful = False
        st.session_state.submitted = False
        #this is not working as expected, session reset still needs to be checked
        st.session_state.clear()

        for key in st.session_state.keys():
            del st.session_state[key]
    elif not st.session_state.submit_successful and st.session_state.submitted:
        st.error("There was an issue with submission, please check the errors")


if __name__ == "__main__":
    main()

# toDo: Session reset + pdf upload
        