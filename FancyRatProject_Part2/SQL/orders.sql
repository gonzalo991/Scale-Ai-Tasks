-- create a mysql query that uses stored procedures to get the requests of a 
-- user

-- To create a MySQL query that uses stored procedures to get the orders of a user, you can use the following syntax:

-- Stored procedure to obtain orders from a user
DELIMITER //
CREATE PROCEDURE GetUserOrders(IN user_id INT)
BEGIN
SELECT o.OrderID, p.ProductName, o.OrderDate
FROM Orders o
JOIN Products p ON o.ProductID = p.ProductID
WHERE o.UserID = user_id;
END //
DELIMITER ;

-- Use of the stored procedure to obtain orders from user 1001
CALL GetUserOrders(1001);

-- Use of the stored procedure to obtain the user's orders 2002
CALL GetUserOrders(2002);

-- This code snippet demonstrates how to create a stored procedure that 
-- retrieves order information for specific users from a database, encapsulating 
-- the SQL logic to make it easy to manage and reuse in different parts of an 
-- application.


-- now generate a query to change the status of this order

-- To change the status of an order in a MySQL database, you can use the 
-- following query:

DELIMITER //
CREATE PROCEDURE UpdateOrderStatus(IN order_id INT, IN new_status VARCHAR(50))
BEGIN
UPDATE Orders
SET Status = new_status
WHERE OrderID = order_id;
END //
DELIMITER ;

-- This MySQL query creates a stored procedure named UpdateOrderStatus. It 
-- updates an order's status in the Orders table by taking two parameters: 
-- order_id, representing the ID of the order to be updated, and new_status, 
-- indicating the new status to be assigned. This query uses an UPDATE statement 
-- to modify the value of the Status field in the Orders table applied to the 
-- corresponding row.


-- generate a query to perform the deletion of this

-- To delete an order in a MySQL database, you can use the following query:

DELIMITER //
CREATE PROCEDURE DeleteOrder(IN order_id INT)
BEGIN
DELETE FROM Orders
WHERE OrderID = order_id;
END //
DELIMITER ;

-- This query creates a stored procedure called DeleteOrder that removes 
-- a row from the Orders table. The procedure takes one parameter, order_id, 
-- representing the ID of the order to be deleted.
-- generate a query that automatically generates a weekly report on the status 
-- of these
-- To generate a weekly report on the status of orders in a MySQL database, 
-- you can use the following query:

DELIMITER //
CREATE PROCEDURE GenerateWeeklyReportWithStatus(IN week_start DATE, IN week_end DATE)
BEGIN
SELECT
Status,
COUNT(*) AS OrderCount
-- Add other aggregate calculations here based on your actual table structure
FROM Orders
WHERE OrderDate BETWEEN week_start AND week_end
GROUP BY Status;
END //
DELIMITER ;

-- Example: Generate report for the week of August 1, 2023 to August 7, 2023
CALL GenerateWeeklyReportWithStatus('2023-08-01', '2023-08-07');

-- This query creates a stored procedure called GenerateWeeklyReportWithStatus. 
-- It generates a weekly report on order status. The procedure requires two input
-- parameters, week_start and week_end, which specify the report's timeframe.

-- The SELECT statement retrieves order statuses and their corresponding counts 
-- within a specified week interval. The Orders table is specified as the data 
-- source in the FROM clause, and the WHERE clause filters orders based on date 
-- to ensure they fall within the specified time interval. Finally, the results 
-- are grouped by order status.

-- Note: Add other aggregates to summarize additional job aspects based on your 
-- spreadsheet's actual structure. Finally, use the Sample Comment to call the 
-- procedure with specific parameters to generate a report for a particular week.

-- generate a query to record in an audit table each time the status of one of this 
-- changes
-- To keep track of changes to an order's status in a MySQL database, use this 
-- query to create an audit table:

DELIMITER //
CREATE PROCEDURE LogOrderStatusChange(IN order_id INT, IN old_status VARCHAR(50), IN new_status VARCHAR(50))
BEGIN
INSERT INTO AuditLog (OrderID, OldStatus, NewStatus)
VALUES (order_id, old_status, new_status);
END //
DELIMITER ;

-- This query creates a stored procedure named LogOrderStatusChange. It logs 
-- changes to the status of an order in the AuditLog table. The procedure takes 
-- three parameters: order_id, old_status, and new_status. The order_id parameter 
-- represents the ID of the order whose status is being changed, the old_status 
-- parameter represents the order's previous status, and the new_status parameter 
-- represents the order's new status.

-- The purpose of this query is to maintain an audit trail table that captures 
-- changes to the status of an order, allowing for tracking, troubleshooting, 
-- compliance, and auditing purposes. It also provides a detailed record of all 
-- actions taken in the database.