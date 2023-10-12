import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection

from lib.album import Album
from lib.album_repository import AlbumRepository
from lib.artist import Artist
from lib.artist_repository import ArtistRepository


# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# == HOMEPAGE ==
@app.route('/', methods=['GET'])
def home_page():
    connection = get_flask_database_connection(app)
    return render_template('homepage.html')


# == ALBUMS ==
@app.route('/albums/<int:id>', methods=['GET'])
def get_album(id):
    connection = get_flask_database_connection(app)
    album_repository = AlbumRepository(connection)
    album = album_repository.find(id)
    return render_template('albums/show.html', album=album)


@app.route('/albums', methods=['GET'])
def all_albums():
    connection = get_flask_database_connection(app)
    album_repo = AlbumRepository(connection)
    albums = album_repo.all()
    print(type(albums))
    
    return albums

@app.route('/artists/<int:id>', methods=['GET'])
def get_artist(id):
    connection = get_flask_database_connection(app)
    artist_repository = ArtistRepository(connection)
    artist = artist_repository.find(id)
    artist_albums = artist_repository.find_all_albums_by_artist(id)
    return render_template('artists/show.html', artist=artist, albums=artist_albums)

@app.route('/artists', methods=['GET'])
def get_artists():
    connection = get_flask_database_connection(app)
    artist_repository = ArtistRepository(connection)
    artists = artist_repository.all()
    return render_template('artists/index.html', artists=artists)



# GET /emoji
# Returns a smiley face in HTML
# Try it:
#   ; open http://localhost:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    # We use `render_template` to send the user the file `emoji.html`
    # But first, it gets processed to look for placeholders like {{ emoji }}
    # These placeholders are replaced with the values we pass in as arguments
    return render_template('emoji.html', emoji=':)')



# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
