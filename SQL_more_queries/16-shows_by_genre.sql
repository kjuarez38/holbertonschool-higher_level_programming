-- 15.comedy_only.sql starts here
-- write a script that lists all Comedy shows in the database hbtn_0d_tvshows
SELECT s.`title`, t.`name`
  FROM `tv_shows` AS s
       LEFT JOIN `tv_show_genres` AS g
       ON g.`id` = g.`show_id`

       LEFT JOIN `tv_genres` AS t
       ON t.`id` = g.`genre_id`
 ORDER BY s.`title`;