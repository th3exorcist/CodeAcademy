SELECT DISTINCT year FROM movies;  

SELECT name,
 CASE
  WHEN genre = 'romance' THEN 'Chill'
  WHEN genre = 'comedy'  THEN 'Chill'
  ELSE 'Intense'
 END AS 'Mood'
FROM movies;

SELECT DISTINCT name
FROM babies
WHERE name LIKE 'S%'
LIMIT 20;
