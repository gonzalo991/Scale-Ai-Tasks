-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS citizen_data;

-- Switch to the database
USE citizen_data;

-- Create the citizens table with an email column
CREATE TABLE citizens (
    citizen_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INT,
    salary DECIMAL(10, 2),
    email VARCHAR(100) -- Specify the data type and length for the email column
);

-- Insert data into the citizens table
INSERT INTO citizens (first_name, last_name, age, salary, email)
VALUES ('John', 'Doe', 30, 50000.00, 'john.doe@example.com'),
       ('Jane', 'Smith', 25, 60000.50, 'jane.smith@example.com'),
       ('Michael', 'Johnson', 35, 75000.75, 'michael.johnson@example.com');

SELECT first_name, last_name, email
FROM citizens
WHERE email LIKE '%.com';


SELECT MIN(age) AS min_age, MAX(age) AS max_age
FROM citizens;


SELECT ROUND(salary) AS rounded_salary
FROM citizens;



