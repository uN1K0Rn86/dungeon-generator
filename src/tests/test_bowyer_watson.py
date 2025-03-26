import unittest
from services.bowyer_watson import Triangle
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