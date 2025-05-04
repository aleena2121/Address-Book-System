-- Trigger to create a log table for the contacts getting inserted

DELIMITER $$

CREATE TRIGGER after_contact_insert
AFTER INSERT ON contacts
FOR EACH ROW
BEGIN
    INSERT INTO contacts_log(id, name)
    VALUES (NEW.id, NEW.first_name);
END$$

DELIMITER ;
