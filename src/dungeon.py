from random import randint
import matplotlib.pyplot as plt
from room import Room
from services.bowyer_watson import BowyerWatson
from services.prim import Prim
from services.a_star import AStar

class Dungeon:
    """
    The class dungeon models the dungeon created by the algorithms.
    """

    def __init__(self, width, height, room_maxwidth, room_maxheight, rooms_amount, name=""):
        """
        The constructor, which sets initial properties for the dungeon
        """
        self.width = width
        self.height = height
        self.room_maxwidth = room_maxwidth
        self.room_maxheight = room_maxheight
        self.rooms_amount = rooms_amount
        self.tiles = [["#" for i in range(width)] for j in range(height)]
        self.rooms = []
        self.hallways = []
        self.full = False
        self.d = None
        self.paths = None
        self.name = name

    def place_rooms(self):
        """
        Places the rooms into the dungeon, if they can fit
        """

        for _ in range(self.rooms_amount):
            overlap = True
            tries = 50 # Allow 50 attemps to avoid endless loops

            while overlap and tries > 0:
                overlap = False
                room = Room(self.room_maxwidth, self.room_maxheight)

                # Location of the upper left corner
                room.set_corner(randint(1, self.width - room.width - 1), randint(1, self.height - room.height - 1))

                # Make sure the room does not connect to an existing room
                for j in range(room.corner_y - 1, room.corner_y + room.height + 1):
                    for k in range(room.corner_x - 1, room.corner_x + room.width + 1):
                        if self.tiles[j][k] == ".":
                            overlap = True
                tries -= 1

            # If the room does not fit after 50 attempts, return
            if tries == 0:
                self.full = True
                self.delaunay()
                return

            # Place the room
            for j in range(room.corner_y, room.corner_y + room.height):
                for k in range(room.corner_x, room.corner_x + room.width):
                    self.tiles[j][k] = "."

            self.rooms.append(room)

        self.delaunay()

    def delaunay(self):
        """
        Perform a Delaunay Triangulation using the center of each room as a point.
        """

        room_centers = [(room.center_x, self.height - room.center_y) for room in self.rooms]
        self.d = BowyerWatson(room_centers)
        self.d.triangulate()

    def prim(self):
        """
        Use Prim's algorithm to find a minimum spanning tree of a Delaunay triangulation.
        """

        self.paths = Prim(self.d.triangles)
        self.paths.form_mst()

    def a_star(self):
        """
        Use the A* algorithm to form paths between rooms.
        """

        AStar(self).run()

    def display(self, mode=None):
        """
        Plot the dungeon and the Delauney Triangulation / MST of the rooms in an x-y grid.
        """
        plt.figure(figsize=(8, 8))

        borders_x = [0, self.width, self.width, 0, 0]
        borders_y = [0, 0, self.height, self.height, 0]
        plt.plot(borders_x, borders_y, color='black', linewidth=3)

        for room in self.rooms:
            room_x = [
                room.corner_x,
                room.corner_x,
                room.corner_x + room.width,
                room.corner_x + room.width,
                room.corner_x
                ]
            room_y = [
                self.height - room.corner_y,
                self.height - room.corner_y - room.height,
                self.height - room.corner_y - room.height,
                self.height - room.corner_y,
                self.height - room.corner_y
                ]
            plt.plot(room_x, room_y, color='blue', linewidth=1)

        x = [point[0] for point in self.d.points]
        y = [point[1] for point in self.d.points]
        plt.scatter(x, y, color='orange')

        if mode == "delaunay":
            for triangle in self.d.triangles:
                t_x = [triangle.p1[0], triangle.p2[0], triangle.p3[0], triangle.p1[0]]
                t_y = [triangle.p1[1], triangle.p2[1], triangle.p3[1], triangle.p1[1]]
                plt.plot(t_x, t_y, color='green', linewidth=1)
        elif mode == "prim":
            for edge in self.paths.mst.edges:
                e_x = [edge.p1[0], edge.p2[0]]
                e_y = [edge.p1[1], edge.p2[1]]
                plt.plot(e_x, e_y, color='green', linewidth=1)
        else:
            for tile in self.hallways:
                plt.scatter(tile[0], self.height - tile[1], color='brown', marker='s', s=50)

        plt.show()

    def __str__(self):
        """
        Method for visual representation.
        """
        dungeon = ""
        for row in self.tiles:
            for tile in row:
                dungeon += tile
            dungeon += "\n"

        return dungeon

if __name__ == "__main__":
    d = Dungeon(40, 40, 10, 10, 10, "Castle")
    d.place_rooms()
    d.prim()
    d.display("prim")
    d.a_star()
    print(d)
    d.display()
