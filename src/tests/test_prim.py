import unittest
from unittest.mock import patch
from dungeon import Dungeon

class TestPrim(unittest.TestCase):
    def setUp(self):
        self.dungeon = Dungeon(90, 80, 20, 19, 18)
        self.dungeon.place_rooms()
        self.dungeon.prim()

    def test_mst_has_correct_number_of_edges(self):
        edges = len(self.dungeon.paths.mst.edges)
        vertices = len(self.dungeon.paths.mst.vertices)
        self.assertEqual(edges, vertices - 1)

    def test_all_vertices_are_used(self):
        vertices = set()
        for triangle in self.dungeon.d.triangles:
            vertices.add(triangle.p1)
            vertices.add(triangle.p2)
            vertices.add(triangle.p3)
        self.assertEqual(vertices, self.dungeon.paths.mst.vertices)

    @patch("matplotlib.pyplot.show")
    def test_display(self, mock_show):
        self.dungeon.paths.display()

        mock_show.assert_called_once()