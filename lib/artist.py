class Artist:

    def __init__(self, id, name, genre):
        self.id = id
        self.name = name
        self.genre = genre

    # Test object equevilance acceptance method
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # Tstring representation method
    def __repr__(self):
        return f"Artist({self.id}, {self.name}, {self.genre})"
