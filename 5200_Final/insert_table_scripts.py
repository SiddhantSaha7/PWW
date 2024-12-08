import streamlit as st
from db_connection import init_connection

# insert in the PWW ENTRY table
def insert_pwwEntry(conn, PWWTitle, PWWShortDescription, PWWAdditionalNotes, PublishStatus, 
    CitationPageStart, CitationPageEnd, CitationMediaType, CitationDOI, CitationYear, PWWSourceUrl,  
    PWWGraphicRightsHolder, ProofPdf):
    try:
        c = conn.cursor()
        PWWShortDescription = PWWShortDescription.strip() if PWWShortDescription.strip() else None
        PWWAdditionalNotes = PWWAdditionalNotes.strip() if PWWAdditionalNotes.strip() else None
        CitationPageStart = int(CitationPageStart) if str(CitationPageStart).strip() else None
        CitationPageEnd = int(CitationPageEnd) if str(CitationPageEnd).strip() else None
        CitationMediaType = CitationMediaType.strip() if CitationMediaType.strip() else None
        CitationDOI = CitationDOI.strip() if CitationDOI and CitationDOI.strip() else None
        CitationYear = int(CitationYear) if str(CitationYear).strip() else None
        PWWSourceUrl = PWWSourceUrl.strip() if PWWSourceUrl.strip() else None
        PWWGraphicRightsHolder = PWWGraphicRightsHolder.strip() if PWWGraphicRightsHolder.strip() else None
        c.execute("""INSERT INTO PWW_ENTRY(PWWTitle, PWWShortDescription, PWWAdditionalNotes, PublishStatus, CitationPageStart, CitationPageEnd, CitationMediaType, CitationDOI, CitationYear, PWWSourceUrl, PWWGraphicRightsHolder, ProofPdf) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", 
        (PWWTitle, PWWShortDescription, PWWAdditionalNotes, PublishStatus, CitationPageStart, CitationPageEnd, CitationMediaType, CitationDOI, CitationYear, PWWSourceUrl, PWWGraphicRightsHolder, ProofPdf))
        pwwEntryId = c.lastrowid
        return pwwEntryId
    except Exception as e:
        st.error(f"Error in inserting a new PWW article: {e}")
        raise Exception(f"Insert PWW article failed: {e}")



# insert in the author table
def insert_author(conn, AuthorFirstName, AuthorLastName):
    try: 
        c = conn.cursor()
        checkQuery = """ select PWWAuthorId from PWW_AUTHOR where AuthorFirstName=%s and AuthorLastName=%s"""
        c.execute(checkQuery, AuthorFirstName, AuthorLastName)
        authorId = c.fetchone()
        if authorId:
            print("Author {AuthorFirstName} {AuthorLastName} already existed in the database hence new entry not added, existing author linked to the new PWW Article")
            authorId = authorId[0]
        else:
            c.execute("""insert into PWW_AUTHOR(AuthorFirstName, AuthorLastName) values (%s,%s)""", (AuthorFirstName, AuthorLastName))
            authorId = c.lastrowid
        return authorId
    except Exception as e:
        st.error(f"Error in inserting in the author details: {e}")
        raise Exception(f"Insert author failed: {e}")

    
#insert keywords for the article
def insert_keywords(conn, Keyword):
    try:
        if Keyword.strip()=="":
            print("No Keyword provided, skipping insertion")
            return None
        c = conn.cursor()
        checkQuery = """ select KeywordId from KEYWORD_TAGS where Keyword=%s"""
        c.execute(checkQuery, (Keyword,))
        keywordId = c.fetchone()
        if keywordId:
            print("Keyword {Keyword} already existed in the database hence new entry not added, existing keyword linked to the new PWW Article")
            keywordId = keywordId[0]
        else:
            c.execute("""insert into KEYWORD_TAGS (Keyword) values (%s)""", (Keyword,))
            keywordId = c.lastrowid
        return keywordId
    except Exception as e:
        st.error(f"Error in inserting the keywords: {e}")
        raise Exception(f"Insert keyword failed: {e}")

#insert the topics for the article
def insert_topics(conn, TopicName):
    try:
        if not TopicName or TopicName.strip()=="":
            print("No Topic provided, skipping insertion")
            return None
        c = conn.cursor()
        checkQuery = """ select TopicId from TOPIC_TAGS where TopicName=%s"""
        c.execute(checkQuery, (TopicName,))
        topicId = c.fetchone()
        if topicId:
            print("Topic {TopicName} already existed in the database hence new entry not added, existing topic linked to the new PWW Article")
            topicId = topicId[0]
        else:
            c.execute("""insert into TOPIC_TAGS (TopicName) values (%s)""", (TopicName,))
            topicId = c.lastrowid
        return topicId
    except Exception as e:
        st.error(f"Error in inserting the topics: {e}")
        raise Exception(f"Insert topics failed: {e}")

#insert the theorems for the article
def insert_theorems(conn, Theorem):
    try:
        if not Theorem or Theorem.strip()=="":
            print("No Theorem provided, skipping insertion")
            return None
        c = conn.cursor()
        checkQuery = """ select TheoremId from THEOREM_TAGS where Theorem=%s"""
        c.execute(checkQuery, (Theorem,))
        theoremId = c.fetchone()
        if theoremId:
            print("Theorem {TheoremName} already existed in the database hence new entry not added, existing theorem linked to the new PWW Article")
            theoremId = theoremId[0]
        else:
            c.execute("""insert into THEOREM_TAGS (Theorem) values (%s)""", (Theorem,))   
            theoremId = c.lastrowid
        return theoremId
    except Exception as e:
        st.error(f"Error in inserting the theorems: {e}")    
        raise Exception(f"Insert theorem failed: {e}")

#insert citation for the article
def insert_cited_works(conn, givenCitation):
    try:
        if not givenCitation or givenCitation.strip()=="":
            print("No citations provided, skipping insertion")
            return None
        c = conn.cursor()
        checkQuery = """ select PWWCitedWorkCitationID from CITED_WORKS where GivenCitation=%s"""
        c.execute(checkQuery, (givenCitation,))
        citationId = c.fetchone()
        if citationId:
            print("Citation {givenCitation} already existed in the database hence new entry not added, existing theorem linked to the new PWW Article")
            citationId = citationId[0]
        else:
            c.execute("""insert into CITED_WORKS (GivenCitation) values (%s)""", (givenCitation,))  
            citationId = c.lastrowid
        return citationId
    except Exception as e:
        st.error(f"Error in inserting the cited works: {e}")
        raise Exception(f"Insert citations failed: {e}")

#insert book table
def insert_book(conn, pwwEntryId, bookAuthor, bookTitle, bookSeries, ISBN):
    try:
        if not bookSeries or bookSeries.strip()=="":
            bookSeries = None
        c = conn.cursor()
        c.execute("""insert into BOOK_CITATION (PWWEntryId, BookAuthor, BookTitle, BookSeries, ISBN)values (%s,%s,%s,%s,%s)""", (pwwEntryId, bookAuthor, bookTitle, bookSeries, ISBN))
    except Exception as e:
        st.error(f"Error in inserting in book table: {e}")
        raise Exception(f"Insert book failed: {e}")

#insert journal table
def insert_journal(conn, pwwEntryId, journalTitle, journalVolume, journalNumber, journalMonth):
    try:
        if not journalNumber or journalNumber.strip()=="":
            journalNumber = None
        c = conn.cursor()
        c.execute("""insert into JOURNAL_CITATION values (%s,%s,%s,%s,%s)""", (pwwEntryId, journalTitle, journalVolume, journalNumber, journalMonth))
    except Exception as e:
        st.error(f"Error in inserting in journal table: {e}")
        raise Exception(f"Insert journal failed: {e}")

#insert in the author intersection table
def insert_author_pww_intersection(conn, pwwEntryId, authorId):
    try:
        c = conn.cursor()
        c.execute("""insert into PWW_ENTRY_AUTHOR_INTERSECTION (PWWAuthorId, PWWEntryId) values (%s,%s)""", (authorId, pwwEntryId))
    except Exception as e:
        st.error(f"Error in inserting author: {e}")
        raise Exception(f"Insert author intersection failed: {e}")

#insert in the keyword intersection table
def insert_keyword_pww_intersection(conn, pwwEntryId, keywordId):
    try:
        if keywordId is None:
            print("No valid keyword provided; skipping insertion into the intersection table.")
            return None
        c = conn.cursor()
        c.execute("""insert into PWW_TAGGED_KEYWORDS (PWWEntryId, KeywordId) values (%s,%s)""", (pwwEntryId, keywordId))
    except Exception as e:
        st.error(f"Error in inserting keyword: {e}")
        raise Exception(f"Insert keyword intersection failed: {e}")

#insert in the topic intersection table
def insert_topic_pww_intersection(conn, pwwEntryId, topicId):
    try:
        if topicId is None:
            print("No valid topic provided; skipping insertion into the intersection table.")
            return None
        c = conn.cursor()
        c.execute("""insert into PWW_TAGGED_TOPICS (PWWEntryId, TopicId) values (%s,%s)""", (pwwEntryId, topicId))
    except Exception as e:
        st.error(f"Error in inserting topic: {e}")
        raise Exception(f"Insert topic intersection failed: {e}")

#insert in the theorem intersection table
def insert_theorem_pww_intersection(conn, pwwEntryId, theoremId):
    try:
        if theoremId is None:
            print("No valid theorem provided; skipping insertion into the intersection table.")
            return None
        c = conn.cursor()
        c.execute("""insert into PWW_TAGGED_THEOREMS (PWWEntryId, TheoremId) values (%s,%s)""", (pwwEntryId, theoremId))     
    except Exception as e:
        st.error(f"Error in inserting theorem: {e}")
        raise Exception(f"Insert theorem intersection failed: {e}")

#insert in the cited works intersection table
def insert_cited_works_pww_intersection(conn, pwwEntryId, citationId):
    try:
        if citationId is None:
            print("No valid citation provided; skipping insertion into the intersection table.")
            return None
        c = conn.cursor()
        c.execute("""insert into PWW_TAGGED_CITED_WORKS (PWWEntryId, PWWCitedWorkCitationID) values (%s,%s)""", (pwwEntryId, citationId)) 
    except Exception as e:
        st.error(f"Error in inserting cited works: {e}")
        raise Exception(f"Insert cited works intersection failed: {e}")

#insert in the msc intersection table
def insert_msc_code_pww_intersection(conn, pwwEntryId, msc2020Code, isPrimary):
    try:
        c = conn.cursor()
        query = """ select MSC2020CodeId from MSC_2020_TAGS where MSC2020Codes=%s"""
        c.execute(query, (msc2020Code,))
        msc2020CodeId = c.fetchone()
        if not msc2020CodeId:
            st.error("No valid MSC Code found, skipping insertion in the intersection table.")
            return None
        else:
            c.execute("""insert into PWW_TAGGED_MSC (PWWEntryId, MSC2020CodeId, isPrimaryCode) values (%s,%s,%s)""", (pwwEntryId, msc2020CodeId[0], isPrimary)) 
    except Exception as e:
        st.error(f"Error in inserting msc code: {e}")
        raise Exception(f"Insert msc code intersection failed: {e}")