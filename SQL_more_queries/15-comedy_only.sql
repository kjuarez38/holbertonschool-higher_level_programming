-- 14.my_genres.sql starts here
-- write a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT g.`name`
  FROM `tv_shows` AS g
       INNER JOIN `tv_show_genres` AS s
       ON g.`id` = s.`genre_id`

       INNER JOIN `tv_genres` AS t
       ON t.`id` = s.`genre_id`
       WHERE t.`name` = "Comedy"
 ORDER BY g.`title`;