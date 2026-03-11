-- Lists all shows from hbtn_0d_tvshows that have at least one genre linked.
-- Displays tv_shows.title and tv_show_genres.genre_id, sorted by title and genre_id ascending.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
