from visual_output import output

def test_visual_output():
    """
    Test to make sure that the visual output correctly deciphers the list of lists.
    """
    dungeon_list = [
        ["#", "#", "#", "#", "#", "#", "#"],
        ["#", ".", ".", ".", "#", "#", "#"],
        ["#", "#", ".", ".", "#", "#", "#"],
        ["#", "#", ".", "#", "#", ".", "#"],
        ["#", "#", "#", "#", ".", ".", "#"],
        ["#", "#", "#", ".", ".", ".", "#"],
        ["#", "#", "#", ".", ".", "#", "#"],
        ["#", "#", "#", "#", "#", "#", "#"]
    ]

    dungeon_output = output(dungeon_list)

    assert dungeon_output == """#######
#...###
##..###
##.##.#
####..#
###...#
###..##
#######
"""
