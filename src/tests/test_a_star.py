import unittest
from dungeon import Dungeon
from services.a_star import AStar

class TestAStar(unittest.TestCase):
    def setUp(self):
        self.dungeon = Dungeon(90, 80, 20, 19, 18)
        self.dungeon.place_rooms()
        self.dungeon.prim()
        self.dungeon.a_star()

    def test_astar_finds_path(self):
        start_room = self.dungeon.rooms[0]
        goal_room = self.dungeon.rooms[-1]

        start = (round(start_room.center_x), round(self.dungeon.height - start_room.center_y))
        goal = (round(goal_room.center_x), round(self.dungeon.height - goal_room.center_y))

        path = AStar(self.dungeon).find_path(start, goal)
        self.assertEqual(path[-1], start)
        self.assertEqual(path[0], goal)

    def test_path_is_optimal(self):
        start_room = self.dungeon.rooms[0]
        goal_room = self.dungeon.rooms[-1]

        start = (round(start_room.center_x), round(self.dungeon.height - start_room.center_y))
        goal = (round(goal_room.center_x), round(self.dungeon.height - goal_room.center_y))

        path_length = abs(start[0] - goal[0]) + abs(start[1] - goal[1])
        path = AStar(self.dungeon).find_path(start, goal)
        self.assertEqual(len(path), path_length + 1)