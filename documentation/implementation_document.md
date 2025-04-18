# Implementation Document

## Program Structure

The core of the program is managed through the Dungeon -class. A Dungeon object is created and updated throughout dungeon creation. The user interacts with the program through the UI -class. The dungeon creation process is as follows:

- Rooms are randomly generated and placed into the dungeon
- The Bowyer-Watson algorithms forms a Delaunay triangulation of the rooms. In practise, this is a triangulation of the center points of the rooms in such a way that no center point is in the circumcircle of any of the other triangles.
- Prim's algorithm is used to form a minimum spanning tree from the Delaunay triangulation.
- The A-Star algorithm is used to form hallways between the rooms according to the MST formed by Prim's algorithm.

## Time and Space Complexities

### Bowyer-Watson

- The Algorithm iterates over all points and inserts them one at a time. This means n insertions.
- For each insertion, the algorithm iterates over all triangles currently in the triangulation. In the worst case, this happens n times, but on average it is log(n) times.
- The algorithm then loops through all the unique edges of all the bad triangles and creates new triangles based on them. Since the amount of triangles is proportional to n, this is bounded to O(n).

Since the edges are processed alongside the bad triangles, this step does not contribute significantly to the overall time complexity. The overall time complexity is ***O(n<sup>2</sup>)*** (worst case) or ***O(nlog n)*** (expected).

### Prim

## Deficiencies and Possible Improvements

Coming Soon

## LLM Usage

ChatGPT was used to check syntax and help with matplotlib (examples only) and for brainstorming how to test algorithms. All code was written independently of LLMs.

## Sources

- [Wikipedia: Circumcircles](https://en.wikipedia.org/wiki/Circumcircle#Circumcenter_coordinates)
- [Vazgriz: Procedurally Generated Dungeons](https://vazgriz.com/119/procedurally-generated-dungeons/)  
- [Wikipedia: Delauney Triangulation](https://en.wikipedia.org/wiki/Delaunay_triangulation)  
- [Wikipedia: Bowyer-Watson Algorithm](https://en.wikipedia.org/wiki/Bowyer%E2%80%93Watson_algorithm)  
- [Wikipedia: Prim's Algorithm](https://en.wikipedia.org/wiki/Prim%27s_algorithm)  
- [Wikipedia: A* Algorithm](https://en.wikipedia.org/wiki/A*_search_algorithm)
- [Method for calculating super triangle](https://brandewinder.com/2025/03/05/delaunay-super-triangle/)