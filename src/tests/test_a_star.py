import unittest
from dungeon import Dungeon

class TestAStar(unittest.TestCase):
    def setUp(self):
        self.dungeon = Dungeon(90, 80, 20, 19, 18)
        self.dungeon.place_rooms()
        self.dungeon.prim()
        self.dungeon.a_star()