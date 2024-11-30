DELIMITER //

CREATE PROCEDURE ChangeProofToPrivate()
BEGIN
    DECLARE entryId BIGINT;
    DECLARE endDate DATE;
    DECLARE done INT DEFAULT 0;
    
    DECLARE C1 CURSOR FOR SELECT PWWEntryId, publicAccessEndDate FROM PUBLIC_ACCESS_DATES_PWW WHERE publicAccessEndDate <= CURRENT_DATE;

    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

    OPEN C1;

    FETCH C1 INTO entryId, endDate;
    WHILE done = 0 DO 
       
        UPDATE PWW_ENTRY SET PublishStatus = 'PrivateAccessPublished' WHERE PWWEntryId = entryId;

        DELETE FROM PUBLIC_ACCESS_DATES_PWW WHERE PWWEntryId = entryId;

        --INSERT INTO test_sp_execution (TimeOfExec) VALUES (CURRENT_TIMESTAMP);

        FETCH C1 INTO entryId, endDate;
    END WHILE;

    CLOSE C1;
END;
//

DELIMITER ;

--event for the procedure to run every 5 seconds
CREATE EVENT runEveryFiveSeconds
    ON SCHEDULE EVERY 5 SECOND
      DO
        CALL PWW_DATABASE.ChangeProofToPrivate();
    
