import unittest
from services.bowyer_watson import Edge, Triangle, BowyerWatson
from random import randint
from math import sqrt

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

class TestBowyerWatson(unittest.TestCase):
    def setUp(self):
        p = [(1, 1), (2, 2), (3, 2), (3, 1), (3, 7), (6, 4), (5, 0)]
        self.b = BowyerWatson(p)
        self.tri = Triangle(p[0], p[1], p[2])

    def test_is_in_circle(self):
        self.assertTrue(self.b.is_in_circle(self.b.points[3], self.tri))
        self.assertFalse(self.b.is_in_circle(self.b.points[4], self.tri))

    def test_is_unique(self):
        ab = Edge(self.b.points[0], self.b.points[1])
        ba = Edge(self.b.points[1], self.b.points[0])
        ac = Edge(self.b.points[0], self.b.points[2])
        edges = [ab, ba, ac]
        self.assertTrue(self.b.is_unique(edges, ac))
        self.assertFalse(self.b.is_unique(edges, ab))
        self.assertFalse(self.b.is_unique(edges, ba))