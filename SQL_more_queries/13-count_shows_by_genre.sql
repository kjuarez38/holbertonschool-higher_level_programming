-- 13.count_shows_by_genre.sql starts here
-- Write a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT g.`name`, 
    COUNT(*) AS `number_of_shows`
  FROM `tv_genres` AS g
        INNER JOIN `tv_shows_genres` AS s
        ON g.`id` = s.`genre_id`
 GROUP BY g.`name`
 ORDER BY number_of_shows DESC;