-- shows show shws with genre id NULL.
SELECT tv_shows.tittle, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
Where genre_id IS NULL
ORDER BY tv_shows.title, tv_show_genres.genres_id;
