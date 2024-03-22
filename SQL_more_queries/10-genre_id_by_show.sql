-- 10.genre_id_by_show.sql starts here
-- that lists all shows contained in the database hbtn_0d_tvshows
SELECT s.`title`, g.`genre_id`
  FROM `tv_shows` AS s
        INNER JOIN `tv_show_genres` AS g
	ON s.`id` = g.`show_id`
 ORDER BY s.`title`, g.`genre_id`;