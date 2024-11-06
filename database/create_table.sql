CREATE DATABASE PWW_DATABASE;

CREATE TABLE PWW_DATABASE.PWW_ENTRY(
    PWWEntryId BIGINT NOT NULL AUTO_INCREMENT,
    PWWTitle MEDIUMTEXT NOT NULL Default('Proof Without Words'),
    PWWShortDescription MEDIUMTEXT NULL,
    PWWAdditionalNotes LONGTEXT NULL,
    PublishStatus TINYTEXT NOT NULL,
    CitationPageStart SMALLINT  NULL,
    CitationPageEnd SMALLINT NULL,
    CitationMediaType TINYTEXT NULL,
    CitationDOI MEDIUMTEXT NULL,
    CitationYear SMALLINT NULL,
    PWWSourceUrl MEDIUMTEXT NULL,
    PWWGraphicRightsHolder MEDIUMTEXT NULL,
    ProofPdf MEDIUMTEXT NULL,
    Constraint PWW_Entry_PK PRIMARY KEY(PWWEntryId),
    Constraint PWW_Entry_AK1_1 UNIQUE(CitationDOI),
    Constraint PWW_Entry_AK2_1 UNIQUE(PWWSourceUrl),
    Constraint PWW_Entry_AK3_1 UNIQUE(ProofPdf),
    Constraint CitationPageEndCheck CHECK (CitationPageEnd>CitationPageStart),
    Constraint CitationMediaType CHECK (CitationMediaType in ('Book', 'Journal'))
);

CREATE TABLE PWW_DATABASE.PUBLIC_ACCESS_DATES_PWW(
    PWWEntryId BIGINT NOT NULL,
    PublicAccessStartDate DATE NOT NULL,
    PublicAccessEndDate DATE NOT NULL DEFAULT('9999-12-31'),
    Constraint PUBLIC_ACCESS_DATES_PWW_PK PRIMARY KEY(PWWEntryId),
    Constraint PUBLIC_ACCESS_DATES_PWW_FK FOREIGN KEY(PWWEntryId) REFERENCES PWW_ENTRY(PWWEntryId) ON UPDATE NO ACTION ON DELETE CASCADE
);

CREATE TABLE PWW_DATABASE.BOOK_CITATION(
    PWWEntryId BIGINT NOT NULL,
    BookAuthor VARCHAR(50) NOT NULL,
    BookTitle VARCHAR(100) NOT NULL,
    BookSeries VARCHAR(100) NULL,
    ISBN CHAR(17) NOT NULL,
    Constraint BOOK_CITATION_PK PRIMARY KEY(PWWEntryId),
    Constraint BOOK_CITATION_FK FOREIGN KEY(PWWEntryId) REFERENCES PWW_ENTRY(PWWEntryId) ON UPDATE NO ACTION ON DELETE CASCADE,
    Constraint BOOK_CITATION_AK1_1 UNIQUE(ISBN)
);

CREATE TABLE PWW_DATABASE.JOURNAL_CITATION(
    PWWEntryId BIGINT NOT NULL,
    JournalTitle VARCHAR(50) NOT NULL,
    JournalVolume INT NOT NULL,
    JournalNumber INT NULL,
    JournalMonth VARCHAR(15) NOT NULL,
    Constraint JOURNAL_CITATION_PK PRIMARY KEY(PWWEntryId),
    Constraint JOURNAL_CITATION_FK FOREIGN KEY(PWWEntryId) REFERENCES PWW_ENTRY(PWWEntryId) ON UPDATE NO ACTION ON DELETE CASCADE
);

CREATE TABLE PWW_DATABASE.PWW_AUTHOR(
    PWWAuthorId BIGINT NOT NULL AUTO_INCREMENT,
    AuthorFirstName VARCHAR(30) NOT NULL DEFAULT('unknown'),
    AuthorLastName VARCHAR(30) NOT NULL DEFAULT('unknown'),
    Constraint PWW_AUTHOR_PK PRIMARY KEY(PWWAuthorId)
);

CREATE TABLE PWW_DATABASE.PWW_ENTRY_AUTHOR_INTERSECTION(
    PWWAuthorId BIGINT NOT NULL,
    PWWEntryId BIGINT NOT NULL,
    CONSTRAINT PWW_ENTRY_AUTHOR_INTERSECTION_PK PRIMARY KEY(PWWEntryId, PWWAuthorId),
    CONSTRAINT PWW_ENTRY_AUTHOR_INTERSECTION_FK1_1 FOREIGN KEY(PWWEntryId) REFERENCES PWW_ENTRY(PWWEntryId) ON UPDATE NO ACTION ON DELETE CASCADE,
    CONSTRAINT PWW_ENTRY_AUTHOR_INTERSECTION_FK2_1 FOREIGN KEY(PWWAuthorId) REFERENCES PWW_AUTHOR(PWWAuthorId) ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE PWW_DATABASE.MSC_2020_TAGS(
    MSC2020CodeId BIGINT NOT NULL AUTO_INCREMENT,
    MSC2020Codes TINYTEXT NOT NULL,
    MathematicalField MEDIUMTEXT NOT NULL,
    CONSTRAINT MSC_2020_TAGS_PK PRIMARY KEY(MSC2020CodeId),
    CONSTRAINT MSC_2020_TAGS_AK_1_1 UNIQUE(MSC2020Codes),
    CONSTRAINT MSC_2020_TAGS_AK_2_1 UNIQUE(MathematicalField) 
);

CREATE TABLE PWW_DATABASE.PWW_TAGGED_MSC(
    PWWEntryId BIGINT NOT NULL,
    MSC2020CodeId BIGINT NOT NULL,
    IsPrimaryCode Boolean NOT NULL, 
    CONSTRAINT PWW_TAGGED_MSC_PK PRIMARY KEY(PWWEntryId, MSC2020CodeId),
    CONSTRAINT PWW_TAGGED_MSC_FK_1_1 FOREIGN KEY(PWWEntryId) REFERENCES PWW_ENTRY(PWWEntryId) ON UPDATE NO ACTION ON DELETE CASCADE,
    CONSTRAINT PWW_TAGGED_MSC_FK_2_1 FOREIGN KEY(MSC2020CodeId) REFERENCES MSC_2020_TAGS(MSC2020CodeId) ON UPDATE NO ACTION ON DELETE CASCADE
    /* will have to write a trigger to enforce the 'no more than 2 primary code' rule :( */
);

CREATE TABLE PWW_DATABASE.THEOREM_TAGS(
    TheoremId BIGINT NOT NULL AUTO_INCREMENT,
    Theorem MEDIUMTEXT NOT NULL,
    CONSTRAINT THEOREM_TAGS_PK PRIMARY KEY(TheoremId),
    CONSTRAINT THEOREM_TAGS_AK_1_1 UNIQUE(Theorem) 
);

CREATE TABLE PWW_DATABASE.PWW_TAGGED_THEOREMS(
    PWWEntryId BIGINT NOT NULL,
    TheoremId BIGINT NOT NULL,
    CONSTRAINT PWW_TAGGED_THEOREM_PK PRIMARY KEY(PWWEntryId, TheoremId),
    CONSTRAINT PWW_TAGGED_THEOREM_FK_1_1 FOREIGN KEY(PWWEntryId) REFERENCES PWW_ENTRY(PWWEntryId) ON UPDATE NO ACTION ON DELETE CASCADE,
    CONSTRAINT PWW_TAGGED_THEOREM_FK_2_1 FOREIGN KEY(TheoremId) REFERENCES THEOREM_TAGS(TheoremId) ON UPDATE NO ACTION ON DELETE CASCADE
);

CREATE TABLE PWW_DATABASE.KEYWORD_TAGS(
    KeywordId BIGINT NOT NULL AUTO_INCREMENT,
    Keyword MEDIUMTEXT NOT NULL,
    CONSTRAINT KEYWORD_TAGS_PK PRIMARY KEY(KeywordId),
    CONSTRAINT KEYWORD_TAGS_AK_1_1 UNIQUE(Keyword)
);

CREATE TABLE PWW_DATABASE.PWW_TAGGED_KEYWORDS(
    PWWEntryId BIGINT NOT NULL,
    KeywordId BIGINT NOT NULL,
    CONSTRAINT PWW_TAGGED_KEYWORDS_PK PRIMARY KEY(PWWEntryId, KeywordId),
    CONSTRAINT PWW_TAGGED_KEYWORDS_FK_1_1 FOREIGN KEY(PWWEntryId) REFERENCES PWW_ENTRY(PWWEntryId) ON UPDATE NO ACTION ON DELETE CASCADE,
    CONSTRAINT PWW_TAGGED_KEYWORDS_FK_2_1 FOREIGN KEY(KeywordId) REFERENCES KEYWORD_TAGS(KeywordId) ON UPDATE NO ACTION ON DELETE CASCADE
);

CREATE TABLE PWW_DATABASE.TOPIC_TAGS(
    TopicId BIGINT NOT NULL AUTO_INCREMENT,
    TopicName MEDIUMTEXT NOT NULL,
    CONSTRAINT TOPIC_TAGS_PK PRIMARY KEY(TopicId),
    CONSTRAINT TOPIC_TAGS_AK_1_1 UNIQUE(TopicName)
);

CREATE TABLE PWW_DATABASE.PWW_TAGGED_TOPICS(
    PWWEntryId BIGINT NOT NULL,
    TopicId BIGINT NOT NULL,
    CONSTRAINT PWW_TAGGED_TOPICS_PK PRIMARY KEY(PWWEntryId, TopicId),
    CONSTRAINT PWW_TAGGED_TOPICS_FK_1_1 FOREIGN KEY(PWWEntryId) REFERENCES PWW_ENTRY(PWWEntryId) ON UPDATE NO ACTION ON DELETE CASCADE,
    CONSTRAINT PWW_TAGGED_TOPICS_FK_2_1 FOREIGN KEY(TopicId) REFERENCES TOPIC_TAGS(TopicId) ON UPDATE NO ACTION ON DELETE CASCADE
);


CREATE TABLE PWW_DATABASE.PWW_CITED_WORKS(
    PWWCitedWorkCitationID BIGINT NOT NULL AUTO_INCREMENT,
    PWWEntryID BIGINT NOT NULL,
    GivenCitation MEDIUMTEXT NOT NULL,
    DOI MEDIUMTEXT NULL,
    CONSTRAINT PWW_CITED_WORKS_PK PRIMARY KEY(PWWCitedWorkCitationId, PWWEntryID),
    CONSTRAINT PWW_CITED_WORKS_FK_1_1 FOREIGN KEY(PWWEntryId) REFERENCES PWW_ENTRY(PWWEntryId) ON UPDATE NO ACTION ON DELETE CASCADE
);

CREATE TABLE PWW_DATABASE.USER_INFORMATION(
    UserId BIGINT NOT NULL AUTO_INCREMENT,
    UserFirstName TINYTEXT NOT NULL,
    UserLastName TINYTEXT NOT NULL,
    UserEmailAddress TINYTEXT NOT NULL,
    UserPassword VARCHAR(30) NOT NULL,
    UserAccessStartDate DATE NOT NULL,
    UserAccessEndDate DATE NOT NULL,
    CONSTRAINT USER_INFORMATION_PK PRIMARY KEY(UserId),
    CONSTRAINT USER_INFORMATION_AK_1_1 UNIQUE(UserEmailAddress)
);

CREATE TABLE PWW_DATABASE.PWW_ENTRY_CREATORS(
    PWWEntryId BIGINT NOT NULL,
    UserId BIGINT NOT NULL,
    DateEdited DATE NOT NULL,
    ShortDescriptionOfChange MEDIUMTEXT NULL,
    CONSTRAINT PWW_ENTRY_CREATORS_PK PRIMARY KEY(PWWEntryId, UserId),
    CONSTRAINT PWW_ENTRY_CREATORS_FK_1_1 FOREIGN KEY(PWWEntryId) REFERENCES PWW_ENTRY(PWWEntryId) ON UPDATE NO ACTION ON DELETE CASCADE,
    CONSTRAINT PWW_ENTRY_CREATORS_FK_2_1 FOREIGN KEY(UserId) REFERENCES USER_INFORMATION(UserId) ON UPDATE NO ACTION ON DELETE CASCADE
);

CREATE TABLE PWW_DATABASE.USER_ROLES(
    UserRoleId BIGINT NOT NULL AUTO_INCREMENT,
    RoleName TINYTEXT NOT NULL,
    ShortRoleDescription MEDIUMTEXT NOT NULL,
    CreateAccess BOOLEAN NOT NULL,
    InsertAccess BOOLEAN NOT NULL,
    UpdateAccess BOOLEAN NOT NULL,
    DeleteAccess BOOLEAN NOT NULL,
    CONSTRAINT USER_ROLES_PK PRIMARY KEY(UserRoleId),
    CONSTRAINT USER_ROLES_AK_1_1 UNIQUE(RoleName)
);

CREATE TABLE PWW_DATABASE.USER_ROLE_ASSIGNMENT(
    UserId BIGINT NOT NULL,
    UserRoleId BIGINT NOT NULL,
    CONSTRAINT USER_ROLE_ASSIGNMENT_PK PRIMARY KEY(UserId, UserRoleId),
    CONSTRAINT USER_ROLE_ASSIGNMENT_FK_1_1 FOREIGN KEY(UserRoleId) REFERENCES USER_ROLES(UserRoleId) ON UPDATE NO ACTION ON DELETE CASCADE,
    CONSTRAINT USER_ROLE_ASSIGNMENT_FK_2_1 FOREIGN KEY(UserId) REFERENCES USER_INFORMATION(UserId) ON UPDATE NO ACTION ON DELETE CASCADE
);
