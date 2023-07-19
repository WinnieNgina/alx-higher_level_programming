-- lists all the cities of California that can be found in the database hbtn_0d_usa.
-- Use select to retrieve all columns from cities table

SELECT `id`, `name`
FROM cities
WHERE `state_id` IN (
SELECT id
FROM states
WHERE `name` = 'California'
)
ORDER BY id;

