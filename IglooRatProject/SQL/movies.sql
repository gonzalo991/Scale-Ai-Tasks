CREATE DATABASE movie_recommendations_db;

USE movie_recommendations_db;

CREATE TABLE movies (
    movie_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    category VARCHAR(255)
);

INSERT INTO movies (title, category) VALUES
    ('Movie 1', 'Action'),
    ('Movie 2', 'Drama'),
    ('Movie 3', 'Comedy'),
    ('Movie 4', 'Action'),
    ('Movie 5', 'Comedy');

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL
);

INSERT INTO users (username) VALUES
    ('User1'),
    ('User2'),
    ('User3');

CREATE TABLE interactions (
    interaction_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    movie_id INT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users (user_id),
    FOREIGN KEY (movie_id) REFERENCES movies (movie_id)
);

INSERT INTO interactions (user_id, movie_id) VALUES
    (1, 1),
    (1, 2),
    (2, 1),
    (3, 3),
    (3, 4),
    (3, 5);

CREATE TABLE ratings (
    rating_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    movie_id INT NOT NULL,
    rating INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (user_id),
    FOREIGN KEY (movie_id) REFERENCES movies (movie_id)
);

INSERT INTO ratings (user_id, movie_id, rating) VALUES
    (1, 1, 4),
    (1, 2, 3),
    (2, 1, 5),
    (3, 3, 4),
    (3, 4, 2),
    (3, 5, 5);
    
SELECT movies.title, COUNT(interactions.interaction_id) AS interaction_count
FROM movies
JOIN interactions ON movies.movie_id = interactions.movie_id
GROUP BY movies.title
ORDER BY interaction_count DESC
LIMIT 1;


SELECT movies.title, COUNT(ratings.rating_id) AS rating_count
FROM movies
JOIN ratings ON movies.movie_id = ratings.movie_id
GROUP BY movies.title
ORDER BY rating_count DESC;

SELECT movies.title, AVG(ratings.rating) AS avg_rating
FROM movies
JOIN ratings ON movies.movie_id = ratings.movie_id
GROUP BY movies.title
ORDER BY avg_rating DESC;


SELECT m.title, AVG(r.rating) AS average_rating
FROM movies m
LEFT JOIN ratings r ON m.movie_id = r.movie_id
GROUP BY m.title
HAVING AVG(r.rating) >= 3.5
ORDER BY average_rating DESC;

SELECT m.movie_id, m.title, COUNT(i.user_id) AS popularity
FROM movies m
JOIN interactions i ON m.movie_id = i.movie_id
WHERE i.timestamp >= NOW() - INTERVAL 7 DAY
GROUP BY m.movie_id
ORDER BY popularity DESC;

