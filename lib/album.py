class Album:

    def __init__(self, id, title, release_year, artist_id) -> None:
        self.id = id
        self.title = title
        self.release_year = release_year
        self.artist_id = artist_id
    
    # equvilance method, allowing objects to be equal for pytest
    def __eq__(self, other):
        if isinstance(other, Album):
            return (self.id == other.id and
                    self.title == other.title and
                    self.release_year == other.release_year and
                    self.artist_id == other.artist_id)
        return False

    # string representation
    def __repr__(self):
        return f"Album({self.id}, {self.title}, {self.release_year}, {self.artist_id})"
