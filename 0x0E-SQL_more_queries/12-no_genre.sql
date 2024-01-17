-- Shows contained in hbtn_0d_tvshows without a genre linked.
USE hbtn_0d_tvshows;

SELECT tv_genres.name FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_show_genres.show_id IS NULL
ORDER BY tv_genres.name;
