-- Create the students database if it doesn't exist
CREATE DATABASE IF NOT EXISTS students_db;

-- Use the students database
USE students_db;

-- Create the students_data table
CREATE TABLE students_data (
  student_id INT AUTO_INCREMENT PRIMARY KEY,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  age INT NOT NULL,
  course VARCHAR(255) NOT NULL,
  section VARCHAR(255) NOT NULL
);

-- Insert data into the students_data table to create students
INSERT INTO students_data (first_name, last_name, age, course, section)
VALUES
  ('John', 'Doe', 20, 'Computer Science', 'A'),
  ('Jane', 'Smith', 22, 'Engineering', 'B'),
  ('Michael', 'Johnson', 19, 'Mathematics', 'C'),
  ('Emily', 'Brown', 21, 'Physics', 'D'),
  ('William', 'Davis', 20, 'Biology', 'E');
  
  SELECT * FROM students_data;
  
  
