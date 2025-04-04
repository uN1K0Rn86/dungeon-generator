# Weekly Report 4

## What Have I Done / Learned This Week

- Implemented Prim's algorithm for finding a minimum spanning tree from the Delaunay triangulation.

- Implemented a first version of the A* algorithm for pathfinding. The program now finds paths between rooms specified to be connected by Prim's algorithm and creates hallways between those rooms.

- Wrote some tests for Prim's algorithm.

## What Was Unclear and / or Difficult

- I had some difficulties refining data structures while getting Prim's algorithm to work.

- A* was more straightforward, but I ran into difficulties with visual representation. Representing the dungeon in matrix form conflicts with plotting pyplot because the y-axis coordinates are flipped between the two.

## Next Steps

- Refactoring the code. I wrote a lot of new code this week because I wanted to have features ready, but the code needs cleaning in some places.

- Refining visual representation.

- Further testing for Prim's algorithm and A*.

- Refining the UI.

## Time Tracking

| Date | What Was Done | Time Used |
|------|---------------|-----------|
| 3.4 | Prim's algorithm | 7h |
| 4.4 | A* algorithm and documentation | 7h
| Total | | 14h |

## Sources and LLM usage

- [Prim's Algorithm](https://en.wikipedia.org/wiki/Prim%27s_algorithm)
- [A* algorithm](https://en.wikipedia.org/wiki/A*_search_algorithm)
- ChatGPT was used to check syntax.