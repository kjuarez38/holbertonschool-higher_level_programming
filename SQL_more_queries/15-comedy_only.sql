-- 15.comedy_only.sql starts here
-- write a script that lists all Comedy shows in the database hbtn_0d_tvshows
SELECT g.`title`
  FROM `tv_shows` AS g
       INNER JOIN `tv_show_genres` AS s
       ON g.`id` = s.`show_id`

       INNER JOIN `tv_genres` AS t
       ON t.`id` = s.`genre_id`
       WHERE t.`name` = "Comedy"
 ORDER BY g.`title`;