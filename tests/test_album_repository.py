from lib.album_repository import AlbumRepository
from lib.album import Album

"""
When we call AlbumRepository#all
We get a list of Album objects reflecting the seed data.
"""
def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/music_library.sql") # Seed our database with some test data
    repository = AlbumRepository(db_connection) # Create a new AlbumRepository

    albums = repository.all() # Get all albums

    # Assert on the results
    assert albums == [
        {"album_id": 1, "title": "Doolittle", "artist_name": "Pixies", "release_year": 1989},
        {"album_id": 2, "title": "Surfer Rosa", "artist_name": "Pixies", "release_year": 1988},
        {"album_id": 3, "title": "Waterloo", "artist_name": "ABBA", "release_year": 1974},
        {"album_id": 4, "title": "Super Trouper", "artist_name": "ABBA", "release_year": 1980},
        {"album_id": 5, "title": "Bossanova", "artist_name": "Pixies", "release_year": 1990},
        {"album_id": 6, "title": "Lover", "artist_name": "Taylor Swift", "release_year": 2019},
        {"album_id": 7, "title": "Folklore", "artist_name": "Taylor Swift", "release_year": 2020},
        {"album_id": 8, "title": "I Put a Spell on You", "artist_name": "Nina Simone", "release_year": 1965},
        {"album_id": 9, "title": "Baltimore", "artist_name": "Nina Simone", "release_year": 1978},
        {"album_id": 10, "title": "Here Comes the Sun", "artist_name": "Nina Simone", "release_year": 1971},
        {"album_id": 11, "title": "Fodder on My Wings", "artist_name": "Nina Simone", "release_year": 1982},
        {"album_id": 12, "title": "Ring Ring", "artist_name": "ABBA", "release_year": 1973}
        ]

    # assert albums == [
    #     Album(1, "Doolittle", 1989, 1),
    #     Album(2, "Surfer Rosa", 1988, 1),
    #     Album(3, "Waterloo", 1974, 2),
    #     Album(4, "Super Trouper", 1980, 2),
    #     Album(5, "Bossanova", 1990, 1),
    #     Album(6, "Lover", 2019, 3),
    #     Album(7, "Folklore", 2020, 3),
    #     Album(8, "I Put a Spell on You", 1965, 4),
    #     Album(9, "Baltimore", 1978, 4),
    #     Album(10, "Here Comes the Sun", 1971, 4),
    #     Album(11, "Fodder on My Wings", 1982, 4),
    #     Album(12, "Ring Ring", 1973, 2)
    # ]

"""
When we call AlbumRepository#find
We get a single Album object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)

    album = repository.find(3)
    assert album == {"album_id": 3, "title": "Waterloo", "artist_name": "ABBA", "release_year": 1974}



"""
When we call AlbumRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)

    repository.create(Album(None, "Trompe le Monde", 1991, 1))

    result = repository.all()
    assert result == [
        {"album_id": 1, "title": "Doolittle", "artist_name": "Pixies", "release_year": 1989},
        {"album_id": 2, "title": "Surfer Rosa", "artist_name": "Pixies", "release_year": 1988},
        {"album_id": 3, "title": "Waterloo", "artist_name": "ABBA", "release_year": 1974},
        {"album_id": 4, "title": "Super Trouper", "artist_name": "ABBA", "release_year": 1980},
        {"album_id": 5, "title": "Bossanova", "artist_name": "Pixies", "release_year": 1990},
        {"album_id": 6, "title": "Lover", "artist_name": "Taylor Swift", "release_year": 2019},
        {"album_id": 7, "title": "Folklore", "artist_name": "Taylor Swift", "release_year": 2020},
        {"album_id": 8, "title": "I Put a Spell on You", "artist_name": "Nina Simone", "release_year": 1965},
        {"album_id": 9, "title": "Baltimore", "artist_name": "Nina Simone", "release_year": 1978},
        {"album_id": 10, "title": "Here Comes the Sun", "artist_name": "Nina Simone", "release_year": 1971},
        {"album_id": 11, "title": "Fodder on My Wings", "artist_name": "Nina Simone", "release_year": 1982},
        {"album_id": 12, "title": "Ring Ring", "artist_name": "ABBA", "release_year": 1973},
        {"album_id": 13, "title": "Trompe le Monde", "artist_name": "Pixies", "release_year": 1991}
        ]

"""
When we call AlbumRepository#delete
We remove a record from the database.
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)

    repository.delete(2)
    result = repository.all()
    assert result == [
        {"album_id": 1, "title": "Doolittle", "artist_name": "Pixies", "release_year": 1989},
        {"album_id": 3, "title": "Waterloo", "artist_name": "ABBA", "release_year": 1974},
        {"album_id": 4, "title": "Super Trouper", "artist_name": "ABBA", "release_year": 1980},
        {"album_id": 5, "title": "Bossanova", "artist_name": "Pixies", "release_year": 1990},
        {"album_id": 6, "title": "Lover", "artist_name": "Taylor Swift", "release_year": 2019},
        {"album_id": 7, "title": "Folklore", "artist_name": "Taylor Swift", "release_year": 2020},
        {"album_id": 8, "title": "I Put a Spell on You", "artist_name": "Nina Simone", "release_year": 1965},
        {"album_id": 9, "title": "Baltimore", "artist_name": "Nina Simone", "release_year": 1978},
        {"album_id": 10, "title": "Here Comes the Sun", "artist_name": "Nina Simone", "release_year": 1971},
        {"album_id": 11, "title": "Fodder on My Wings", "artist_name": "Nina Simone", "release_year": 1982},
        {"album_id": 12, "title": "Ring Ring", "artist_name": "ABBA", "release_year": 1973}
        ]

