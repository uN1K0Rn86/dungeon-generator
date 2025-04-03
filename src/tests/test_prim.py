import unittest
from unittest.mock import patch
from dungeon import Dungeon

class TestPrim(unittest.TestCase):
    def setUp(self):
        self.dungeon = Dungeon(90, 80, 20, 19, 18)
        self.dungeon.place_rooms()
        self.prim = self.dungeon.prim()

    def test_mst_has_correct_number_of_edges(self):
        edges = len(self.prim.mst.edges)
        vertices = len(self.prim.mst.vertices)
        self.assertEqual(edges, vertices - 1)

    @patch("matplotlib.pyplot.show")
    def test_display(self, mock_show):
        self.prim.display()

        mock_show.assert_called_once()