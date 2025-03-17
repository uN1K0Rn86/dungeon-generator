def output(tiles: list):
    """
    Changes the dungeon from matrix form into a string.

    Args:
        tiles (List): A list of lists where each list represents a row in the dungeon.

    Returns:
        dungeon (String): A string depicting a visual representation of the dungeon.
    """

    dungeon = ""
    for row in tiles:
        for tile in row:
            dungeon += tile
        dungeon += "\n"

    return dungeon
