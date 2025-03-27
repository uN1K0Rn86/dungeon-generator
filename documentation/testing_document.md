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

- Display: this test calls the display() -method and makes sure that matplotlib.pyplot.show is called once at the end of it, thus making sure that the display method gives no errors.

### Class Dungeon

- Size_is_correct: this test makes sure the created dungeon has the length and width it is supposed to.

- All_rooms_are_placed: this test makes sure that the correct number of rooms (as specified by the user) is placed when the dungeon is big enough to fit them all.

- Visual_output: this tests the method that converts the dungeon from a matrix to a string.

### Class Room

- Room_size_within_limits: this test makes sure that the generated room size is within the limits specified by the user.

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