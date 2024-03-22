-- 8.cities_of_california_subquery.sql creates a subquery
-- that lists all the cities of the state of California that can be found in the database hbtn_0d_usa
SELECT `id`, `name`
FROM `cities`
WHERE `state_id` = (SELECT `id` FROM `states` WHERE `name` = 'California');
