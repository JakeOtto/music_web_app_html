from lib.album import Album
# from album import Album
# from database_connection import DatabaseConnection

class AlbumRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all albums
    def all(self):
        rows = self._connection.execute('SELECT albums.id AS album_id, albums.title, artists.name as artist_name, albums.release_year FROM artists JOIN albums ON albums.artist_id = artists.id')
        albums = []
        for row in rows:
            item = {"album_id": row["album_id"],
                    "title": row["title"],
                    "artist_name": row["artist_name"],
                    "release_year": row["release_year"]}
            albums.append(item)
        return albums
    
    # Find a single album by their id
    def find(self, id):
        rows = self._connection.execute(
            'SELECT albums.id AS album_id, albums.title, artists.name as artist_name, albums.release_year FROM artists JOIN albums ON albums.artist_id = artists.id WHERE albums.id = %s', [id])
            # 'SELECT * FROM albums_with_artists WHERE id = %s', [id])
        row = rows[0]
        return {"album_id": row["album_id"],
                "title": row["title"],
                "artist_name": row["artist_name"],
                "release_year": row["release_year"]}

    # Create a new album
    # Do you want to get its id back? Look into RETURNING id;
    def create(self, album:Album):
        self._connection.execute('INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s)', [album.title, album.release_year, album.artist_id])
        return None

    # Delete an album by their id
    def delete(self, id):
        self._connection.execute(
            'DELETE FROM albums WHERE id = %s', [id]
        )
        return None
