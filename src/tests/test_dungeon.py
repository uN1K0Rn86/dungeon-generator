import unittest
from dungeon import Dungeon

class TestDungeon(unittest.TestCase):
    def setUp(self):
        self.dungeon = Dungeon(50, 40, 10, 8, 7)

    def test_size_is_correct(self):
        width = len(self.dungeon.tiles[0])
        height = len(self.dungeon.tiles)
        self.assertEqual(width, self.dungeon.width)
        self.assertEqual(height, self.dungeon.height)

    def test_all_rooms_are_placed(self):
        self.dungeon.place_rooms()
        self.assertEqual(len(self.dungeon.rooms), 7)

    def test_visual_output(self):
        self.dungeon.tiles = [
            ["#", "#", "#", "#", "#", "#", "#"],
            ["#", ".", ".", ".", "#", "#", "#"],
            ["#", "#", ".", ".", "#", "#", "#"],
            ["#", "#", ".", "#", "#", ".", "#"],
            ["#", "#", "#", "#", ".", ".", "#"],
            ["#", "#", "#", ".", ".", ".", "#"],
            ["#", "#", "#", ".", ".", "#", "#"],
            ["#", "#", "#", "#", "#", "#", "#"]
        ]

        self.assertEqual(str(self.dungeon), """#######
#...###
##..###
##.##.#
####..#
###...#
###..##
#######
""")
    
    def test_if_room_dont_fit_return_dungeon_as_is(self):
        self.new_dungeon = Dungeon(8, 8, 5, 5, 7)
        self.assertNotEqual(len(self.new_dungeon.rooms), 7)