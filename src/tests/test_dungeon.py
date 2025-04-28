import unittest
from unittest.mock import patch
from dungeon import Dungeon

class TestDungeon(unittest.TestCase):
    def setUp(self):
        self.dungeon = Dungeon(50, 40, 10, 8, 7)
        self.dungeon.place_rooms()
        self.dungeon.prim(5)
        self.dungeon.a_star()

    def test_size_is_correct(self):
        width = len(self.dungeon.tiles[0])
        height = len(self.dungeon.tiles)
        self.assertEqual(width, self.dungeon.width)
        self.assertEqual(height, self.dungeon.height)

    def test_all_rooms_are_placed(self):
        self.assertEqual(len(self.dungeon.rooms), 7)

    def test_if_rooms_cant_all_be_placed_return(self):
        small_dungeon = Dungeon(20, 20, 10, 10, 15)
        small_dungeon.place_rooms()
        self.assertNotEqual(len(small_dungeon.rooms), 15)


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

    @patch("matplotlib.pyplot.show")
    def test_display_delaunay(self, mock_show):
        self.dungeon.display("delaunay")

        mock_show.assert_called_once()

    @patch("matplotlib.pyplot.show")
    def test_display_prim(self, mock_show):
        self.dungeon.display("prim")

        mock_show.assert_called_once()

    @patch("matplotlib.pyplot.show")
    def test_display_final(self, mock_show):
        self.dungeon.display()

        mock_show.assert_called_once()
