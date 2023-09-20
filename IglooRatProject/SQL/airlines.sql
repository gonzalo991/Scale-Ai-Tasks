-- Create the flight reservation database
CREATE DATABASE FlightReservations;

-- Use the newly created database
USE FlightReservations;

-- Create the table for flights
CREATE TABLE flights (
    id_flight INT AUTO_INCREMENT PRIMARY KEY,
    origin VARCHAR(255),
    destination VARCHAR(255),
    departure_date DATE,
    arrival_date DATE,
    capacity INT,
    price DECIMAL(10, 2)
);

-- Create the table for passengers
CREATE TABLE passengers (
    id_passenger INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email VARCHAR(255)
);

-- Create the table for reservations
CREATE TABLE reservations (
    id_reservation INT AUTO_INCREMENT PRIMARY KEY,
    id_flight INT,
    id_passenger INT,
    reservation_date DATETIME,
    FOREIGN KEY (id_flight) REFERENCES flights(id_flight),
    FOREIGN KEY (id_passenger) REFERENCES passengers(id_passenger)
);

-- Insert some sample data
INSERT INTO flights (origin, destination, departure_date, arrival_date, capacity, price)
VALUES ('New York', 'Los Angeles', '2023-10-01', '2023-10-05', 150, 300.00),
       ('Chicago', 'Miami', '2023-09-25', '2023-09-30', 120, 250.00);

INSERT INTO passengers (first_name, last_name, email)
VALUES ('John', 'Doe', 'john.doe@example.com'),
       ('Jane', 'Smith', 'jane.smith@example.com');

INSERT INTO reservations (id_flight, id_passenger, reservation_date)
VALUES (1, 1, '2023-08-15 10:30:00'),
       (2, 2, '2023-08-20 15:45:00');

-- Insert more sample data into the flights table
INSERT INTO flights (origin, destination, departure_date, arrival_date, capacity, price)
VALUES ('San Francisco', 'Seattle', '2023-10-10', '2023-10-14', 100, 220.00),
       ('Los Angeles', 'Las Vegas', '2023-09-28', '2023-09-30', 80, 150.00),
       ('Miami', 'Orlando', '2023-10-05', '2023-10-07', 90, 180.00);

-- Insert more sample data into the passengers table
INSERT INTO passengers (first_name, last_name, email)
VALUES ('Michael', 'Johnson', 'michael.j@example.com'),
       ('Emily', 'Brown', 'emily.b@example.com'),
       ('Daniel', 'Davis', 'daniel.d@example.com');

-- Insert more sample data into the reservations table
INSERT INTO reservations (id_flight, id_passenger, reservation_date)
VALUES (3, 3, '2023-08-22 09:15:00'),
       (4, 4, '2023-08-25 18:30:00'),
       (5, 5, '2023-08-28 14:45:00');
       
SELECT f.id_flight, COUNT(r.id_reservation) AS total_reservations
FROM flights f
LEFT JOIN reservations r ON f.id_flight = r.id_flight
GROUP BY f.id_flight;

SELECT SUM(f.price) AS total_revenue
FROM flights f
JOIN reservations r ON f.id_flight = r.id_flight;

SELECT COUNT(id_reservation) AS total_reservations
FROM reservations
WHERE DATE_FORMAT(reservation_date, '%Y-%m') = '2023-01';

SELECT AVG(price) AS average_price
FROM flights
WHERE MONTH(departure_date) = 10;

