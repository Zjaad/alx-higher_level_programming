-- lists  all shows from hbtn_0d_tvshows_rate by their rating.
SELECT tv_shows.title, SUM(tv_shows_rate.rating) as rating_sum
FROM tv_shows
LEFT JOIN tv_shows_rate ON tv_shows.id = tv_shows_rate.show_id
GROUP BY tv_shows.title
ORDER BY rating_sum DESC;

SELECT g.`name` AS `genre`, SUM(r.`rate`) AS `rating`
FROM `tv_genres` AS g
INNER JOIN `tv_show_genres` AS gs ON g.`id` = gs.`genre_id`
INNER JOIN `tv_show_ratings` AS r ON gs.`show_id` = r.`show_id`
GROUP BY g.`name`
ORDER BY `rating` DESC;
