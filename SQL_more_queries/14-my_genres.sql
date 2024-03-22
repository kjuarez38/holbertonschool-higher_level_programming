-- 14.my_genres.sql starts here
-- write a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT g.`name`
  FROM `tv_genres` AS g
      INNER JOIN `tv_show_genres` AS t
      ON g.`id` = t.`genre_id`

      INNER JOIN `tv_shows` AS s
      ON t.`show_id` = s.`id`
      WHERE s.`title` = 'Dexter'
  ORDERED BY g.`name`;