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
