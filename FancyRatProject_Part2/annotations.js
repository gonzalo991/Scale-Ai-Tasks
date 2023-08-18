/**
generates a query that counts the total amount of "likes" given by a user on facebook in the "Likes" table
Here is an example query that calculates the total number of "likes" a user has given on Facebook, extracted from the "Likes" table:
```sql
SELECT SUM(likes) AS total_likes
FROM likes
WHERE user_id = 'user_id'
```
This query sums the number of likes for a user using the SUM function. User_id is a column in the "Likes" table that stores the ID of the user who gave the like.
generate a query to calculate the average number of comments per publication in this table
Here is an example query that calculates the average number of comments per publication in the "Comments" table:
```sql
SELECT AVG(ComentariosPorPublicacion) AS AverageComments
FROM (
SELECT COUNT(*) AS ComentariosPorPublicacion
FROM Comments
WHERE UserID = 'user_id'
GROUP BY PostID
) AS Subquery;
```
To find the average number of comments per post by a particular user, the SQL query provided is used. It uses a sub-query to count the number of comments for each individual post that is attributed to the user. This subquery effectively creates a count of comments for each post by selecting and grouping the comments based on their corresponding posts. This results in an average of comments for each post for a given set of users. This query makes it easy to assess the user's level of engagement. It also provides insight into the average interaction their posts generate through comments.
now generate a query that groups this by day and counts the number of daily publications
Here is an example query that groups the number of publications by day and counts the total number of publications:
```sql
SELECT date_trunc('day', publish_date) AS Day, COUNT(*) AS TotalPublications
FROM Publications
GROUP BY date_trunc('day', publish_date);
```
This query counts the number of publications per day by truncating the publish_date column to the day level using the date_trunc function.
based on this count, generate a query that groups them by category
Here is an example query that groups the number of daily publications grouped by category and counts the total number of publications:
```sql
SELECT date_trunc('day', publish_date) AS Day, category, COUNT(*) AS TotalPublications
FROM Publications
GROUP BY date_trunc('day', publish_date), category
ORDER BY Day, category;
```
This query will count daily publications by category, for analyzing distribution.
generate a query to identify the popular ones

Here is an example search query that shows the most popular categories based on daily publication count:
```sql
SELECT date_trunc('day', publish_date) AS Day, category, COUNT(*) AS TotalPublications
FROM Publications
GROUP BY date_trunc('day', publish_date), category
ORDER BY Day, category;
```
This query groups daily publications by category, counts them, and orders the results by day and category to identify popular categories based on daily publications.
 */



