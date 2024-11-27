CREATE VIEW PWW_DATABASE.PRIVATE_ACCESS_VIEW AS (
    SELECT 
    PWW_ENTRY.PWWEntryId, PWW_ENTRY.PWWTitle,  PWW_ENTRY.PWWShortDescription, PWW_ENTRY.PublishStatus, PWW_ENTRY.PWWAdditionalNotes, PWW_ENTRY.CitationPageStart, PWW_ENTRY.CitationPageEnd, PWW_ENTRY.CitationMediaType, PWW_ENTRY.CitationDOI, PWW_ENTRY.CitationYear, PWW_ENTRY.PWWSourceUrl, PWW_ENTRY.PWWGraphicRightsHolder,  PWW_ENTRY.ProofPdf , 
    GROUP_CONCAT(DISTINCT CASE WHEN PWW_TAGGED_MSC.IsPrimaryCode=1 THEN MSC_2020_TAGS.MSC2020Codes END) AS PRIMARY_MSC_CODE, 
    GROUP_CONCAT(DISTINCT CASE WHEN PWW_TAGGED_MSC.IsPrimaryCode=0 THEN MSC_2020_TAGS.MSC2020Codes END) AS SECONDARY_MSC_CODE, 
    GROUP_CONCAT(DISTINCT TOPIC_TAGS.TopicName) AS TOPICS,
    GROUP_CONCAT(DISTINCT THEOREM_TAGS.Theorem) AS THEOREMS,
    GROUP_CONCAT(DISTINCT CITED_WORKS.GivenCitation) AS CITATIONS,
    GROUP_CONCAT(DISTINCT CONCAT(PWW_AUTHOR.AuthorLastName,', ', PWW_AUTHOR.AuthorFirstName) SEPARATOR '; ') AS Authors,
    CONCAT(USER_INFORMATION.UserLastName, ', ', USER_INFORMATION.UserFirstName) AS ENTRY_CREATOR
    -- JOIN AUTHOR TABLE
    FROM PWW_ENTRY LEFT OUTER JOIN PWW_ENTRY_AUTHOR_INTERSECTION
    ON PWW_ENTRY.PWWEntryId = PWW_ENTRY_AUTHOR_INTERSECTION.PWWEntryId
    LEFT OUTER JOIN PWW_AUTHOR
    ON PWW_ENTRY_AUTHOR_INTERSECTION.PWWAuthorId = PWW_AUTHOR.PWWAuthorId
    -- JOIN TOPICS TABLE
    LEFT OUTER JOIN PWW_TAGGED_TOPICS
    ON PWW_ENTRY.PWWEntryId = PWW_TAGGED_TOPICS.PWWEntryId
    LEFT OUTER JOIN TOPIC_TAGS
    ON PWW_TAGGED_TOPICS.TopicId = TOPIC_TAGS.TopicId
    -- JOIN THEOREMS TABLE
    LEFT OUTER JOIN PWW_TAGGED_THEOREMS
    ON PWW_ENTRY.PWWEntryId = PWW_TAGGED_THEOREMS.PWWEntryId
    LEFT OUTER JOIN THEOREM_TAGS
    ON PWW_TAGGED_THEOREMS.TheoremId = THEOREM_TAGS.TheoremId
    -- JOIN CITATIONS TABLE
    LEFT OUTER JOIN PWW_TAGGED_CITED_WORKS
    ON PWW_ENTRY.PWWEntryId = PWW_TAGGED_CITED_WORKS.PWWEntryId
    LEFT OUTER JOIN CITED_WORKS
    ON PWW_TAGGED_CITED_WORKS.PWWCitedWorkCitationID = CITED_WORKS.PWWCitedWorkCitationID
    -- JOIN MSC CODES TABLE
    LEFT OUTER JOIN PWW_TAGGED_MSC
    ON PWW_ENTRY.PWWEntryId = PWW_TAGGED_MSC.PWWEntryId
    LEFT OUTER JOIN MSC_2020_TAGS
    ON PWW_TAGGED_MSC.MSC2020CodeId = MSC_2020_TAGS.MSC2020CodeId
    -- JOIN ENTRY CREATOR TABLE
    LEFT OUTER JOIN PWW_ENTRY_CREATORS
    ON PWW_ENTRY.PWWEntryId = PWW_ENTRY_CREATORS.PWWEntryId
    LEFT OUTER JOIN USER_INFORMATION
    ON USER_INFORMATION.UserId = PWW_ENTRY_CREATORS.UserId
    where
    PWW_ENTRY.PublishStatus in ('PublicAccessPublished', 'PrivateAccessPublished', 'NeedsReview')
    GROUP BY PWW_ENTRY.PWWEntryId
);