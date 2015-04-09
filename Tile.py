class Tile(object):
    def __init__(self, name, north = False, south = False, east = False, west = False, message = ""):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.message = message

    def rotate(self, direction):
        """
        Rotates new rooms before thay are placed.
        """
        pass

    def breakOut(self):
        """
        Triggered when player is trapped with no more doorways to continue.
        Creates door in current room on wall of players choice,
        the player then battles 3 zombies.
        """
        pass


class IndoorTile(Tile):
    pass


class OutdoorTile(Tile):
    pass
