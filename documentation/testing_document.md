# Testing Document

## Coverage Report

[![codecov](https://codecov.io/gh/uN1K0Rn86/dungeon-generator/graph/badge.svg?token=MS4VHFA85E)](https://codecov.io/gh/uN1K0Rn86/dungeon-generator)

## Unit Testing

Automated unit testing is done where applicable. Explanations for each test are below:

### Class Triangle

- Circumcenter: the test uses the methods in the Triangle -class to calculate the circumcenter and the radius of the circumcircle. It then calculates the distance from each vertex to the calculated circumcenter and verifies that each of these distances is the same (according to the definition of a circumcenter).

### Class BowyerWatson

- Is_in_circle: this tests the method for determining if a point is within the circumcircle of a given triangle. The test checks that the method returns "True" for a point that is in the circumcircle and "False" for a point that is not.

- Is_unique: this tests the method for checking if an edge between two points is unique within a list of edges. The test adds 3 edges to a list, two of which contain the same points but in different orders, and a third that shares one of the points with the other two. The test checks that the method returns "True" for the third edge and "False" for the first two.

- Delaunay_triangulation: this test first runs the Delaunay triangulation for a predetermined set of points. It then iterates through each triangle in the triangulation and checks that every point that is not a vertex of that triangle is NOT within the circumcircle of that triangle. If this is true for every triangle and every point not within that triangle, the Delaunay condition is fulfilled.

- Graph_is_connected: this test makes sure that the graph produced by the Delaunay triangulation is connected i.e. every point is accessible from every point by following the edges of the triangles. A large dungeon is used to make sure this works.

- Display: this test calls the display() -method and makes sure that matplotlib.pyplot.show is called once at the end of it, thus making sure that the display method gives no errors.

### Class Prim

- MST_has_correct_number_of_edges: this test verifies that the number of edges in the MST produced by Prim's algorithm is one less than the number of vertices.-

- All_vertices_are_used: this test makes sure that the MST contains every vertex included in the input triangles by creating a set of those vertices from the triangles and comparing it with the set of vertices included in the MST.

- Graph_is_connected: this test makes sure that every vertex is accessible from every other vertex in the MST by performind a depth first search from every vertex and comparing the result to the set of all vertices in the MST.

- Is_minimum_spanning_tree: this test compares the weight of the MST calculated by Prim's algorithm to that calculated by a known implementation of an MST algorithm from the networkx library.

- Display: this test calls the display() -method and makes sure that matplotlib.pyplot.show is called once at the end of it, thus making sure that the display method gives no errors.

### Class AStar

- A_Star_finds_path: this test chooses two rooms out of the dungeon and uses the A* algorithm to form a path between them. It then verifies that the starting and ending points match those of the path given by the algorithm.

- Path_is_optimal: this test also forms a path between two rooms in the dungeon using A*. It then compares the length of the path (in tiles) to the Manhattan distance (+1) between the starting and ending point. The +1 is because the Manhattan distance equals the amount of steps taken, not the amount of tiles. This works because the algorithm always finds a direct route.

### Class Dungeon

- Size_is_correct: this test makes sure the created dungeon has the length and width it is supposed to.

- All_rooms_are_placed: this test makes sure that the correct number of rooms (as specified by the user) is placed when the dungeon is big enough to fit them all.

- If_rooms_cant_all_be_placed_return: this test makes sure that the method for placing rooms into a dungeon returns without causing an exception if the desired number of rooms does not fit into the dungeon.

- Visual_output: this tests the method that converts the dungeon from a matrix to a string.

- Display: this test works the same way as the display test for the bowyer-watson class. It calls the display method and makes sure that plt.show() is called at the end.

### Class Room

- Room_size_within_limits: this test makes sure that the generated room size is within the limits specified by the user.

- Visual_output: this tests the method that converts the room into a string and makes sure the width and height of the room are correct in the visual output.

## UI Testing

For now, UI testing has been done manually. In the future I will either come up with a robust a repeatable routine for thorough UI manual testing, or (more likely) automate it. This will be decided once the UI has a more permanent form.

## Running Tests

To run the tests, clone this repository:
```
git clone https://github.com/uN1K0Rn86/dungeon-generator.git
```

navigate to the directory containing the app:
```
cd dungeon-generator
```

install dependencies:
```
poetry install
```

and run the tests:
```
pytest
```