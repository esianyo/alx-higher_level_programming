-- best rating genres
SELECT tv_genres.name, SUM(rating) AS rating_sum
FROM tv_genres
LEFT JOIN tv_shows_genres ON tv_genres.id = tv_shows_genres.genre_id
LEFT JOIN tv_shows ON tv_shows.id = tv_shows_genres.show_id
GROUP BY tv_genres.name
ORDER BY rating_sum DESC;
