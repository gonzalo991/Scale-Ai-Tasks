--taking into account a table called credit_cards where the customer's credit card information is 
-- stored and a table called transactions for the operations performed with it, create a query to 
-- calculate the outstanding balance of a specific customer's credit card

--Here is a sample query to calculate the outstanding balance of a specific customer's credit card 
--using the credit_cards and transactions tables:

SELECT c.card_number, c.credit_limit - COALESCE(SUM(t.amount), 0) AS outstanding_balance
FROM credit_cards c
LEFT JOIN transactions t ON c.card_id = t.card_id
WHERE c.customer_id = <customer_id>
GROUP BY c.card_number, c.credit_limit;

-- In this query we selected the card number and calculated the outstanding balance as the 
-- difference between the card's credit limit and the sum of the customer's transactions. We used 
-- the COALESCE function to handle cases where there were no transactions, in which case we used 0 as 
-- the default value.

-- We then performed a left join on the transactions table, using the card id as the join key 
-- to combine the cards and their corresponding transactions. We then filtered the rows by id and 
-- grouped the results by card number and credit limit.


-- generate a query that calculates the total payments made on each

-- Here is a sample query to calculate the total payments made on each credit card using the 
-- credit_cards and transactions tables:

SELECT c.card_number, SUM(t.amount) AS total_payments
FROM credit_cards c
LEFT JOIN transactions t ON c.card_id = t.card_id
GROUP BY c.card_number;

-- In this query, we selected the card number and calculated the total payments made as the sum 
-- of the amounts of the transactions. We then performed a left join on the transactions table, using 
-- the card id as the join key to combine the cards and their corresponding transactions. We then 
-- grouped the results by card number.

-- The purpose of this query is to give a consolidated view of each customer's total credit card payments. 
-- This enables analysts and managers at a bank or financial institution to gain a better understanding 
-- of the credit card usage and behaviour of their customers, as well as to identify spending patterns 
-- and trends in card payments.


-- create a query to calculate the amount of debt that has accumulated in all over a given period of time


--Here is a sample query to calculate the amount of debt that has accumulated over a given period 
-- of time using the credit_cards and transactions tables:

SELECT c.card_number, SUM(t.amount) AS debt_accumulation
FROM credit_cards c
LEFT JOIN transactions t ON c.card_id = t.card_id
WHERE t.transaction_date >= '2023-01-01'
GROUP BY c.card_number;

-- In this query, we selected the card number and calculated the debt accumulation as the sum of 
-- the amounts of the transactions for each card. We then performed a left join on the transactions 
-- table, using the card id as the join key to combine the cards and their corresponding transactions. We 
-- then filtered the results by card number and grouped the results by card number.

-- The purpose of this query is to give a consolidated view of each customer's debt accumulation over 
-- a given period of time. This enables analysts and managers at a bank or financial institution to better 
-- understand their customers' credit card usage and behavior and identify spending patterns and trends 
-- in card payments.


-- generates a query to calculate the average monthly expense for each customer


-- Here is a sample query to calculate the average monthly expense for each customer using the 
-- credit_cards and transactions tables:

SELECT c.customer_id,
YEAR(t.transaction_date) AS transaction_year,
MONTH(t.transaction_date) AS transaction_month,
AVG(t.amount) AS average_monthly_expense
FROM credit_cards c
LEFT JOIN transactions t ON c.card_id = t.card_id
WHERE t.transaction_date >= '2023-01-01'
GROUP BY c.customer_id, YEAR(t.transaction_date), MONTH(t.transaction_date);

-- In this query, we selected the customer ID, calculated the average monthly expense of each 
-- customer, performed a left join on the transactions table using the card ID as the join key, 
-- and then filtered and grouped the results by customer ID.

-- The purpose of this query is to provide a clear overview of each customer's average monthly 
-- credit card expenses. This helps analysts and managers at financial institutions to understand 
-- customers' behavior better and identify spending patterns and trends in card payments.


-- generate a query to identify who have exceeded their limit

-- Here is a sample query to identify customers who have exceeded their credit card limit using 
-- the credit_cards and transactions tables:

SELECT c.card_number, c.credit_limit, SUM(t.amount) as total_amount
FROM credit_cards c
LEFT JOIN transactions t ON c.card_id = t.card_id
GROUP BY c.card_number, c.credit_limit
HAVING c.credit_limit < total_amount;

-- In this query, we selected the card number and credit limit, and the amount of the transactions. We 
-- then performed a left join on the transactions table, using the card id as the join key to combine the cards and their corresponding transactions. We then filtered the results by credit limit and grouped the results by card number.

-- The query aims to identify credit card customers who surpass their limit and are at risk of 
-- payment default, allowing banks to offer extra assistance.