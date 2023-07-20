--  lists all shows without the genre Comedy in the database hbtn_0d_tvshows
SELECT tv_shows.title
FROM tv_shows
LEFT JOIN shows_genres ON tv_shows.id = shows_genres.show_id
LEFT JOIN genres ON shows_genres.genre_id = genres.id
WHERE genres.name != 'Comedy' OR genres.name IS NULL
ORDER BY tv_shows.title ASC;
