from lib.album import Album
from lib.database_connection import DatabaseConnection

class AlbumRepository:

    # initialise database connection
    def __init__(self, connection):
        self._connection = connection


    # Retrieve all albums
    def all(self):
        #unsightly albums and artist table join on artist id
        rows = self._connection.execute('SELECT albums.id AS album_id, albums.title, artists.name as artist_name, albums.release_year FROM artists JOIN albums ON albums.artist_id = artists.id')

        albums = []
        for row in rows:
            #formating results output appearence
            item = {"album_id": row["album_id"],
                    "title": row["title"],
                    "artist_name": row["artist_name"],
                    "release_year": row["release_year"]}
            albums.append(item)
        return albums
    
    # Find album by id
    def find(self, id):
        rows = self._connection.execute(
            #unsightly albums and artist table join on artist id
            'SELECT albums.id AS album_id, albums.title, artists.name as artist_name, albums.release_year FROM artists JOIN albums ON albums.artist_id = artists.id WHERE albums.id = %s', [id])
            # 'SELECT * FROM albums_with_artists WHERE id = %s', [id])
        row = rows[0]
        return {"album_id": row["album_id"],
                "title": row["title"],
                "artist_name": row["artist_name"],
                "release_year": row["release_year"]}

    # Create new album
    def create(self, album:Album):
        self._connection.execute('INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s)', [album.title, album.release_year, album.artist_id])
        return None

    # Delete album by id
    def delete(self, id):
        self._connection.execute(
            'DELETE FROM albums WHERE id = %s', [id]
        )
        return None


