-- generate a mysql query that calculates the percentage change of the stock 
-- price in the trading table from the first day based on the initial price

-- Here is a MySQL query that calculates the percentage change of the stock 
-- price in the trading table from the first day based on the initial price:

SELECT Date, StockPrice,
(StockPrice - FIRST_VALUE(StockPrice) OVER (ORDER BY Date)) / FIRST_VALUE(StockPrice) OVER (ORDER BY Date) * 100 AS PercentageChange
FROM Trading;

-- In this query, we use the FIRST_VALUE() function with the OVER (ORDER BY Date) 
-- window frame to determine the initial stock price. Then, we calculate the 
-- percentage change for each subsequent trading day by subtracting the initial 
-- price from the current day's price, dividing by the initial price, and 
-- multiplying by 100.

-- now i want a query to calculate the percentage return of different stocks in 
-- a given period, comparing their initial prices with the current prices

-- Here is a MySQL query that calculates the percentage return of different 
-- stocks in a given period, comparing their initial prices with the current prices:

SELECT
StockSymbol,
FIRST_VALUE(StockPrice) OVER (PARTITION BY StockSymbol ORDER BY TradeDate) AS InitialPrice,
LAST_VALUE(StockPrice) OVER (PARTITION BY StockSymbol ORDER BY TradeDate ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS CurrentPrice,
((LAST_VALUE(StockPrice) OVER (PARTITION BY StockSymbol ORDER BY TradeDate ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) - FIRST_VALUE(StockPrice) OVER (PARTITION BY StockSymbol ORDER BY TradeDate)) / FIRST_VALUE(StockPrice) OVER (PARTITION BY StockSymbol ORDER BY TradeDate)) * 100 AS PercentageChange
FROM
TradingTable
WHERE
TradeDate BETWEEN '2023-01-01' AND '2023-06-30';

-- The purpose of this query is the calculation of the percentage change in the 
-- share price of different stocks over a certain period of time. Information 
-- about the transactions, including the stock symbol, the date of the 
-- transaction and the price of the stock at that time, is stored in the 
-- TradingTable table.

-- It returns three values per stock: 'InitialPrice' is stock's price on first 
-- day of period; 'CurrentPrice' is stock's price on last day of period; 
-- and 'PercentageChange' is percentage change between initial price and current 
-- price.

-- This is achieved by means of the window functions FIRST_VALUE() and 
-- LAST_VALUE(), which return the first and last values of a window defined 
-- by the order of the dates. These functions are grouped according to the 
-- action symbol and sorted according to the date of the transaction. The 
-- formula for the percentage change is then calculated. The difference between 
-- the current price and the initial price is divided by the initial price and 
-- multiplied by 100 to give the percentage change. The query filters out 
-- transactions that occurred between 1 January 2023 and 30 June 2023, thus 
-- limiting the period of analysis.


-- i want a query to identify the stock that had the highest initial price in 
-- a selected period
-- Here is a MySQL query that identifies the stock that had the highest initial 
-- price in a selected period:

SELECT StockSymbol, InitialPrice
FROM (
SELECT StockSymbol, StockPrice AS InitialPrice, TradeDate
FROM TradingTable
WHERE TradeDate BETWEEN '2023-01-01' AND '2023-06-30'
AND TradeDate = (
SELECT MIN(TradeDate)
FROM TradingTable t
WHERE t.StockSymbol = TradingTable.StockSymbol
AND t.TradeDate BETWEEN '2023-01-01' AND '2023-06-30'
)
) InitialPrices
ORDER BY InitialPrice DESC
LIMIT 1;

-- This query finds the highest opening price within a specified period. It 
-- does so by first using a subquery to find the minimum date traded within 
-- the specified period. This sub-query acts as a filter to determine the 
-- starting point of the analysis, then the external query retrieves the stock 
-- symbol and corresponding stock price on that initial trading date.

-- The list will then descend from the highest bid to the lowest bid. The LIMIT 1
-- clause ensures that only one row is returned. This row corresponds to the stock with the highest starting price.
-- generate a query to identify the stock with the lowest initial price in the 
-- same period


-- Here is a MySQL query that identifies the stock with the lowest initial price 
-- in the same period:

SELECT StockSymbol, InitialPrice
FROM (
SELECT StockSymbol, StockPrice AS InitialPrice, TradeDate
FROM TradingTable
WHERE TradeDate BETWEEN '2023-01-01' AND '2023-06-30'
AND TradeDate = (
SELECT MIN(TradeDate)
FROM TradingTable t
WHERE t.StockSymbol = TradingTable.StockSymbol
AND t.TradeDate BETWEEN '2023-01-01' AND '2023-06-30'
)
) InitialPrices
ORDER BY InitialPrice ASC
LIMIT 1;

-- This query identifies the stock with the lowest opening price within a 
-- specified time period. It starts by retrieving the stock symbols, initial 
-- prices and trade dates of the stocks that traded on the earliest date within 
-- the specified time period using a subquery in the FROM clause. The subquery 
-- filters the results based on the condition that the trade date is the same as 
-- the minimum trade date for each of the specific stocks within the specified 
-- time period.

-- From the results of the subquery, the outer query then retrieves the stock 
-- symbol and initial price. It then uses the ORDER BY clause with ASC to order 
-- these results in ascending order of opening price. Finally, the LIMIT 1 
-- clause is used to limit the output to just one row. This row represents the 
-- stock with the lowest opening price in the specified time period.

-- generate a query to calculate the difference between the current price and 
-- the initial price for each one
-- Here is a MySQL query that calculates the difference between the current 
-- price and the initial price for each stock in the trading table:

SELECT StockSymbol,
(LAST_VALUE(StockPrice) OVER (PARTITION BY StockSymbol ORDER BY TradeDate ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) - FIRST_VALUE(StockPrice) OVER (PARTITION BY StockSymbol ORDER BY TradeDate)) AS PriceChange
FROM TradingTable
WHERE TradeDate BETWEEN '2023-01-01' AND '2023-06-30';

-- This query calculates the difference between the current price and the price 
-- at which each stock in the trade table was first traded. It retrieves the 
-- current price and the starting price. The window frame is defined by the 
-- TradeDate column, which is sorted in ascending order. Next, the query 
-- subtracts the start price from the current price to calculate the price change.

-- Finally, the results are grouped by StockSymbol and sorted in ascending 
-- order by TradeDate. The difference between the current price and the opening 
-- price of each stock is shown in the PriceChange column.