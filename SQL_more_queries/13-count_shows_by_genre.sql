-- 13.count_shows_by_genre.sql starts here
-- Write a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT g.`id`, g.`name`, 
    COUNT(s.`id`) AS `number_of_shows`
  FROM `genres` AS g
        INNER JOIN `shows` AS s
        ON g.`id` = s.`genre_id`
 GROUP BY g.`name`
 ORDER BY number_of_shows DESC, g.`name`;