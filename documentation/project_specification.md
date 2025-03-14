# Project Specification

## Aim and Motivation

The aim of this project is to create an application that can randomly generate 2-dimensional dungeons based on user specifications. The dungeons will consist of 1x1  square tiles. The user will be able to specify the total size of the dungeon, the maximum size of a room, the number of rooms (within reason given the size of the dungeon), and the relative frequency of hallway connections (in addition to the requirement that every room must have at least one connection).

I chose this topic for the project because it seemed interesting. In my experience, games can be more fun when there is an element of randomness to the world, and I would like to learn how to implement something like that.

## Algorithms and Data Structures

The application will consist of several algorithms, each with a specific task.

- An algorithm to place the rooms into the dungeon. The rooms will be taken from a pool of randomly generated rooms based on the maximum size. A room will be placed in the center of the dungeon, followed by more rooms until the specified number of rooms is reached or there is no more space. This should be possible in O(n) time with n being the number of rooms.
- A Bowyer-Watson algorithm to create a Delauney triangulation of the rooms. This will create potential connections between the rooms. A basic version of this algorithm works in O(n^2) time. By precomputing circumcircles, it is possible to implement in O(n*log(n)) time at the expense of additional memory usage, which will be the goal.
- Prim's algorithm to create a minimum spanning tree (MST) from the triangulation. This will ensure that all rooms are connected. Additional other connections will be preserved based on the user specification. The goal will be to use binary heaps and adjacency lists, which will allow the algorithm to reach O(|E|log|V|) time (with |E| being the amount of edges and |V| the amount of rooms).
- A* algorithm to form the actual hallways from one room to the next. The time complexity will depend on the heuristic function used.
- An algorithm that provides a visual representation of the dungeon. This will be updated during generation. The visual representation will be simple, likely something on the command line.

It is difficult to say what the core of this project will be, as all phases of dungeon generation are essential for the final product. However, perhaps the most important part will be forming the Delauney triangulation. That will form the basis for connections between rooms in the dungeon.

## Programming Languages

Python will be used for this project.

In addition to python, I know JavaScript well enough to peer review projects.

## Degree Programme

Bachelor's degree in Computer Science (Tietojenkäsittelytieteen kandidaatti TKT)

## Sources

[Vazgriz: Procedurally Generated Dungeons](https://vazgriz.com/119/procedurally-generated-dungeons/)  
[Wikipedia: Delauney Triangulation](https://en.wikipedia.org/wiki/Delaunay_triangulation)  
[Wikipedia: Bowyer-Watson Algorithm](https://en.wikipedia.org/wiki/Bowyer%E2%80%93Watson_algorithm)  
[Wikipedia: Prim's Algorithm](https://en.wikipedia.org/wiki/Prim%27s_algorithm)  
[Wikipedia: A* Algorithm](https://en.wikipedia.org/wiki/A*_search_algorithm)