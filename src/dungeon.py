from random import randint
from room import Room

class Dungeon:
    """
    The class dungeon models the dungeon created by the algorithms.
    """

    def __init__(self, width, height, room_maxwidth, room_maxheight, rooms_amount):
        """
        The constructor, which sets initial properties for the dungeon
        """
        self.width = width
        self.height = height
        self.room_maxwidth = room_maxwidth
        self.room_maxheight = room_maxheight
        self.rooms_amount = rooms_amount
        self.tiles = [["#" for i in range(width)] for j in range(height)]
        self.rooms = []
        self.full = False

    def place_rooms(self):
        """
        Places the rooms into the dungeon, if they can fit
        """

        for i in range(self.rooms_amount):
            overlap = True
            tries = 50 # Allow 50 attemps to avoid endless loops

            while overlap and tries > 0:
                overlap = False
                room = Room(self.room_maxwidth, self.room_maxheight)

                # Location of the upper left corner
                room.set_corner(randint(1, self.width - room.width - 1), randint(1, self.height - room.height - 1))

                # Make sure the room does not connect to an existing room
                for j in range(room.corner_y - 1, room.corner_y + room.height + 1):
                    for k in range(room.corner_x - 1, room.corner_x + room.width + 1):
                        if self.tiles[j][k] == ".":
                            overlap = True
                tries -= 1

            # If the room does not fit after 50 attempts, return
            if tries == 0:
                self.full = True
                return

            # Place the room
            for j in range(room.corner_y, room.corner_y + room.height):
                for k in range(room.corner_x, room.corner_x + room.width):
                    self.tiles[j][k] = "."
            
            self.rooms.append(room)

    def __str__(self):
        dungeon = ""
        for row in self.tiles:
            for tile in row:
                dungeon += tile
            dungeon += "\n"
        
        return dungeon