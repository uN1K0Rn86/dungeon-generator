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

    def test_graph_is_connected(self):
        def visit(vertex, visited, graph):
            if vertex in visited:
                return
            visited.add(vertex)

            for next_vertex in graph[vertex]:
                visit(next_vertex, visited, graph)
        
        graph = {}
        for edge in self.dungeon.paths.mst.edges:
            if edge.p1 not in graph:
                graph[edge.p1] = [edge.p2]
            else:
                graph[edge.p1].append(edge.p2)
            if edge.p2 not in graph:
                graph[edge.p2] = [edge.p1]
            else:
                graph[edge.p2].append(edge.p1)

        for vertex in self.dungeon.paths.mst.vertices:
            visited = set()
            visit(vertex, visited, graph)
            self.assertEqual(visited, self.dungeon.paths.mst.vertices)

    @patch("matplotlib.pyplot.show")
    def test_display(self, mock_show):
        self.dungeon.paths.display()

        mock_show.assert_called_once()