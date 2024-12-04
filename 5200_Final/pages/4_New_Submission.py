import streamlit as st
import mysql.connector
from mysql.connector import Error
import pandas as pd
from db_connection import init_connection
from datetime import datetime

st.title("Create New Proof Without Word")

def insert_pwwEntry(conn, PWWTitle, PWWShortDescription, PWWAdditionalNotes, PublishStatus, 
    CitationPageStart, CitationPageEnd, CitationMediaType, CitationDOI, CitationYear, PWWSourceUrl,  
    PWWGraphicRightsHolder, ProofPdf):
    conn = init_connection()
    try:
        if conn is None:
            return "Unable to connect to the database!"
        c = conn.cursor()
        c.execute("insert into PWW_ENTRY(PWWTitle, PWWShortDescription, PublishStatus, PWWAdditionalNotes, CitationMediaType, \
                CitationPageStart, CitationPageEnd, CitationDOI, CitationYear, PWWSourceUrl, PWWGraphicRightsHolder, ProofPdf) \
                values (?,?,?,?,?,?,?,?,?,?,?,?)", 
                (PWWTitle, PWWShortDescription, PWWAdditionalNotes, PublishStatus, 
                CitationPageStart, CitationPageEnd, CitationMediaType, CitationDOI, CitationYear, PWWSourceUrl,  
                PWWGraphicRightsHolder, ProofPdf))
        c.commit()
        pwwEntryId = c.lastrowid
        c.close()
        return pwwEntryId
    except Exception as e:
        st.error("Error in inserting a new PWW article")

def insert_author(conn, AuthorFirstName, AuthorLastName):
    conn = init_connection()
    try: 
        if conn is None:
            return "Unable to connect to the database!"
        c = conn.cursor()
        c.execute("insert into PWW_AUTHOR(AuthorFirstName, AuthorLastName) values (?,?)", (AuthorFirstName, AuthorLastName))
        c.commit()
        authorId = c.lastrowid
        c.close()
        return authorId
    except Exception as e:
        st.error("Error in inserting in the author details")
    

def insert_msc(MSC2020Code, MathematicalField):
    conn = init_connection()
    try:
        if conn is None:
            return "Unable to connect to the database!"
        c = conn.cursor()
        c.execute("insert into MSC_2020_TAGS (MSC2020Code, MathematicalField) values (?,?)", (MSC2020Code, MathematicalField))
        c.commit()
        MSC2020CodeId = c.lastrowid
        c.close()
        return MSC2020CodeId
    except Exception as e:
        st.error("Error in inserting in the MSC code tags")


def insert_theorems(Theorem):
    conn = init_connection()
    try:
        if conn is None:
            return "Unable to connect to the database!"
        c = conn.cursor()
        c.execute("insert into THEOREM_TAGS (Theorem) values (?)", (Theorem))
        c.commit()
        TheoremId = c.lastrowid
        c.close()
        return TheoremId
    except Exception as e:
        st.error("Error in inserting the theorems")    

#def insert_keywords():

def insert_topics(TopicName):
    conn = init_connection()
    try:
        if conn is None:
            return "Unable to connect to the database!"
        c = conn.cursor()
        c.execute("insert into TOPIC_TAGS (TopicName) values (?)", (TopicName))
        c.commit()
        TopicId = c.lastrowid
        c.close()
        return TopicId
    except Exception as e:
        st.error("Error in inserting the topics")
# def insert_cited_works():

# def insert_pwwEntryCreator():


def main():
    st.header("Enter the details for the Proof without Words article")
    PWWTitle = st.text_input("Article Title")
    PWWShortDescription = st.text_input("Article Short Description") 
    PWWAdditionalNotes = st.text_input("Article Additional Notes") 
    PublishStatus = 'NeedsReview'
    CitationPageStart = st.text_input("Citation Starting Page") 
    CitationPageEnd = st.text_input("Citation End Page") 
    CitationMediaType = st.selectbox('Select the media type where the article was published', ('Book', 'Journal')) 
    CitationDOI = st.text_input("Citation DOI") 
    CitationYear = st.selectbox('Citation year', list(range(1970, datetime.now().year + 1))) 
    PWWSourceUrl = st.text_input("Source URL for the PWW article")
    PWWGraphicRightsHolder = st.text_input("Graphic rights holder for the PWW article")
    if st.button("Submit"):
        pwwEntryId = insert_pwwEntry(PWWTitle, PWWShortDescription, PWWAdditionalNotes, PublishStatus, CitationPageStart,
                                     CitationPageEnd, CitationDOI, CitationYear, PWWSourceUrl, PWWGraphicRightsHolder)
                
        
if __name__ == "__main__":
    main()
        
    
# Need to check for data constraint
# Need to ensure no duplicates, check if data already exists
# Need to handle entries like author for eg which will have multiple values with stream editing
