# Weekly Report 2

## What Have I Done / Learned This Week

 - I finished the first version of the Bowyer-Watson algorithm and added plotting using matplotlib to offer a better alternative for displaying dungeons and the Delauney triangulations.

 - I fixed bugs with calculating room centers.

 - I wrote tests for the Bowyer-Watson algorithm.

 - I started the testing document, with detailed explanations for each test.

 - I made some changes to the UI and added the ability to view previously created dungeons. This only works with dungeons created during the same session though.

## What Was Unclear and / or Difficult

Properly understanding the Bowyer-Watson algorithm took a lot of work, but going through it step by step helped.

## Next Steps

- Refining the Bowyer-Watson algorithm. I would like to improve code readability and look into making the algorithm more efficient.

- Start work on Prim's algorithm to create a minimum spanning tree (MST) from the Delaunay triangulation.

## Time Tracking

| Date | What Was Done | Time Used |
|------|---------------|-----------|
| 26.3 | Delauney triangulation | 7h |
| 27.3 | Testing, UI work, documentation, cleaning code | 6h |
| Total | 13h |

## Sources and LLM usage

- [Method for calculating super triangle](https://brandewinder.com/2025/03/05/delaunay-super-triangle/)
- ChatGPT was used to check syntax and help with matplotlib (examples only). All code was written independently of LLMs.