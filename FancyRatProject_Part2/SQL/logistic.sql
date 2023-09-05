-- considering that we are operating on a database of a logistics company, 
-- we want to generate a report on inventory turnover using microsoft sql server
SELECT
    product_name,
    SUM(quantity_sold) AS total_quantity_sold,
    AVG(unit_price) AS average_unit_price,
    (SUM(quantity_sold) * AVG(unit_price)) AS total_inventory_turnover
FROM
    inventory_transactions
WHERE
    date_sold BETWEEN '2023-01-01' AND '2023-12-31'
GROUP BY
    product_name
ORDER BY
    total_inventory_turnover DESC;