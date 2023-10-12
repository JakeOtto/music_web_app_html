from lib.artist import Artist

class ArtistRepository:

    # initialise database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all artists
    def all(self):
        rows = self._connection.execute('SELECT * from artists')
        artists = []
        for row in rows:
            item = Artist(row["id"], row["name"], row["genre"])
            artists.append(item)
        return artists

    # Find artist by id
    def find(self, artist_id):
        rows = self._connection.execute(
            'SELECT * from artists WHERE id = %s', [artist_id])
        row = rows[0]
        return Artist(row["id"], row["name"], row["genre"])

    # Create new artist
    def create(self, artist):
        self._connection.execute('INSERT INTO artists (name, genre) VALUES (%s, %s)', [artist.name, artist.genre])
        return None

    # Delete artist by id
    def delete(self, artist_id):
        self._connection.execute(
            'DELETE FROM artists WHERE id = %s', [artist_id])
        return None
    
    
    def find_all_albums_by_artist(self, artist_id):
        rows = self._connection.execute('SELECT title, release_year, id FROM albums WHERE artist_id = %s', [artist_id])
        albums = []
        for row in rows:
            album = {'title' : row["title"], 'release_year': row["release_year"], 'id': row["id"]}
            albums.append(album)
        return albums

