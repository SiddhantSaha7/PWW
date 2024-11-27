DELIMITER //

CREATE TRIGGER CheckPrimaryMscCodeCount
BEFORE INSERT ON PWW_TAGGED_MSC 
FOR EACH ROW
BEGIN
    DECLARE primaryCodeCount INT;

	SELECT COUNT(*) INTO primaryCodeCount
    FROM PWW_TAGGED_MSC
    WHERE IsPrimaryCode = 1 AND PWWEntryId = NEW.PWWEntryId;

    IF primaryCodeCount = 2 AND NEW.IsPrimaryCode = 1 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Cannot have more than 2 primary MSC codes for a PWW entry';
    END IF;
END //

DELIMITER ;

