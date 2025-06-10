-- Creating the bank_reviews database (Note: In Oracle XE, databases are managed within the instance, so we create a schema instead)
-- Connect as SYS or SYSTEM to create the user/schema
CREATE USER bank_reviews IDENTIFIED BY password123;
GRANT CONNECT, RESOURCE, CREATE SESSION, CREATE TABLE TO bank_reviews;

-- Connect to the bank_reviews schema
ALTER SESSION SET CURRENT_SCHEMA = bank_reviews;

-- Creating Banks table
CREATE TABLE Banks (
    bank_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    bank_name VARCHAR2(100) NOT NULL,
    country VARCHAR2(50) DEFAULT 'Ethiopia',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Creating Reviews table
CREATE TABLE Reviews (
    review_id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    bank_id NUMBER NOT NULL,
    review_text VARCHAR2(4000) NOT NULL,
    sentiment VARCHAR2(20) CHECK (sentiment IN ('Positive', 'Negative', 'Neutral')),
    review_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_bank_id FOREIGN KEY (bank_id) REFERENCES Banks(bank_id)
);

-- Insert sample bank data (Commercial Bank of Ethiopia)
INSERT INTO Banks (bank_name, country) VALUES ('Commercial Bank of Ethiopia', 'Ethiopia');

-- Commit the changes
COMMIT;