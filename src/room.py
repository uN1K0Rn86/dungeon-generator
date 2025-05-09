from random import randint

class Room:
    """
    This class models a room. 
    """

    def __init__(self, maxwidth: int, maxheight: int):
        """
        Constructor that sets a random width and height and initializes locational properties.
        """
        self.width = randint(2, maxwidth)
        self.height = randint(2, maxheight)
        self.corner_x = 0
        self.corner_y = 0
        self.center_x = 0
        self.center_y = 0

    def set_corner(self, x: int, y: int):
        """
        Method that sets the upper left corner coordinates and calculates the center point.
        """
        self.corner_x = x
        self.corner_y = y
        self.center_x = (self.corner_x * 2 + self.width) / 2
        self.center_y = (self.corner_y * 2 + self.height) / 2

    def __str__(self):
        """
        Method for a visual representation.
        """
        room = (self.width * "." + "\n") * self.height
        return room
