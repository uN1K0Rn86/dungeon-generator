from random import randint

def generate_room(maxwidth: int, maxheight: int):
    """
    Generates a width and a height for a room in the dungeon.

    Args:
        maxwidth (Integer): the maximum allowed width for a room.
        maxheight (Integer): the maximum allowed height for a room.
    
    Returns:
        A tuple containing the width and height.
    """

    width = randint(2, maxwidth)
    height = randint(2, maxheight)

    return (width, height)

def place_rooms(width, height, room_maxwidth, room_maxheight, amount):
    """
    Place rooms into a dungeon based on dungeon width and height, maximum width and height per room, and amount of rooms.

    Args:
        width (Integer): The width (in tiles) of the entire dungeon.
        height (Integer): The height of the dungeon.
        room_maxwidth (Integer): Maximum width for a single room.
        room_maxheight (Integer): Maximum height for a single room.
        amount (Integer): Amount of rooms to place.

    Returns:
        A list of lists containing the dungeon with the placed rooms and the amount of remaining tries to place the last room.
    """

    dungeon = [["#" for i in range(width)] for j in range(height)]

    # Place the rooms
    for i in range(amount):
        overlap = True
        tries = 50 # Allow 50 attempts to avoid endless loops if a room cannot be placed
        while overlap and tries > 0:
            overlap = False
            room = generate_room(room_maxwidth, room_maxheight)

            # Randomly select the upper left corner location for the room so that it is not at the edge of the dungeon
            up_left_corner = (randint(1, width - room[0] - 1), randint(1, height - room[1] - 1))
            
            # Make sure the room does not connect to an existing room
            for j in range(up_left_corner[1] - 1, up_left_corner[1] + room[1] + 1):
                for k in range(up_left_corner[0] - 1, up_left_corner[0] + room[0] + 1):
                    if dungeon[j][k] == ".":
                        overlap = True
            tries -= 1

        # If the room cannot be placed, return the dungeon as is
        if tries == 0:
            return dungeon, tries

        # Place the room
        for j in range(up_left_corner[1], up_left_corner[1] + room[1]):
            for k in range (up_left_corner[0], up_left_corner[0] + room[0]):
                dungeon[j][k] = "."

    return dungeon, tries
