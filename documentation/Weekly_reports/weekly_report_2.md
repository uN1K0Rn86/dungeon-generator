# Weekly Report 2

## What Have I Done / Learned This Week

- I created a basic visual output to depict what the dungeon looks like. This was a necessary first step so I can visualize what the algorithms actually do. I decided to use a list of lists as a data structure to represent the dungeon, because it makes it easy to modify single tiles.

- I created a basic room generator that randomly generates rooms based on user input. I also created an algorithm to place randomly generated rooms into a dungeon.

- I made a rudimentary user interface. The user can specify the maximum width and height of a single room, the total amount of rooms, and the width and height of the dungeon.

- I added a Github actions workflow and a coverage report.

- I refactored the code into classes in order to make the Delauney triangulation application simpler.

- I started work on the Bowyer-Watson algorithm by creating a data structure for triangles and a method for calculating the circumcenter of a triangle.

## What Was Unclear and / or Difficult

I spent considerable time figuring out how to calculate the circumcenter of a triangle. I was planning on coming up with a method from scratch but decided instead to use the formulas on the wikipedia page, seeing as that is significantly easier to code.

I would have liked to get further with coding the actual algorithm, but I had very limited time this week due to unforeseen circumstances.

## Next Steps

Next week, I will continue work on the Bowyer-Watson algorithm. The goal is to finish the algorithm over the next week and then move on to the minimum spanning tree algorithm.

## Time Tracking

| Date | What Was Done | Time Used |
|------|---------------|-----------|
| 17.3 | Basic visual output, room generation, ui | 5h |
| 19.3 | CI, coverage, and linter configuration | 2h |
| 21.3 | Refactoring + started work on Bowyer-Watson | 5h |
| Total | | 12h |

## Sources

- [Wikipedia: Circumcircles](https://en.wikipedia.org/wiki/Circumcircle#Circumcenter_coordinates)