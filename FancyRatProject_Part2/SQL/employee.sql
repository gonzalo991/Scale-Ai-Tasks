-- Given the following database and its values, generate a query to know what is the row number assigned 
-- to each record in the table using ROW_NUMBER?

CREATE DATABASE IF NOT EXISTS EmployeeDB;
USE EmployeeDB;

CREATE TABLE Employees (
EmployeeID INT PRIMARY KEY,
FirstName VARCHAR(50),
LastName VARCHAR(50),
Department VARCHAR(50),
Salary DECIMAL(10, 2)
);

INSERT INTO Employees (EmployeeID, FirstName, LastName, Department, Salary)
VALUES
(1, 'John', 'Smith', 'Sales', 50000),
(2, 'Jane', 'Doe', 'HR', 60000),
(3, 'Michael', 'Johnson', 'IT', 70000),
(4, 'Sarah', 'Brown', 'Marketing', 55000),
(5, 'David', 'Lee', 'Finance', 75000),
(6, 'Emily', 'Wilson', 'IT', 65000);

-- Here is the query to get the row number for each record in the table:

SELECT EmployeeID, FirstName, LastName, ROW_NUMBER() OVER (ORDER BY EmployeeID) AS RowNumber
FROM Employees;

-- This query will assign a row number to each record in the Employees table. The ROW_NUMBER() function generates 
-- a unique, sequential number for each row in the result set.

-- The following SQL query can be used to display the details of the three records with the lowest row numbers 
-- using the ROW_NUMBER() function:

SELECT EmployeeID, FirstName, LastName, RowNumber
FROM (
SELECT EmployeeID, FirstName, LastName, ROW_NUMBER() OVER (ORDER BY EmployeeID) AS RowNumber
FROM Employees
) AS Ranked
WHERE RowNumber <= 3;

-- This query interleaves a subquery that assigns row numbers to each set using ROW_NUMBER(). Then, 
-- to give you the details of the three records with the lowest row numbers, the outer query filters out the 
-- records where the row number is less than or equal to 3.

-- The row number of a specific record in the table can be found using the following SQL query:

SELECT RowNumber
FROM (
SELECT EmployeeID, FirstName, LastName, ROW_NUMBER() OVER (ORDER BY EmployeeID) AS RowNumber
FROM Employees
) AS Ranked
WHERE EmployeeID = 1;

-- This query will return the row number of the record with an EmployeeID of 1. The ROW_NUMBER() function 
-- generates a unique, sequential number for each row in the result set, and the WHERE clause filters the 
-- records based on the specified EmployeeID.
-- The result of the query would be:

-- RowNumber
-- 1

-- This indicates that the employee with EmployeeID 1 has a row number of 1 when ordered by EmployeeID.

-- The following SQL query can be used to list the records in the table that have even row numbers:

SELECT *
FROM (
SELECT EmployeeID, FirstName, LastName, ROW_NUMBER() OVER (ORDER BY EmployeeID) AS RowNumber
FROM Employees
) AS EvenRanked
WHERE RowNumber % 2 = 0;

-- This query nests a sub-query that uses ROW_NUMBER() to assign a row number to each of the records. 
-- Then the records with even row numbers (RowNumber % 2 = 0) are filtered out by the outer query. This
-- will give you the details of the records in the Employees table that have an even number of rows.

-- The result of the query would be:

--EmployeeID FirstName LastName Department Salary
--2 Jane Doe HR 60000
--4 Sarah Brown Marketing 55000
--6 Emily Wilson IT 65000

-- This indicates that the records with row numbers 2, 4, and 6 are the ones that have even row 
-- numbers in the Employees table.

-- Here is a SQL query that lists the records with their row numbers and sorts them in descending order:

SELECT *
FROM (
  SELECT EmployeeID, FirstName, LastName, ROW_NUMBER() OVER (ORDER BY EmployeeID) AS RowNumber
  FROM Employees
) AS Ranked
ORDER BY RowNumber DESC;

-- This query encapsulates a subquery that assigns row numbers to each record using ROW_NUMBER(). Then, 
-- based on the assigned row number, the outer query sorts the records in descending order.