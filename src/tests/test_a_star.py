import unittest
from dungeon import Dungeon
from services.a_star import AStar, Node

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

    def test_edge_nodes(self):
        a_star = AStar(self.dungeon)
        ne_node = Node((88, 0), 0, 5, None)
        nw_node = Node((0, 1), 0, 5, None)
        sw_node = Node((1, 79), 0, 5, None)
        se_node = Node((89, 78), 0, 5, None)

        nodes = [ne_node, nw_node, sw_node, se_node]

        for node in nodes:
            neighbors = a_star.neighbors(node)
            self.assertEqual(len(neighbors), 3)

    def test_no_path_outside(self):
        a_star = AStar(self.dungeon)
        goal = (200, 200)

        path = a_star.find_path((50, 40), goal)
        self.assertEqual(path, None)