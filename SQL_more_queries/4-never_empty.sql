-- Creates the table id_not_null with id INT default 1 and name VARCHAR(256).
-- If the table already exists, the script does not fail.
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
