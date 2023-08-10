CREATE DATABASE SuperheroesDatabase;
USE SuperheroesDatabase;

CREATE TABLE DC (
superhero_id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100),
alias VARCHAR(100),
role VARCHAR(100),
race VARCHAR(100)
);

CREATE TABLE Marvel (
superhero_id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100),
alias VARCHAR(100),
role VARCHAR(100),
race VARCHAR(100)
);

CREATE TABLE Capcom (
superhero_id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100),
alias VARCHAR(100),
role VARCHAR(100),
race VARCHAR(100)
);

INSERT INTO DC (name, alias, role, race)
VALUES ('Superman', 'The Man of Steel', 'Superhero', 'Human'),
('Batman', 'The Dark Knight', 'Superhero', 'Human'),
('The Flash', 'The Scarlet Speedster', 'Superhero', 'Human'),
('Wonder Woman', 'The Amazon Princess', 'Superhero', 'Human');

INSERT INTO Marvel (name, alias, role, race)
VALUES ('Iron Man', 'The Invincible Iron Man', 'Superhero', 'Human'),
('Spider-Man', 'The Friendly Neighborhood Spider-Man', 'Superhero', 'Human'),
('The Hulk', 'The Green Goliath', 'Superhero', 'Human'),
('Black Widow', 'The Russian Spy', 'Superhero', 'Human');

INSERT INTO Capcom (name, alias, role, race)
VALUES ('Mega Man', 'The Blue Bomber', 'Superhero', 'Human'),
('Dante', 'The Devil Hunter', 'Superhero', 'Half-Demon'),
('Terry Bogard', 'The Legendary Wolf', 'Superhero', 'Human'),
('Chun-Li', 'The Strongest Woman in the World', 'Superhero', 'Human');

-- Add villains to DC table
INSERT INTO DC (name, alias, role, race)
VALUES ('Joker', 'The Clown Prince of Crime', 'Villain', 'Human'),
('Riddler', 'The Prince of Puzzles', 'Villain', 'Human'),
('Penguin', 'The Birdmaster of Crime', 'Villain', 'Human');

-- Add villains to Marvel table
INSERT INTO Marvel (name, alias, role, race)
VALUES ('Doctor Doom', 'The Master of Mystic Arts', 'Villain', 'Human'),
('Green Goblin', 'The Insanity Incarnate', 'Villain', 'Human'),
('Kingpin', 'The King of Crime', 'Villain', 'Human');

-- Add villains to Capcom table
INSERT INTO Capcom (name, alias, role, race)
VALUES ('Akuma', 'The Raging Demon', 'Villain', 'Human'),
('Wesker', 'The Mastermind', 'Villain', 'Human'),
('Sigma', 'The Maverick Overlord', 'Villain', 'Computer Virus');


USE SuperheroesDatabase;

-- Retrieve all superheroes from all tables
SELECT * FROM DC WHERE role = 'Superhero'
UNION ALL
SELECT * FROM Marvel WHERE role = 'Superhero'
UNION ALL
SELECT * FROM Capcom WHERE role = 'Superhero';

USE SuperheroesDatabase;

-- Retrieve all human villains from the Capcom table
SELECT * FROM Capcom WHERE role = 'Villain' AND race = 'Human';

USE SuperheroesDatabase;

-- Retrieve heroes and villains that are not humans from all tables
SELECT * FROM DC WHERE role IN ('Superhero', 'Villain') AND race != 'Human'
UNION ALL
SELECT * FROM Marvel WHERE role IN ('Superhero', 'Villain') AND race != 'Human'
UNION ALL
SELECT * FROM Capcom WHERE role IN ('Superhero', 'Villain') AND race != 'Human'

USE SuperheroesDatabase;

SELECT * FROM DC WHERE role = 'Superhero' AND name like '%man%'
UNION ALL
SELECT * FROM Marvel WHERE role = 'Superhero' AND name like '%man%'
UNION ALL
SELECT * FROM Capcom WHERE role = 'Superhero' AND name like '%man%'