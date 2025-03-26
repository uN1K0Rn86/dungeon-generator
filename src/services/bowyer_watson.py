import numpy as np
import matplotlib.pyplot as plt

class Edge:
    """
    A class to represent an edge (line) between two points.
    """

    def __init__(self, p1, p2):
        """
        Constructor that initializes the points of the edge.
        """
        self.p1 = (p1[0], p1[1])
        self.p2 = (p2[0], p2[1])

    def __eq__(self, other):
        return {self.p1, self.p2} == {other.p1, other.p2}

class Triangle:
    """
    A class to represent triangles consisting of 3 points.
    """

    def __init__(self, p1, p2, p3):
        """
        Constructor that initializes the 3 vertices of the triangle, the circumcenter, and the radius.
        """
        self.p1 = (p1[0], p1[1])
        self.p2 = (p2[0], p2[1])
        self.p3 = (p3[0], p3[1])
        self.edges = (Edge(self.p1, self.p2), Edge(self.p2, self.p3), Edge(self.p3, self.p1))
        self.center = self.circumcenter()[0]
        self.radius = self.circumcenter()[1]

    def circumcenter(self):
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

        ux = ((ax**2 + ay**2) * (by-cy) + (bx**2 + by**2) * (cy-ay) + (cx**2 + cy**2) * (ay-by)) / d
        uy = ((ax**2 + ay**2) * (cx-bx) + (bx**2 + by**2) * (ax-cx) + (cx**2 + cy**2) * (bx-ax)) / d

        radius = np.sqrt((ux - ax)**2 + (uy - ay)**2)

        return ((ux, uy), radius)


class BowyerWatson:
    """
    Class for the Bowyer-Watson algorithm
    """

    def __init__(self, points):
        """
        Constructor that initializes a super triangle containing all the given points.
        """

        self.points = points

        # Initialize the super triangle containing all points.
        xmin = float('inf')
        ymin = float('inf')
        xmax = 0
        ymax = 0
        for point in self.points:
            if point[0] < xmin:
                xmin = point[0]
            if point[0] > xmax:
                xmax = point[0]

            if point[1] < ymin:
                ymin = point[1]
            if point[1] > ymax:
                ymax = point[1]

        square_width = max(xmax - xmin, ymax - ymin)
        p1 = (xmin - 0.5 * square_width, ymin)
        p2 = (xmin + 1.5 * square_width, ymin)
        p3 = (xmin + 0.5 * square_width, ymin + 2 * square_width)

        self.st = Triangle(p1, p2, p3)

        self.triangles = [self.st]

    def triangulate(self):
        """
        Add all the points to the triangulation and remove any triangles that share an edge
        with the super triangle.
        """

        for point in self.points:
            self.add_point(point)

        final_triangles = []

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

    def add_point(self, point):
        """
        Add a point to the Delauney Triangulation.
        """

        edges = []
        new_triangles = []

        for triangle in self.triangles:
            if self.is_in_circle(point, triangle):
                for edge in triangle.edges:
                    edges.append(edge)
            else:
                new_triangles.append(triangle)

        unique_edges = []

        for edge in edges:
            if self.is_unique(edges, edge):
                unique_edges.append(edge)

        for edge in unique_edges:
            try:
                new_triangles.append(Triangle(edge.p1, edge.p2, point))
            except ZeroDivisionError:
                continue

        self.triangles = new_triangles

    def is_unique(self, edges, edge):
        """
        Determines whether an edge in a list of edges is unique.
        
        Args:
            edges (list): List of Edges
            edge (Edge): an Edge between two points

        Returns:
            Boolean (True if edge is unique)
        """

        return edges.count(edge) == 1

    def is_in_circle(self, point, triangle):
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

    def display(self):
        """
        Create a plot displaying points and the super triangle.
        """
        x = [point[0] for point in self.points]
        y = [point[1] for point in self.points]
        st_x = [self.st.p1[0], self.st.p2[0], self.st.p3[0], self.st.p1[0]]
        st_y = [self.st.p1[1], self.st.p2[1], self.st.p3[1], self.st.p1[1]]

        plt.figure(figsize=(6, 6))
        plt.scatter(x, y, color='blue')
        plt.plot(st_x, st_y, color='red', linewidth=2)

        for triangle in self.triangles:
            t_x = [triangle.p1[0], triangle.p2[0], triangle.p3[0], triangle.p1[0]]
            t_y = [triangle.p1[1], triangle.p2[1], triangle.p3[1], triangle.p1[1]]
            plt.plot(t_x, t_y, color='green', linewidth=1)

        plt.show()

if __name__ == "__main__":
    p = [(1, 1), (2, 2), (3, 2), (3, 1), (3, 7), (6, 4), (5, 0)]

    b = BowyerWatson(p)
    b.triangulate()
    b.display()
    c = Triangle(p[0], p[1], p[2])
    print(b.is_in_circle(p[3], c))
    e = Edge(b.points[0], b.points[1])
    f = Edge(b.points[1], b.points[0])
    g = Edge(b.points[2], b.points[1])
    h = [e, f, g]
    print(b.is_unique(h, e))
    print(b.is_unique(h, g))
