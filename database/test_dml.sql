USE PWW_DATABASE;
/* insert into the main PWW_ENTRY TABLE*/

insert into PWW_ENTRY(PWWTitle, PWWShortDescription, PublishStatus, CitationMediaType, CitationDOI, CitationYear, PWWSourceUrl, 
PWWGraphicRightsHolder, ProofPdf ) values
('Proof Without Words: Varignon\’s Theorem', 'A visual proof of Varignon\’s Theorem', 'PublicAccessPublished', 'Journal',
'10.4169/college.math.j.48.5.354', 2017, 'https://www.jstor.org/stable/10.4169/college.math.j.48.5.354','MAA', 'Pal17.pdf');

insert into PWW_ENTRY(PWWTitle, PWWShortDescription, PublishStatus, CitationMediaType, CitationDOI, CitationYear, PWWSourceUrl, 
PWWGraphicRightsHolder, ProofPdf ) values
('Proof without Words: Algebraic Areas', 'Proof that $(a+b)^2+(a-b)^2=2(a^2+b^2)$ using rectangles', 'PublicAccessPublished', 'Journal',
NULL, 1984, 'http://www.jstor.org/stable/2689683','MAA', 'Wak84.pdf');

insert into PWW_ENTRY(PWWTitle, PWWShortDescription, PublishStatus, CitationMediaType, CitationDOI, CitationYear, PWWSourceUrl, 
PWWGraphicRightsHolder, ProofPdf ) values
('Proof without Words: A 2 × 2 Determinant Is the Area of a Parallelogram', 'Uses the difference in areas of two rectangles to show that the value of the determinant is the area of an associated rectangle.', 'PublicAccessPublished', 'Journal',
NULL , 1985, 'http://www.jstor.org/stable/2689900','MAA', 'Gol85.pdf');

insert into PWW_ENTRY(PWWTitle, PWWShortDescription, PublishStatus, CitationMediaType, CitationDOI, CitationYear, PWWSourceUrl, 
PWWGraphicRightsHolder, ProofPdf ) values
('Behold! The Pythagorean Theorem via Mean Proportions', 'A proof of the Pythagorean Theorem using a triangle erected on the diameter of a circle of radius $c$ with legs of length $a$ and $b$.', 'PublicAccessPublished', 'Journal',
NULL , 1986, 'http://www.jstor.org/stable/2686255','MAA', 'Har86.pdf');

insert into PWW_ENTRY(PWWTitle, PWWShortDescription, PublishStatus, CitationMediaType, CitationDOI, CitationYear, PWWSourceUrl, 
PWWGraphicRightsHolder, ProofPdf ) values
('Proof without Words: The Arithmetic Mean-Geometric Mean Inequality', 'Dissection of a square into 4 rectangles and a square to demonstrate the inequality.', 'PublicAccessPublished', 'Journal',
NULL, 1986, 'http://www.jstor.org/stable/2690011','MAA', 'Sch86.pdf');

insert into PWW_ENTRY(PWWTitle, PWWShortDescription, PublishStatus, CitationMediaType, CitationDOI, CitationYear, PWWSourceUrl, 
PWWGraphicRightsHolder, ProofPdf ) values
('Proof without Words', 'Single diagram using similar triangles and squares of increasing sizes to demonstrate by $1+2+\cdots +n=\frac{1}{2}n(n+1)$ and $1^3+2^3+\cdots +n^3=\left(\frac{1}{2}n(n+1)\right)^2$.', 'PrivateAccessPublished', 'Journal',
NULL, 1992, 'http://www.jstor.org/stable/2691330','MAA', 'Sch92.pdf');


insert into PWW_ENTRY(PWWTitle, PWWShortDescription, PublishStatus, CitationMediaType, CitationDOI, CitationYear, PWWSourceUrl, 
PWWGraphicRightsHolder, ProofPdf ) values
('The Pythagorean Theorem VI', 'A proof of the Pythagorean Theorem using a triangle erected on the diameter of a circle of radius $c$ with legs of length $a$ and $b$.', 'PublicAccessPublished', 'Journal',
NULL, 1993, NULL,'MAA', 'pdf7');

insert into PWW_ENTRY(PWWTitle, PWWShortDescription, PublishStatus, CitationMediaType, CitationDOI, CitationYear, PWWSourceUrl, 
PWWGraphicRightsHolder, ProofPdf ) values
('Area under an Arch of the Cycloid', 'Proof that area under an arch of the cycloid is $3\pi R^2$ where $R$ is the radius of the circle. Method uses dissection of arch into a circle, and two copies of a region of area $\pi R^2$.', 'PublicAccessPublished', 'Journal',
NULL, 1993, NULL,'MAA', 'Bee93.pdf');

insert into PWW_ENTRY(PWWTitle, PWWShortDescription, PublishStatus, CitationMediaType, CitationDOI, CitationYear, PWWSourceUrl, 
PWWGraphicRightsHolder, ProofPdf ) values
('Proof without Words: Area under a Cycloid Cusp', 'Proof that area under an arch of the cycloid is $3\pi R^2$ where $R$ is the radius of the circle. Method uses dissection of arch into a circle, and two copies of a region of area $\pi R^2$.', 'NeedsReview', 'Journal',
NULL, 1993, 'http://www.jstor.org/stable/2690472','MAA', 'Bee93_2.pdf');

insert into PWW_ENTRY(PWWTitle, PWWShortDescription, PublishStatus, CitationMediaType, CitationDOI, CitationYear, PWWSourceUrl, 
PWWGraphicRightsHolder, ProofPdf ) values
('Proof Without Words: Series of Perfect Powers', 'A subdivision of a unit square into self-similar collections of rectangles is used to demonstrate that the sum of reciprocals of all perfect powers is 1.', 'PublicAccessPublished', 'Journal',
'10.4169/math.mag.90.4.286', 2017, 'https://www.jstor.org/stable/10.4169/math.mag.90.4.286','MAA', 'Edg17.pdf');

/*Inserts into the PWW_AUTHOR Table*/

insert into PWW_AUTHOR(AuthorFirstName, AuthorLastName) values('Alik', 'Palatnik');
insert into PWW_AUTHOR(AuthorFirstName, AuthorLastName) values('Shirley', 'Wakin');
insert into PWW_AUTHOR(AuthorFirstName, AuthorLastName) values('Solomon', 'W. Golomb');
insert into PWW_AUTHOR(AuthorFirstName, AuthorLastName) values('Michael', 'Hardy');
insert into PWW_AUTHOR(AuthorFirstName, AuthorLastName) values('Doris', 'Schattschneider');
insert into PWW_AUTHOR(AuthorFirstName, AuthorLastName) values('Georg', 'Schrage');
insert into PWW_AUTHOR(AuthorFirstName, AuthorLastName) values('Michael', 'Hardy');
insert into PWW_AUTHOR(AuthorFirstName, AuthorLastName) values('Richard', 'M. Beekman');
insert into PWW_AUTHOR(AuthorFirstName, AuthorLastName) values('Tom', 'Edgar');

/*inserts into the BOOK TABLE*/

insert into BOOK_CITATION(PWWEntryId, BookAuthor, BookTitle, BookSeries, ISBN) values (10006, 'Roger Nelsen', 'Proofs without words: Exercises in visual thinking', 'AMS/MAA Classroom Resource Materials', '978-1-4704-5186-8');
insert into BOOK_CITATION(PWWEntryId, BookAuthor, BookTitle, BookSeries, ISBN) values (10007, 'Roger Nelsen', 'Proofs without words: Exercises in visual thinking', 'AMS/MAA Classroom Resource Materials', '978-1-4704-5186-8');

/*inserts into the JOURNAL TABLE*/

insert into JOURNAL_CITATION(PWWEntryId, JournalTitle, JournalVolume, JournalNumber, JournalMonth) values (10000, 
'The College Mathematics Journal', 48, 5, NULL);
insert into JOURNAL_CITATION(PWWEntryId, JournalTitle, JournalVolume, JournalNumber, JournalMonth) values (10001, 
'Mathematics Magazine', 57, 4, NULL);
insert into JOURNAL_CITATION(PWWEntryId, JournalTitle, JournalVolume, JournalNumber, JournalMonth) values (10002,
'Mathematics Magazine', 58, 2, NULL);
insert into JOURNAL_CITATION(PWWEntryId, JournalTitle, JournalVolume, JournalNumber, JournalMonth) values (10003,
'The College Mathematics Journal', 17, 5, NULL);
insert into JOURNAL_CITATION(PWWEntryId, JournalTitle, JournalVolume, JournalNumber, JournalMonth) values (10004,
'Mathematics Magazine', 59, 1, NULL);
insert into JOURNAL_CITATION(PWWEntryId, JournalTitle, JournalVolume, JournalNumber, JournalMonth) values (10005,
'Mathematics Magazine', 65, 3, NULL);
insert into JOURNAL_CITATION(PWWEntryId, JournalTitle, JournalVolume, JournalNumber, JournalMonth) values (10008,
'Mathematics Magazine', 66, 1, NULL);
insert into JOURNAL_CITATION(PWWEntryId, JournalTitle, JournalVolume, JournalNumber, JournalMonth) values (10009,
'Mathematics Magazine', 90, 4, NULL);

/*inserts into the PUBLIC ACCESS START DATE TABLE*/

insert into PUBLIC_ACCESS_DATES_PWW (PWWEntryId, PublicAccessStartDate) VALUES (10000, '2024-11-20');
insert into PUBLIC_ACCESS_DATES_PWW (PWWEntryId, PublicAccessStartDate) VALUES (10001, '2024-11-16');
insert into PUBLIC_ACCESS_DATES_PWW (PWWEntryId, PublicAccessStartDate) VALUES (10002, '2024-12-16');
insert into PUBLIC_ACCESS_DATES_PWW (PWWEntryId, PublicAccessStartDate) VALUES (10003, '2024-12-25');
insert into PUBLIC_ACCESS_DATES_PWW (PWWEntryId, PublicAccessStartDate) VALUES (10004, '2024-11-16');
insert into PUBLIC_ACCESS_DATES_PWW (PWWEntryId, PublicAccessStartDate) VALUES (10005, '2024-12-16');
insert into PUBLIC_ACCESS_DATES_PWW (PWWEntryId, PublicAccessStartDate) VALUES (10006, '2024-12-16');
insert into PUBLIC_ACCESS_DATES_PWW (PWWEntryId, PublicAccessStartDate) VALUES (10007, '2024-12-16');
insert into PUBLIC_ACCESS_DATES_PWW (PWWEntryId, PublicAccessStartDate) VALUES (10008, '2024-11-15');
insert into PUBLIC_ACCESS_DATES_PWW (PWWEntryId, PublicAccessStartDate) VALUES (10009, '2024-11-30');

/*inserts into the AUTHOR AND PWW INTERSECTION TABLE*/

insert into PWW_ENTRY_AUTHOR_INTERSECTION (PWWEntryId, PWWAuthorId) VALUES (10000, 25000);
insert into PWW_ENTRY_AUTHOR_INTERSECTION (PWWEntryId, PWWAuthorId) VALUES (10001, 25001);
insert into PWW_ENTRY_AUTHOR_INTERSECTION (PWWEntryId, PWWAuthorId) VALUES (10002, 25002);
insert into PWW_ENTRY_AUTHOR_INTERSECTION (PWWEntryId, PWWAuthorId) VALUES (10003, 25003);
insert into PWW_ENTRY_AUTHOR_INTERSECTION (PWWEntryId, PWWAuthorId) VALUES (10004, 25004);
insert into PWW_ENTRY_AUTHOR_INTERSECTION (PWWEntryId, PWWAuthorId) VALUES (10005, 25004);
insert into PWW_ENTRY_AUTHOR_INTERSECTION (PWWEntryId, PWWAuthorId) VALUES (10006, 25006);
insert into PWW_ENTRY_AUTHOR_INTERSECTION (PWWEntryId, PWWAuthorId) VALUES (10007, 25007);
insert into PWW_ENTRY_AUTHOR_INTERSECTION (PWWEntryId, PWWAuthorId) VALUES (10008, 25007);
insert into PWW_ENTRY_AUTHOR_INTERSECTION (PWWEntryId, PWWAuthorId) VALUES (10009, 25008);
insert into PWW_ENTRY_AUTHOR_INTERSECTION (PWWEntryId, PWWAuthorId) VALUES (10000, 25008);


/*insert into TOPIC Table*/
insert into TOPIC_TAGS (TopicName) VALUES ('Geometry');
insert into TOPIC_TAGS (TopicName) VALUES ('Algebra');
insert into TOPIC_TAGS (TopicName) VALUES ('Linear Algebra');
insert into TOPIC_TAGS (TopicName) VALUES ('Inequalities');
insert into TOPIC_TAGS (TopicName) VALUES ('Series');
insert into TOPIC_TAGS (TopicName) VALUES ('Analytic geometry');
insert into TOPIC_TAGS (TopicName) VALUES ('Differential Calculus');
insert into TOPIC_TAGS (TopicName) VALUES ('Integral Calculus');
insert into TOPIC_TAGS (TopicName) VALUES ('Vector Algebra');
insert into TOPIC_TAGS (TopicName) VALUES ('Statistics');

/*insert into PWW_TAGGED_TOPICS intersection Table*/
insert into PWW_TAGGED_TOPICS (PWWEntryId, TopicId) values (10000,4000);
insert into PWW_TAGGED_TOPICS (PWWEntryId, TopicId) values (10001,4001);
insert into PWW_TAGGED_TOPICS (PWWEntryId, TopicId) values (10003,4002);
insert into PWW_TAGGED_TOPICS (PWWEntryId, TopicId) values (10003,4000);
insert into PWW_TAGGED_TOPICS (PWWEntryId, TopicId) values (10004,4004);
insert into PWW_TAGGED_TOPICS (PWWEntryId, TopicId) values (10005,4004);
insert into PWW_TAGGED_TOPICS (PWWEntryId, TopicId) values (10006,4000);
insert into PWW_TAGGED_TOPICS (PWWEntryId, TopicId) values (10007,4005);
insert into PWW_TAGGED_TOPICS (PWWEntryId, TopicId) values (10008,4005);
insert into PWW_TAGGED_TOPICS (PWWEntryId, TopicId) values (10009,4004);

/*insert into MSC_2020 TAGS table handled in another script*/

/*insert into TAGGED_MSC_CODES intersection table*/
insert into PWW_TAGGED_MSC (PWWEntryId, MSC2020CodeId, IsPrimaryCode) VALUES (10000, 1000, TRUE);
insert into PWW_TAGGED_MSC (PWWEntryId, MSC2020CodeId, IsPrimaryCode) VALUES (10001, 1001, TRUE);
insert into PWW_TAGGED_MSC (PWWEntryId, MSC2020CodeId, IsPrimaryCode) VALUES (10002, 1002, TRUE);
insert into PWW_TAGGED_MSC (PWWEntryId, MSC2020CodeId, IsPrimaryCode) VALUES (10003, 1003, TRUE);
insert into PWW_TAGGED_MSC (PWWEntryId, MSC2020CodeId, IsPrimaryCode) VALUES (10004, 1004, TRUE);
insert into PWW_TAGGED_MSC (PWWEntryId, MSC2020CodeId, IsPrimaryCode) VALUES (10005, 1005, TRUE);
insert into PWW_TAGGED_MSC (PWWEntryId, MSC2020CodeId, IsPrimaryCode) VALUES (10006, 1006, TRUE);
insert into PWW_TAGGED_MSC (PWWEntryId, MSC2020CodeId, IsPrimaryCode) VALUES (10007, 1007, TRUE);
insert into PWW_TAGGED_MSC (PWWEntryId, MSC2020CodeId, IsPrimaryCode) VALUES (10008, 1008, TRUE);
insert into PWW_TAGGED_MSC (PWWEntryId, MSC2020CodeId, IsPrimaryCode) VALUES (10009, 1009, TRUE);
insert into PWW_TAGGED_MSC (PWWEntryId, MSC2020CodeId, IsPrimaryCode) VALUES (10000, 1009, TRUE);
insert into PWW_TAGGED_MSC (PWWEntryId, MSC2020CodeId, IsPrimaryCode) VALUES (10009, 1008, TRUE);



/*insert into THEOREM_TAGS table*/
insert into THEOREM_TAGS (Theorem) VALUES ('Varignon\’s Theorem');
insert into THEOREM_TAGS (Theorem) VALUES ('The Pythagorean Theorem');
insert into THEOREM_TAGS (Theorem) VALUES ('Midpoint Theorem');
insert into THEOREM_TAGS (Theorem) VALUES ('Remainder Theorem');
insert into THEOREM_TAGS (Theorem) VALUES ('Bayes Theorem');
insert into THEOREM_TAGS (Theorem) VALUES ('Inscribed Angle Theorem');
insert into THEOREM_TAGS (Theorem) VALUES ('Angle Bisector Theorem');
insert into THEOREM_TAGS (Theorem) VALUES ('Eulers Formula');
insert into THEOREM_TAGS (Theorem) VALUES ('Binomial Theorem');
insert into THEOREM_TAGS (Theorem) VALUES ('Prime Number Theorem');

/*insert into the TAGGED_THEOREM intersection table*/
insert into PWW_TAGGED_THEOREMS (PWWEntryId, TheoremId) VALUES (10000,2000);
insert into PWW_TAGGED_THEOREMS (PWWEntryId, TheoremId) VALUES (10001,2001);
insert into PWW_TAGGED_THEOREMS (PWWEntryId, TheoremId) VALUES (10002,2002);
insert into PWW_TAGGED_THEOREMS (PWWEntryId, TheoremId) VALUES (10003,2003);
insert into PWW_TAGGED_THEOREMS (PWWEntryId, TheoremId) VALUES (10004,2004);
insert into PWW_TAGGED_THEOREMS (PWWEntryId, TheoremId) VALUES (10005,2006);
insert into PWW_TAGGED_THEOREMS (PWWEntryId, TheoremId) VALUES (10006,2006);
insert into PWW_TAGGED_THEOREMS (PWWEntryId, TheoremId) VALUES (10007,2007);
insert into PWW_TAGGED_THEOREMS (PWWEntryId, TheoremId) VALUES (10008,2008);
insert into PWW_TAGGED_THEOREMS (PWWEntryId, TheoremId) VALUES (10009,2009);
insert into PWW_TAGGED_THEOREMS (PWWEntryId, TheoremId) VALUES (10000,2002);
insert into PWW_TAGGED_THEOREMS (PWWEntryId, TheoremId) VALUES (10009,2004);

/*insert into the KEYWORD_TAGS table*/
insert into KEYWORD_TAGS (Keyword) VALUES ('Topology');
insert into KEYWORD_TAGS (Keyword) VALUES ('Linear Algebra');
insert into KEYWORD_TAGS (Keyword) VALUES ('Geometry');
insert into KEYWORD_TAGS (Keyword) VALUES ('Number Theory');
insert into KEYWORD_TAGS (Keyword) VALUES ('Combinatorics');
insert into KEYWORD_TAGS (Keyword) VALUES ('Graph Theory');
insert into KEYWORD_TAGS (Keyword) VALUES ('Probability');
insert into KEYWORD_TAGS (Keyword) VALUES ('Mathematical Modeling');
insert into KEYWORD_TAGS (Keyword) VALUES ('Abstract Algebra');
insert into KEYWORD_TAGS (Keyword) VALUES ('Optimization');

/*insert into the PWW_TAGGED_TOPICS intersection table*/
insert into PWW_TAGGED_KEYWORDS(PWWEntryId, KeywordId) VALUES (10000, 3001);
insert into PWW_TAGGED_KEYWORDS(PWWEntryId, KeywordId) VALUES (10001, 3002);
insert into PWW_TAGGED_KEYWORDS(PWWEntryId, KeywordId) VALUES (10002, 3003);
insert into PWW_TAGGED_KEYWORDS(PWWEntryId, KeywordId) VALUES (10003, 3003);
insert into PWW_TAGGED_KEYWORDS(PWWEntryId, KeywordId) VALUES (10004, 3005);
insert into PWW_TAGGED_KEYWORDS(PWWEntryId, KeywordId) VALUES (10005, 3006);
insert into PWW_TAGGED_KEYWORDS(PWWEntryId, KeywordId) VALUES (10006, 3007);
insert into PWW_TAGGED_KEYWORDS(PWWEntryId, KeywordId) VALUES (10007, 3008);
insert into PWW_TAGGED_KEYWORDS(PWWEntryId, KeywordId) VALUES (10008, 3009);
insert into PWW_TAGGED_KEYWORDS(PWWEntryId, KeywordId) VALUES (10009, 3000);
insert into PWW_TAGGED_KEYWORDS(PWWEntryId, KeywordId) VALUES (10000, 3004);
insert into PWW_TAGGED_KEYWORDS(PWWEntryId, KeywordId) VALUES (10009, 3002);



/*insert into the USER_ROLES Table*/
insert into USER_ROLES (RoleName, ShortRoleDescription) VALUES ('Editor','Its the editor of the journal and editors of the repository');
insert into USER_ROLES (RoleName, ShortRoleDescription) VALUES ('DataEntry','Data entry staff will be primarily student and volunteers trained to populate the database with new entries');
insert into USER_ROLES (RoleName, ShortRoleDescription) VALUES ('Referee','These people will need to be able to access all of the content in the database for a limited period of time, but will not have access to editing functionality.');
insert into USER_ROLES (RoleName, ShortRoleDescription) VALUES ('GeneralUser','These people will have access to view but not edit the content of the database, and will have limited or no access to the images');

/*insert into the USER_INFORMATION Table, only 2 users created for now*/

insert into USER_INFORMATION (RoleId, UserFirstName, UserLastName, UserEmailAddress, UserPassword, UserAccessStartDate) VALUES
(1, 'Gordon', 'Williams', 'giwilliams@alaska.edu', 'testPassword', '2024-11-16');
insert into USER_INFORMATION (RoleId, UserFirstName, UserLastName, UserEmailAddress, UserPassword, UserAccessStartDate) VALUES
(2, 'Siddhant', 'Saha', 'saha.si@northeastern.edu', 'testPassword2', '2024-11-16');
insert into USER_INFORMATION (RoleId, UserFirstName, UserLastName, UserEmailAddress, UserPassword, UserAccessStartDate) VALUES
(3, 'Elizabeth', 'Sluchak', 'sluchak.e@northeastern.edu', 'testPassword3', '2024-11-16');
insert into USER_INFORMATION (RoleId, UserFirstName, UserLastName, UserEmailAddress, UserPassword, UserAccessStartDate) VALUES
(4, 'Ethan', 'Virgil', 'virgil.e@northeastern.edu', 'testPassword4', '2024-11-16');

/*insert into the PWW_ENTRY_CREATOR intersection table*/
insert into PWW_ENTRY_CREATORS(PWWEntryId, UserId, DateEdited) VALUES (10000, 100000, '2024-11-15');
insert into PWW_ENTRY_CREATORS(PWWEntryId, UserId, DateEdited) VALUES (10001, 100000, '2024-11-16');
insert into PWW_ENTRY_CREATORS(PWWEntryId, UserId, DateEdited) VALUES (10002, 100000, '2024-10-15');
insert into PWW_ENTRY_CREATORS(PWWEntryId, UserId, DateEdited) VALUES (10003, 100000, '2024-09-15');
insert into PWW_ENTRY_CREATORS(PWWEntryId, UserId, DateEdited) VALUES (10004, 100000, '2024-08-15');
insert into PWW_ENTRY_CREATORS(PWWEntryId, UserId, DateEdited) VALUES (10005, 100000, '2024-11-15');
insert into PWW_ENTRY_CREATORS(PWWEntryId, UserId, DateEdited) VALUES (10006, 100000, '2024-11-15');
insert into PWW_ENTRY_CREATORS(PWWEntryId, UserId, DateEdited) VALUES (10007, 100001, '2024-11-15');
insert into PWW_ENTRY_CREATORS(PWWEntryId, UserId, DateEdited) VALUES (10008, 100001, '2024-11-15');
insert into PWW_ENTRY_CREATORS(PWWEntryId, UserId, DateEdited) VALUES (10009, 100000, '2024-12-01');

/*insert into CITED_WORKS table*/
insert into CITED_WORKS(GivenCitation) values ('Dummy citation 1');
insert into CITED_WORKS(GivenCitation) values ('Dummy citation 2');
insert into CITED_WORKS(GivenCitation) values ('Dummy citation 3');
insert into CITED_WORKS(GivenCitation) values ('Dummy citation 4');
insert into CITED_WORKS(GivenCitation) values ('Dummy citation 5');
insert into CITED_WORKS(GivenCitation) values ('Dummy citation 6');
insert into CITED_WORKS(GivenCitation) values ('Dummy citation 7');
insert into CITED_WORKS(GivenCitation) values ('Dummy citation 8');
insert into CITED_WORKS(GivenCitation) values ('Dummy citation 9');
insert into CITED_WORKS(GivenCitation) values ('Dummy citation 10');

/*insert into PWW_TAGGED_CITED_WORKS intersection table*/
insert into PWW_TAGGED_CITED_WORKS(PWWEntryId, PWWCitedWorkCitationID) values (10000,5000);
insert into PWW_TAGGED_CITED_WORKS(PWWEntryId, PWWCitedWorkCitationID) values (10001,5001);
insert into PWW_TAGGED_CITED_WORKS(PWWEntryId, PWWCitedWorkCitationID) values (10002,5002);
insert into PWW_TAGGED_CITED_WORKS(PWWEntryId, PWWCitedWorkCitationID) values (10003,5005);
insert into PWW_TAGGED_CITED_WORKS(PWWEntryId, PWWCitedWorkCitationID) values (10003,5003);
insert into PWW_TAGGED_CITED_WORKS(PWWEntryId, PWWCitedWorkCitationID) values (10005,5004);
insert into PWW_TAGGED_CITED_WORKS(PWWEntryId, PWWCitedWorkCitationID) values (10006,5006);
insert into PWW_TAGGED_CITED_WORKS(PWWEntryId, PWWCitedWorkCitationID) values (10007,5007);
insert into PWW_TAGGED_CITED_WORKS(PWWEntryId, PWWCitedWorkCitationID) values (10008,5008);
insert into PWW_TAGGED_CITED_WORKS(PWWEntryId, PWWCitedWorkCitationID) values (10009,5009);


