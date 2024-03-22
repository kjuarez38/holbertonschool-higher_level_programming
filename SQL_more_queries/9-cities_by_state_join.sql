-- 9.cities_by_state_join.sql starts here
-- that lists all the cities of the database hbtn_0d_usa
SELECT `cities`.`id`, `cities`.`name`, `states`.`name`
FROM `cities`
JOIN `states`
ON `cities`.`state_id` = `states`.`id`