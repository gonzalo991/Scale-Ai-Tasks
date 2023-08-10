-- Create the 'library' database
CREATE DATABASE IF NOT EXISTS library;
USE library;

-- Create the 'books' table
CREATE TABLE IF NOT EXISTS books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    genre VARCHAR(255) NOT NULL,
    publication_year INT,
    price DECIMAL(10, 2)
);

-- Insert book records into the 'books' table
INSERT INTO books (title, author, genre, publication_year, price) VALUES
    ('Harry Potter and the Sorcerer''s Stone', 'J.K. Rowling', 'Fantasy', 1997, 19.99),
    ('The Fellowship of the Ring', 'J.R.R. Tolkien', 'Fantasy', 1954, 15.99),
    ('A Game of Thrones', 'George R.R. Martin', 'Fantasy', 1996, 12.99),
    ('Strange Case of Dr Jekyll and Mr Hyde', 'Robert Louis Stevenson', 'Horror', 1886, 17.99),
    ('Hamlet', 'William Shakespeare', 'Drama', 1603, 22.99),
    ('Don Quijote de la Mancha', 'Miguel de Cervantes', 'Classic', 1605, 14.99),
    ('To Kill a Mockingbird', 'Harper Lee', 'Fiction', 1960, 16.99),
    ('1984', 'George Orwell', 'Dystopian', 1949, 13.99),
    ('The Great Gatsby', 'F. Scott Fitzgerald', 'Classic', 1925, 18.99),
    ('Pride and Prejudice', 'Jane Austen', 'Romance', 1813, 14.99);
