-- script that creates the database hbtn_0d_usa and the
-- table states (in the database hbtn_0d_usa) on your MySQL server.
-- script that creates the table unique_id on your MySQL server.
CREATE TABLE IF NOT EXISTS states (
    id INT PRIMARY NOT NULL UNIQUE AUTO GENERATED,
    name VARCHAR(256) NOT NULL
);