import unittest
from unittest.mock import patch
from random import randint, uniform
from math import sqrt, pi, cos, sin
from services.bowyer_watson import Edge, Triangle, BowyerWatson
from dungeon import Dungeon

class TestTriangle(unittest.TestCase):
    def setUp(self):
        self.p1 = (randint(1, 70), randint(1, 80))
        self.p2 = (randint(1, 70), randint(1, 80))
        self.p3 = (randint(1, 70), randint(1, 80))
        
        self.triangle = Triangle(self.p1, self.p2, self.p3)

    def test_circumcenter(self):
        u = self.triangle.center
        r = self.triangle.radius
        d1 = sqrt((u[0] - self.p1[0])**2 + (u[1] - self.p1[1])**2)
        d2 = sqrt((u[0] - self.p2[0])**2 + (u[1] - self.p2[1])**2)
        d3 = sqrt((u[0] - self.p3[0])**2 + (u[1] - self.p3[1])**2)
        self.assertAlmostEqual(d1, d2)
        self.assertAlmostEqual(d2, d3)
        self.assertAlmostEqual(d1, r)

    def test_determinant_is_zero(self):
        triangle = Triangle((1, 1), (2, 2), (3, 3))
        self.assertEqual(triangle.center, None)
        self.assertEqual(triangle.radius, float('inf'))

class TestBowyerWatson(unittest.TestCase):
    def setUp(self):
        p = [(1, 1), (2, 2), (3, 2), (3, 1), (3, 7), (6, 4), (5, 0)]
        self.b = BowyerWatson(p)
        self.tri = Triangle(p[0], p[1], p[2])

    def test_is_in_circle(self):
        self.assertTrue(self.b.is_in_circle(self.b.points[3], self.tri))
        self.assertFalse(self.b.is_in_circle(self.b.points[4], self.tri))
        
        for _ in range(100):
            theta = uniform(0, 2 * pi)
            r = sqrt(uniform(self.tri.radius**2, (self.tri.radius*100)**2))
            x = self.tri.center[0] + r * cos(theta)
            y = self.tri.center[1] + r * sin(theta)
            self.assertFalse(self.b.is_in_circle((x, y), self.tri))

        for _ in range(100):
            theta = uniform(0, 2 * pi)
            r = self.tri.radius * sqrt(uniform(0, 1))
            x = self.tri.center[0] + r * cos(theta)
            y = self.tri.center[1] + r * sin(theta)
            self.assertTrue(self.b.is_in_circle((x, y), self.tri))

    def test_is_unique(self):
        ab = Edge(self.b.points[0], self.b.points[1])
        ba = Edge(self.b.points[1], self.b.points[0])
        ac = Edge(self.b.points[0], self.b.points[2])
        edges = [ab, ba, ac]
        self.assertTrue(self.b.is_unique(edges, ac))
        self.assertFalse(self.b.is_unique(edges, ab))
        self.assertFalse(self.b.is_unique(edges, ba))

    def test_delaunay_triangulation(self):
        self.b.triangulate()
        for triangle in self.b.triangles:
            tri_points = [triangle.p1, triangle.p2, triangle.p3]
            for point in self.b.points:
                if point not in tri_points:
                    self.assertFalse(self.b.is_in_circle(point, triangle))

    def test_graph_is_connected(self):
        dungeon = Dungeon(10000, 10000, 200, 200, 200)
        dungeon.place_rooms()

        def visit(vertex, visited, graph):
            if vertex in visited:
                return
            visited.add(vertex)

            for next_vertex in graph[vertex]:
                visit(next_vertex, visited, graph)

        graph = {}
        for triangle in dungeon.d.triangles:
            for edge in triangle.edges:
                if edge.p1 not in graph:
                    graph[edge.p1] = [edge.p2]
                else:
                    graph[edge.p1].append(edge.p2)
                if edge.p2 not in graph:
                    graph[edge.p2] = [edge.p1]
                else:
                    graph[edge.p2].append(edge.p1)

        for point in dungeon.d.points:
            visited = set()
            visit(point, visited, graph)
            self.assertEqual(visited, set(dungeon.d.points))

    def test_correct_number_of_triangles(self):
        n = len(self.b.points)
        h = 4 # Number of points on the convex hull (verified visually)
        num_of_triangles = 2 * n - 2 - h
        self.b.triangulate()
        self.assertEqual(num_of_triangles, len(self.b.triangles))
    
    @patch("matplotlib.pyplot.show")
    def test_display(self, mock_show):
        self.b.triangulate()
        self.b.display()

        mock_show.assert_called_once()