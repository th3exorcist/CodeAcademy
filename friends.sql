CREATE table friends(id INTEGER, name TEXT, birthday DATE);

INSERT INTO friends(id, name, birthday)
VALUES(1, 'Jane Doe', '05-30-1990');

SELECT * 
FROM friends;

UPDATE friends
SET name = 'Jane Smith'
WHERE id=1;

ALTER TABLE friends
ADD COLUMN email TEXT;

INSERT INTO friends (email)
VALUES('jane@codeacademy.com')
WHERE id = 1;

UPDATE friends
SET email = 'jane@codecademy.com'
WHERE id = 1;

SELECT*
FROM friends
