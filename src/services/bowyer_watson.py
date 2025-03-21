class Triangle:
    """
    A class to represent triangles consisting of 3 points
    """

    def __init__(self, p1, p2, p3):
        """
        Constructor that initializes the 3 vertices of the triangle
        """
        self.p1 = (p1[0], p1[1])
        self.p2 = (p2[0], p2[1])
        self.p3 = (p3[0], p3[1])

    def circumcenter(self):
        """
        Calculates the center point of the circumcircle.
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

        return (ux, uy)

class BowyerWatson:
    """
    Class for the Bowyer-Watson algorithm
    """

    def __init__(self, points):
        self.points = points
