from collections import defaultdict
from random import randint
from typing import Set, List, DefaultDict, Tuple, Optional
import numpy as np
import matplotlib.pyplot as plt
from services.bowyer_watson import Edge, Triangle

class Mst:
    """
    A class to represent a minimum spanning tree.
    """

    def __init__(self) -> None:
        self.outgoing: Set[Edge] = set()
        self.vertices: Set[Tuple] = set()
        self.edges: Set[Edge] = set()

class Prim:
    """
    A class to implement Prim's algorithm.
    """

    def __init__(self, triangles: List[Triangle], chance: int):
        """
        Initialize a set of edges from triangles provided by the Bowyer-Watson algorithm,
        a dictionary of vertices showing their connections, and a set containing all vertices.
        """
        self.edges: Set[Edge] = set()
        for triangle in triangles:
            for edge in triangle.edges:
                self.edges.add(edge)

        self.graph: DefaultDict[Tuple[int, int], Set[Tuple[int, int]]] = defaultdict(set)
        self.vertices: Set[Tuple] = set()
        for edge in self.edges:
            self.graph[edge.p1].add(edge.p2)
            self.graph[edge.p2].add(edge.p1)
            self.vertices.add(edge.p1)
            self.vertices.add(edge.p2)

        self.chance = chance
        self.mst = Mst()

    def form_mst(self, demo: bool = False) -> None:
        """
        Method that forms a minimum spanning tree from sets of edges and vertices.
        """
        if not self.vertices: # pragma: no cover
            return

        vertex: Tuple[int, int] = next(iter(self.vertices)) # Arbitrarily choose a starting vertex

        # Loop over vertices that are not yet included in the mst.
        while vertex is not None and self.vertices:
            # Add the vertex to the MST and remove it from the set of vertices still to be added
            self.mst.vertices.add(vertex)
            self.vertices.discard(vertex)

            distance = float('inf')

            # Add connections to neighbouring vertices to possible edges for MST
            for connection in self.graph[vertex]:
                if connection not in self.mst.vertices:
                    edge = Edge(vertex, connection)
                    self.mst.outgoing.add(edge)

            next_v: Optional[Tuple] = None
            next_e: Optional[Edge] = None

            # Loop over possible connections and determine the shortest
            for edge in self.mst.outgoing:
                weight = np.sqrt((edge.p1[0]-edge.p2[0])**2 + (edge.p1[1]-edge.p2[1])**2)
                if weight < distance:
                    distance = weight
                    next_v = edge.p1 if edge.p1 not in self.mst.vertices else edge.p2
                    next_e = edge

            if demo:
                self.display() # pragma: no cover

            # Remove edges that connect back into the MST from the next vertex
            if next_v:
                for connection in self.graph[next_v]:
                    if connection in self.mst.vertices:
                        edge = Edge(next_v, connection)
                        self.mst.outgoing.remove(edge)
                        vertex = next_v

            if next_e:
                self.mst.edges.add(next_e)

        if self.chance > 0:
            additional_edges = self.add_loops()
            self.mst.edges = self.mst.edges | additional_edges

    def add_loops(self) -> Set[Edge]:
        """
        Adds additional paths to the MST to create loops in the dungeon.

        Args: 
            chance (int): percentage chance to include any given edge
        Returns:
            edges (set): set of edges to add to paths
        """
        edges: Set[Edge] = self.edges.difference(self.mst.edges)
        additional_edges: Set[Edge] = set()

        for edge in edges:
            if randint(1, 100) <= self.chance:
                additional_edges.add(edge)

        return additional_edges

    def display(self):
        """
        Method for displaying the vertices and edges along with possible outgoing edges.
        """
        vertices_list = list(self.mst.vertices | self.vertices)
        x = [vertex[0] for vertex in vertices_list]
        y = [vertex[1] for vertex in vertices_list]

        plt.figure(figsize=(6, 6))
        plt.scatter(x, y, color='blue')

        for edge in self.mst.edges:
            e_x = [edge.p1[0], edge.p2[0]]
            e_y = [edge.p1[1], edge.p2[1]]
            plt.plot(e_x, e_y, color='green', linewidth=1)

        for edge in self.mst.outgoing: # pragma: no cover
            e_x = [edge.p1[0], edge.p2[0]]
            e_y = [edge.p1[1], edge.p2[1]]
            plt.plot(e_x, e_y, color='red', linewidth=1)

        print("Adding point to minimum spanning tree. Possible connections in red, added connections in green.")
        plt.show()
