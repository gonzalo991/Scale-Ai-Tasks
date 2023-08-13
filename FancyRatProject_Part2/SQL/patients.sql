-- create database
CREATE DATABASE patient_database;

USE patient_database;

CREATE TABLE patients (
    patient_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INT,
    gender VARCHAR(10)
);

CREATE TABLE appointments (
    appointment_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT,
    appointment_date DATE,
    doctor_name VARCHAR(50),
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
);

INSERT INTO patients (first_name, last_name, age, gender)
VALUES
    ('Juan', 'Pérez', 30, 'Male'),
    ('María', 'González', 25, 'Female'),
    ('Luis', 'Martínez', 40, 'Male'),
    ('Ana', 'López', 28, 'Female'),
    ('Carlos', 'Rodríguez', 45, 'Male'),
    ('Laura', 'Fernández', 35, 'Female');

INSERT INTO appointments (patient_id, appointment_date, doctor_name)
VALUES
    (1, '2023-08-10', 'Dr. Murphy'),
    (2, '2023-08-15', 'Dra. Grey'),
    (3, '2023-08-20', 'Dr. Rodriguez')