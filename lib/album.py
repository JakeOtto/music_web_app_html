class Album:
    # We initialise with all of our attributes
    # Each column in the table should have an attribute here
    def __init__(self, id, title, release_year, artist_id) -> None:
        self.id = id
        self.title = title
        self.release_year = release_year
        self.artist_id = artist_id
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # This method makes it look nicer when we print an Artist
    def __repr__(self):
        return f"Album({self.id}, {self.title}, {self.release_year}, {self.artist_id})"
    
    def __dict__(self):
        return {
        'id': self.id,
        'title': self.title,
        'release_year': self.release_year,
        'artist_id': self.artist_id
    }

