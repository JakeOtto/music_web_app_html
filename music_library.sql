-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS artists;
DROP SEQUENCE IF EXISTS artists_id_seq;
DROP TABLE IF EXISTS albums;
DROP SEQUENCE IF EXISTS albums_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS artists_id_seq;
CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    genre VARCHAR(255)
);

CREATE SEQUENCE IF NOT EXISTS albums_id_seq;
CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    release_year INTEGER,
    artist_id INTEGER
);

-- Finally, we add any records that are needed for the tests to run
INSERT INTO artists (name, genre) VALUES ('Pixies', 'Rock');
INSERT INTO artists (name, genre) VALUES ('ABBA', 'Pop');
INSERT INTO artists (name, genre) VALUES ('Taylor Swift', 'Pop');
INSERT INTO artists (name, genre) VALUES ('Nina Simone', 'Jazz');

INSERT INTO albums (title, release_year, artist_id) VALUES ('Doolittle', 1989, 1);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Surfer Rosa', 1988, 1);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Waterloo', 1974, 2);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Super Trouper', 1980, 2);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Bossanova', 1990, 1);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Lover', 2019, 3);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Folklore', 2020, 3);
INSERT INTO albums (title, release_year, artist_id) VALUES ('I Put a Spell on You', 1965, 4);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Baltimore', 1978, 4);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Here Comes the Sun', 1971, 4);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Fodder on My Wings', 1982, 4);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Ring Ring', 1973, 2);

-- psql -h 127.0.0.1 music_web_app_db < music_library.sql
-- psql -h 127.0.0.1 music_web_app_db_test < music_library.sql


-- -- MAKING A NEW TABLE TO GET ALBUMS WITH ARTIST NAME:
-- DROP TABLE IF EXISTS albums_with_artists;
-- CREATE TABLE albums_with_artists AS
-- SELECT albums.id AS album_id,
--     albums.title,
--     artists.name as artist_name,
--     albums.release_year
-- FROM artists
-- JOIN albums
-- ON albums.artist_id = artists.id
-- ;

-- -- Create a trigger function to automatically update albums_with_artists
-- CREATE OR REPLACE FUNCTION update_albums_with_artists()
-- RETURNS TRIGGER AS $$
-- BEGIN
--   INSERT INTO albums_with_artists (album_id, title, artist_name, release_year)
--   VALUES (NEW.id, NEW.title, (SELECT name FROM artists WHERE id = NEW.artist_id), NEW.release_year);
--   RETURN NEW;
-- END;
-- $$ LANGUAGE plpgsql;

-- -- Create a trigger that fires on INSERT into the albums table
-- CREATE TRIGGER update_albums_with_artists_trigger
-- AFTER INSERT ON albums
-- FOR EACH ROW
-- EXECUTE FUNCTION update_albums_with_artists();


-- INSERT INTO albums (title, release_year, artist_id) VALUES ('Trompe Le Monde', 1991, 1);

