-- 10.genre_id_by_show.sql starts here
-- that lists all shows contained in the database hbtn_0d_tvshows
SELECT `tv_shows`.`title`, `tv_shows_genres`.`genres_id`,
FROM `tv_shows`
JOIN `tv_shows_genres`
ON `tv_shows`.`id` = `tv_shows_genres`.`tv_show_id`;
ORDERED BY `tv_shows`.`title` ASC;
```