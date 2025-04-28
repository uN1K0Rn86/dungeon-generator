import heapq

class Node:
    """
    A class to represent a node for the A-Star algorithm.
    """

    def __init__(self, coordinates, g, h, parent):
        """
        Constructor that initializes the properties for the node
        """
        self.coordinates = coordinates
        self.g = g
        self.h = h
        self.f = g + h
        self.parent = parent

    def __lt__(self, other):
        """
        Less than comparison operator
        """
        return self.f < other.f

class AStar:
    """
    A class to represent an implementation of the A-Star algorithm.
    """
    def __init__(self, dungeon):
        """
        A constructor that initializes a list of tiles and a list of edges.
        """
        self.dungeon = dungeon
        self.edges = dungeon.paths.mst.edges

    def run(self):
        """
        Run the algorithm and convert hallway tiles to floors.
        """
        for edge in self.edges:
            start = (round(edge.p1[0]), self.dungeon.height - round(edge.p1[1]))
            goal = (round(edge.p2[0]), self.dungeon.height - round(edge.p2[1]))

            path = self.find_path(start, goal)

            for tile in path:
                if self.dungeon.tiles[tile[1]][tile[0]] != ".":
                    self.dungeon.hallways.append(tile)
                self.dungeon.tiles[tile[1]][tile[0]] = "."

    def heuristic(self, current, goal):
        """
        Gives an estimate of the length of the path to the goal.
        """

        return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

    def reconstruct_path(self, node):
        """
        Reconstructs the path from a node to the start node.

        Args:
            node(Node): the current node
        Returns:
            path(list): a list of nodes that forms a path to the start node
        """
        path = []
        while node:
            path.append(node.coordinates)
            node = node.parent

        return path

    def neighbors(self, node):
        """
        Make a list of the neighbors of a node, assuming they are in the dungeon.

        Args:
            node (Node): The current node

        Returns:
            adjacent(list): A list of coordinates of neighboring nodes
        """
        adjacent = []
        x, y = node.coordinates

        if x - 1 >= 0:
            adjacent.append((x - 1, y))
        if x + 1 < self.dungeon.width:
            adjacent.append((x + 1, y))
        if y - 1 >= 0:
            adjacent.append((x, y - 1))
        if y + 1 < self.dungeon.height:
            adjacent.append((x, y + 1))

        return adjacent

    def find_path(self, start, goal):
        """
        Implementation of the A-Star algorithm that forms a path from the start node to the goal.

        Args:
            start(tuple): coordinates of the starting node
        Returns:
            path(list): a list that forms a path from the start node to the goal
        """
        start_node = Node(start, 0, self.heuristic(start, goal), None)

        open_list = [start_node]
        open_coords = {start}
        closed = set()

        while open_list:
            current = heapq.heappop(open_list)
            open_coords.remove(current.coordinates)

            if current.coordinates == goal:
                return self.reconstruct_path(current)

            closed.add(current.coordinates)

            neighbors = self.neighbors(current)
            for neighbor in neighbors:
                x, y = neighbor
                if neighbor in closed or neighbor in open_coords:
                    continue

                if self.dungeon.tiles[y][x] == "#":
                    heapq.heappush(open_list, Node(neighbor, current.g + 1, self.heuristic(neighbor, goal), current))
                else:
                    heapq.heappush(open_list, Node(neighbor, current.g, self.heuristic(neighbor, goal), current))
                open_coords.add(neighbor)

        return None
