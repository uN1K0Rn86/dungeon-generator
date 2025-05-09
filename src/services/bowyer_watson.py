from typing import List
import numpy as np
import matplotlib.pyplot as plt

class Edge:
    """
    A class to represent an edge (line) between two points.
    """

    def __init__(self, p1: tuple, p2: tuple):
        """
        Constructor that initializes the points of the edge.
        """
        self.p1 = (p1[0], p1[1])
        self.p2 = (p2[0], p2[1])

    def __eq__(self, other):
        return {self.p1, self.p2} == {other.p1, other.p2}

    def __hash__(self):
        return hash(frozenset([self.p1, self.p2]))

class Triangle:
    """
    A class to represent triangles consisting of 3 points.
    """

    def __init__(self, p1: tuple, p2: tuple, p3: tuple):
        """
        Constructor that initializes the 3 vertices of the triangle, the circumcenter, and the radius.
        """
        self.p1 = (p1[0], p1[1])
        self.p2 = (p2[0], p2[1])
        self.p3 = (p3[0], p3[1])
        self.edges = (Edge(self.p1, self.p2), Edge(self.p2, self.p3), Edge(self.p3, self.p1))
        self.center: tuple = self.circumcenter()[0]
        self.radius: int = self.circumcenter()[1]

    def circumcenter(self) -> tuple:
        """
        Calculates the center point of the circumcircle and its radius.
        """

        ax = self.p1[0]
        ay = self.p1[1]
        bx = self.p2[0]
        by = self.p2[1]
        cx = self.p3[0]
        cy = self.p3[1]
        d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
        if d == 0:
            return (None, float('inf'))

        ux = ((ax**2 + ay**2) * (by-cy) + (bx**2 + by**2) * (cy-ay) + (cx**2 + cy**2) * (ay-by)) / d
        uy = ((ax**2 + ay**2) * (cx-bx) + (bx**2 + by**2) * (ax-cx) + (cx**2 + cy**2) * (bx-ax)) / d

        radius = np.sqrt((ux - ax)**2 + (uy - ay)**2)

        return ((ux, uy), radius)


class BowyerWatson:
    """
    Class for the Bowyer-Watson algorithm
    """

    def __init__(self, points: List[tuple]):
        """
        Constructor that initializes a super triangle containing all the given points.
        """

        self.points: List[tuple] = points

        # Initialize the super triangle containing all points.
        xmin = float('inf')
        ymin = float('inf')
        xmax = 0
        ymax = 0

        # Find minimum and maximum x and y values
        for point in self.points:
            if point[0] < xmin:
                xmin = point[0]
            if point[0] > xmax:
                xmax = point[0]

            if point[1] < ymin:
                ymin = point[1]
            if point[1] > ymax:
                ymax = point[1]

        # Determine which has a larger difference; x or y values and use that as a baseline
        # for forming the super triangle
        dx = xmax - xmin
        dy = ymax - ymin
        delta_max = max(dx, dy)
        mid_x = (xmin + xmax) / 2
        mid_y = (ymin + ymax) / 2

        # Assign points to the super triangle
        p1 = (mid_x - 20 * delta_max, mid_y - delta_max)
        p2 = (mid_x, mid_y + 20 * delta_max)
        p3 = (mid_x + 20 * delta_max, mid_y - delta_max)

        self.xmin, self.xmax = xmin, xmax
        self.ymin, self.ymax = ymin, ymax
        self.st = Triangle(p1, p2, p3)
        self.triangles: List[Triangle] = [self.st]

    def triangulate(self, demo=False):
        """
        Add all the points to the triangulation and remove any triangles that share an edge
        or vertex with the super triangle.
        """

        for point in self.points:
            self.add_point(point, demo)

        final_triangles: List[Triangle] = []

        # Find which triangles share edges or vertices with the super triangle and discard those
        for triangle in self.triangles:
            not_st = True
            for edge in triangle.edges:
                if edge in self.st.edges:
                    not_st = False
            points = [triangle.p1, triangle.p2, triangle.p3]
            st_points = [self.st.p1, self.st.p2, self.st.p3]
            for point in points:
                if point in st_points:
                    not_st = False
            if not_st:
                final_triangles.append(triangle)

        self.triangles = final_triangles

    def add_point(self, point, demo=False):
        """
        Add a point to the Delauney Triangulation.
        """

        edges: List[Edge] = []
        new_triangles: List[Triangle] = []

        # Iterate through all triangles
        for triangle in self.triangles:
            # If the point is in the triangle's circumcircle, the triangle is invalid
            if self.is_in_circle(point, triangle):
                for edge in triangle.edges:
                    # Add the edges of an invalid triangle to a list of edges used to create new triangles
                    edges.append(edge)
            else:
                # Add valid triangles to the list of new triangles.
                new_triangles.append(triangle)

        unique_edges: List[Edge] = []

        # Find which edges are unique
        for edge in edges:
            if self.is_unique(edges, edge):
                unique_edges.append(edge)

        # Use unique edges to form new triangles
        for edge in unique_edges:
            new_triangles.append(Triangle(edge.p1, edge.p2, point))

        self.triangles = new_triangles
        if demo: # pragma: no cover
            self.display(point, True)

    def is_unique(self, edges: List[Edge], edge: Edge) -> bool:
        """
        Determines whether an edge in a list of edges is unique.
        
        Args:
            edges (list): List of Edges
            edge (Edge): an Edge between two points

        Returns:
            Boolean (True if edge is unique)
        """

        return edges.count(edge) == 1

    def is_in_circle(self, point: tuple, triangle: Triangle) -> bool:
        """
        Check if a point is inside the circumcircle of a triangle.

        Args:
            point (tuple): x and y coordinates of a point
            triangle (Triangle): a triangle object containing 3 points

        Returns:
            Boolean (True if the point is inside the circumcircle of the triangle)
        """

        distance = np.sqrt(((point[0] - triangle.center[0])**2 + (point[1] - triangle.center[1])**2))

        return distance < triangle.radius

    def display(self, point=None, limits=False):
        """
        Create a plot displaying points, the super triangle, and the Delauney triangulation.
        """

        if not point:
            x = [point[0] for point in self.points]
            y = [point[1] for point in self.points]
        else:
            x = point[0]
            y = point[1]

        st_x = [self.st.p1[0], self.st.p2[0], self.st.p3[0], self.st.p1[0]]
        st_y = [self.st.p1[1], self.st.p2[1], self.st.p3[1], self.st.p1[1]]

        plt.figure(figsize=(6, 6))
        if limits:
            plt.xlim(self.xmin - 5, self.xmax + 5)
            plt.ylim(self.ymin - 5, self.ymax + 5)
        plt.scatter(x, y, color='blue')
        plt.plot(st_x, st_y, color='red', linewidth=2)

        for triangle in self.triangles:
            t_x = [triangle.p1[0], triangle.p2[0], triangle.p3[0], triangle.p1[0]]
            t_y = [triangle.p1[1], triangle.p2[1], triangle.p3[1], triangle.p1[1]]
            plt.plot(t_x, t_y, color='green', linewidth=1)

        print("Adding point to Delaunay triangulation. Zoom out to see super triangle.")
        plt.show()
