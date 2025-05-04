-- Stored procedure to add contact to db
DELIMITER $$

CREATE PROCEDURE add_contacts_to_db(
    IN first_name VARCHAR(50),
    IN last_name VARCHAR(50),
    IN email VARCHAR(100),
    IN phone_number VARCHAR(15),
    IN address VARCHAR(255),
    IN city VARCHAR(50),
    IN state VARCHAR(50),
    IN zip VARCHAR(6),
    IN address_book_id INT
)
BEGIN
    INSERT INTO contacts (
        address_book_id, first_name, last_name, email,
        phone_number, address, city, state, zip, is_valid
    ) VALUES (
        address_book_id, first_name, last_name, email,
        phone_number, address, city, state, zip, 0
    );
END$$

DELIMITER ;


-- stored procedure to get contacts data from each addressbook and store into csv

DELIMITER $$

CREATE PROCEDURE get_contacts_by_address_book(
    IN address_book_name VARCHAR(50)
)
BEGIN
    SELECT * 
    FROM contacts 
    WHERE address_book_id IN (
        SELECT id 
        FROM addressbooks 
        WHERE name = address_book_name
    );
END$$

DELIMITER ;



-- stored procedure to export data to csv
DELIMITER $$

CREATE PROCEDURE ExportDataToCSV ()
BEGIN
    SET @timestamp = DATE_FORMAT(NOW(), '%Y%m%d_%H%i%s');
    SET @file = CONCAT('C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/address_book_details_', @timestamp, '.csv');

    SET @sql = CONCAT(
        "SELECT 'Total Address Books' AS type, NULL AS name, COUNT(*) AS count ",
        "FROM AddressBooks ",
        "UNION ALL ",
        "SELECT 'Address Book Details' AS type, ab.name, COUNT(c.id) ",
        "FROM AddressBooks ab ",
        "LEFT JOIN Contacts c ON ab.id = c.address_book_id ",
        "GROUP BY ab.id, ab.name ",
        "UNION ALL ",
        "SELECT 'Average Contacts Per Book' AS type, NULL AS name, ROUND(AVG(contact_counts.count), 2) AS avg_count ",
        "FROM (SELECT COUNT(c.id) AS count FROM AddressBooks ab ",
        "LEFT JOIN Contacts c ON ab.id = c.address_book_id GROUP BY ab.id) AS contact_counts ",
        "INTO OUTFILE '", @file, "' ",
        "FIELDS TERMINATED BY ',' ENCLOSED BY '\"' LINES TERMINATED BY '\n'"
    );

    PREPARE stmt FROM @sql;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END$$

DELIMITER ;

