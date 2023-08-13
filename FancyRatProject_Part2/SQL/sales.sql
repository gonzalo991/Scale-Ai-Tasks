-- Calculate the average monthly sales for each year in the sales table.
-- Here is the average monthly sales for each year in the sales table:

WITH MonthlyAverageSales AS (
SELECT YEAR(sales_date) AS year, MONTH(sales_date) AS month, AVG(sales_amount) AS monthly_average
FROM sales
GROUP BY year, month
)
SELECT year, month, monthly_average
FROM MonthlyAverageSales;

-- In a sales table, this query calculates the average monthly sales over several years and months. The temporary 
-- table 'MonthlyAverageSales' groups the sales by year and month, computes the average sales and displays the resultant 
-- year, month and month average.

-- generates a query to calculate the month with the highest and lowest average sales in each year
-- Here is a query to calculate the month with the highest and lowest average sales in each year:

WITH MonthlyAverageSales AS (
SELECT YEAR(sales_date) AS year,
MONTH(sales_date) AS month,
AVG(sales_amount) AS monthly_average
FROM sales
GROUP BY YEAR(sales_date), MONTH(sales_date)
)
SELECT mas_max.year,
mas_max.month AS max_month,
mas_max.monthly_average AS max_monthly_average,
mas_min.month AS min_month,
mas_min.monthly_average AS min_monthly_average
FROM (
SELECT year,
MAX(monthly_average) AS max_avg
FROM MonthlyAverageSales
GROUP BY year
) max_subquery
JOIN MonthlyAverageSales mas_max ON max_subquery.year = mas_max.year AND max_subquery.max_avg = mas_max.monthly_average
JOIN (
SELECT year,
MIN(monthly_average) AS min_avg
FROM MonthlyAverageSales
GROUP BY year
) min_subquery
JOIN MonthlyAverageSales mas_min ON min_subquery.year = mas_min.year AND min_subquery.min_avg = mas_min.monthly_average
WHERE mas_max.year = mas_min.year
ORDER BY mas_max.year;

-- This query computes the average maximum and minimum turnover for each year and merges it with the original data.
-- extend this query to include sales details to show the quantity sold and the amount in the months with the highest and 
-- lowest sales
-- Here is the extended query that includes the quantity sold and the amount in the months with the highest and lowest sales:

WITH MonthlyAverageSales AS (
SELECT YEAR(sales_date) AS year,
MONTH(sales_date) AS month,
AVG(sales_amount) AS monthly_average,
COUNT(DISTINCT sales_id) AS quantity_sold
FROM sales
GROUP BY year, month
)
SELECT mas_max.year,
mas_max.month AS max_month,
mas_max.quantity_sold AS max_quantity_sold,
mas_max.monthly_average AS max_monthly_average,
mas_min.month AS min_month,
mas_min.quantity_sold AS min_quantity_sold,
mas_min.monthly_average AS min_monthly_average
FROM (
SELECT year,
MAX(quantity_sold) AS max_quantity,
MAX(monthly_average) AS max_avg
FROM MonthlyAverageSales
GROUP BY year
) max_subquery
JOIN MonthlyAverageSales mas_max ON max_subquery.year = mas_max.year AND max_subquery.max_quantity = mas_max.quantity_sold AND max_subquery.max_avg = mas_max.monthly_average
JOIN (
SELECT year,
MIN(quantity_sold) AS min_quantity,
MIN(monthly_average) AS min_avg
FROM MonthlyAverageSales
GROUP BY year
) min_subquery
JOIN MonthlyAverageSales mas_min ON min_subquery.year = mas_min.year AND min_subquery.min_quantity = mas_min.quantity_sold AND min_subquery.min_avg = mas_min.monthly_average
WHERE mas_max.year = mas_min.year
ORDER BY mas_max.year;

-- This query extends the previous query by adding the quantity_sold column to the results.
-- The quantity_sold column was added to the MonthlyAverageSales temporary table. The quantity_sold column was then 
-- added to the results of the query. The quantity_sold column is included in the final results, along with the year, month, 
-- quantity_sold, and monthly_average columns.

-- This query calculates the average monthly sales and the number of unique sales for each year and month in the sales table 
-- using a temporary table called MonthlyAverageSales. By combining these statistics, we can find the months with the highest 
-- and lowest sales in each year, as well as their monthly average.

-- In the temporary table, it selects the year and month from the sales_date column, calculates the average monthly sales and 
-- the number of unique sales, and then groups them by year and month.

-- A max_subquery is created in the main query. This calculates the maximum monthly average sales and the maximum number of 
-- sales for each year. It performs a join on the time table using the year, the maximum sales amount and the maximum monthly average to get the details of the months with the maximum sales.

-- In a similar way, a further min_subquery subquery is created to calculate the minimum average monthly sales amount and 
-- the minimum number of unique sales for each year.

-- We then select relevant information, e.g. year, month with highest and lowest turnover, number of single transactions 
-- and corresponding monthly average.


-- i want to compare the average sales in the months with the highest and lowest number of individual sales in this table

-- Here is the query to compare the average sales in the months with the highest and lowest number of individual sales:

WITH MonthlyIndividualSales AS (
SELECT YEAR(sales_date) AS year,
MONTH(sales_date) AS month,
AVG(sales_amount) AS monthly_average,
COUNT(DISTINCT sales_id) AS quantity_sold,
RANK() OVER (PARTITION BY YEAR(sales_date) ORDER BY COUNT(DISTINCT sales_id) DESC) AS max_rank,
RANK() OVER (PARTITION BY YEAR(sales_date) ORDER BY COUNT(DISTINCT sales_id) ASC) AS min_rank
FROM sales
GROUP BY year, month
)
SELECT year,
MAX(CASE WHEN max_rank = 1 THEN month END) AS max_sales_month,
MAX(CASE WHEN max_rank = 1 THEN monthly_average END) AS max_monthly_average,
MAX(CASE WHEN min_rank = 1 THEN month END) AS min_sales_month,
MAX(CASE WHEN min_rank = 1 THEN monthly_average END) AS min_monthly_average
FROM MonthlyIndividualSales
WHERE max_rank = 1 OR min_rank = 1
GROUP BY year
ORDER BY year;

-- This query uses a common table expression (CTE) to calculate the average sales and the number of individual sales for 
-- each month. It then uses the RANK() function to rank the months based on the number of individual sales. Finally, it 
-- selects the months with the highest and lowest number of individual sales and their corresponding average sales.

