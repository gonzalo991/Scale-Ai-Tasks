-- Create a new database (if it doesn't exist)
CREATE DATABASE IF NOT EXISTS supermarket_db;

-- Use the new database
USE supermarket_db;

-- Create a table for products
CREATE TABLE products (
  product_id INT AUTO_INCREMENT PRIMARY KEY,
  product_name VARCHAR(255) NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  stock_quantity INT NOT NULL
);

-- Create a table for sales
CREATE TABLE sales (
  sale_id INT AUTO_INCREMENT PRIMARY KEY,
  sale_date DATE NOT NULL,
  product_id INT NOT NULL,
  quantity_sold INT NOT NULL,
  total_amount DECIMAL(10, 2) NOT NULL,
  FOREIGN KEY (product_id) REFERENCES products (product_id)
);

-- Insert sample data into the 'products' table
INSERT INTO products (product_name, price, stock_quantity)
VALUES
  ('Product A', 10.99, 100),
  ('Product B', 5.99, 50),
  ('Product C', 7.49, 75);

-- Insert sample data into the 'sales' table
INSERT INTO sales (sale_date, product_id, quantity_sold, total_amount)
VALUES
  ('2023-01-01', 1, 5, 54.95),
  ('2023-01-01', 2, 10, 59.90),
  ('2023-01-02', 1, 2, 21.98);
  
  -- Create a table for categories
CREATE TABLE categories (
  category_id INT AUTO_INCREMENT PRIMARY KEY,
  category_name VARCHAR(255) NOT NULL
);

-- Insert sample data into the 'categories' table
INSERT INTO categories (category_name)
VALUES
  ('Category X'),
  ('Category Y'),
  ('Category Z');

-- Calculate the total revenue for each day, including days with no sales
SELECT
  d.date,
  COALESCE(SUM(s.total_amount), 0) AS total_revenue
FROM (
  SELECT DISTINCT sale_date AS date FROM sales
  UNION ALL
  SELECT CURDATE() -- Add current date to include days with no sales
) AS d
LEFT JOIN sales s ON d.date = s.sale_date
GROUP BY d.date
ORDER BY d.date;


SELECT
  all_dates.date,
  COALESCE(SUM(s.total_amount), 0) AS total_revenue
FROM (
  SELECT DISTINCT sale_date AS date FROM sales
  UNION ALL
  SELECT CURDATE() -- Add current date to include days with no sales
) AS all_dates
LEFT JOIN sales s ON all_dates.date = s.sale_date
GROUP BY all_dates.date
ORDER BY all_dates.date;

SELECT AVG(quantity_sold) AS avg_products_per_transaction
FROM sales;


SELECT
  p.product_name,
  SUM(p.price * s.quantity_sold) AS total_cost
FROM products p
JOIN sales s ON p.product_id = s.product_id
GROUP BY p.product_name
ORDER BY total_cost DESC
LIMIT 1;


SELECT
  c.category_name,
  AVG(s.quantity_sold * p.price) AS avg_sales_per_category
FROM sales s
JOIN products p ON s.product_id = p.product_id
JOIN categories c ON p.category_id = c.category_id
GROUP BY c.category_name;

-- LEAD FUNCTION

-- Retrieve the next sale date for each product
SELECT
  product_id,
  sale_date AS current_sale_date,
  LEAD(sale_date) OVER (PARTITION BY product_id ORDER BY sale_date) AS next_sale_date
FROM sales;

-- Calculate the time interval (in days) between consecutive sales for each product

SELECT
  product_id,
  sale_date AS current_sale_date,
  LEAD(sale_date) OVER (PARTITION BY product_id ORDER BY sale_date) AS next_sale_date,
  DATEDIFF(
    LEAD(sale_date) OVER (PARTITION BY product_id ORDER BY sale_date),
    sale_date
  ) AS days_between_sales
FROM sales;

-- Find the product that had the highest quantity increase in consecutive sales

SELECT
  product_id,
  quantity_sold AS current_quantity,
  LEAD(quantity_sold) OVER (PARTITION BY product_id ORDER BY sale_date) AS next_quantity
FROM sales
ORDER BY product_id, (next_quantity - quantity_sold) DESC
LIMIT 1;

-- Determine the products that are out of stock and their expected restock date

SELECT
  product_id,
  product_name,
  stock_quantity AS current_stock,
  LEAD(sale_date) OVER (PARTITION BY product_id ORDER BY sale_date) AS restock_date
FROM products
LEFT JOIN sales ON products.product_id = sales.product_id
WHERE stock_quantity = 0;

-- Calculate the percentage change in price for each product

SELECT
  product_id,
  price AS current_price,
  LEAD(price) OVER (PARTITION BY product_id ORDER BY sale_date) AS next_price,
  ROUND(((next_price - price) / price) * 100, 2) AS price_change_percentage
FROM sales
JOIN products ON sales.product_id = products.product_id;

-- Find the products that have experienced a price decrease

SELECT DISTINCT
  product_id,
  product_name
FROM (
  SELECT
    product_id,
    price AS current_price,
    LEAD(price) OVER (PARTITION BY product_id ORDER BY sale_date) AS next_price
  FROM sales
  JOIN products ON sales.product_id = products.product_id
) AS price_changes
WHERE next_price < current_price;


-- Identify the products with decreasing sales quantities

SELECT DISTINCT
  product_id,
  product_name
FROM (
  SELECT
    product_id,
    quantity_sold AS current_quantity,
    LEAD(quantity_sold) OVER (PARTITION BY product_id ORDER BY sale_date) AS next_quantity
  FROM sales
  JOIN products ON sales.product_id = products.product_id
) AS quantity_changes
WHERE next_quantity < current_quantity;


-- Calculate the total revenue for each product and its percentage contribution to the category's revenue

SELECT
  product_id,
  product_name,
  total_amount AS current_revenue,
  LEAD(total_amount) OVER (PARTITION BY product_id ORDER BY sale_date) AS next_revenue,
  (total_amount / SUM(total_amount) OVER (PARTITION BY category_id)) * 100 AS percentage_contribution
FROM sales
JOIN products ON sales.product_id = products.product_id
JOIN categories ON products.category_id = categories.category_id;








