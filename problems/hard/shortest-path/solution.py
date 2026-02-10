"""
Shortest Path

You're building a navigation system for a logistics company. Given a
network of cities connected by weighted roads, implement a shortest-path
finder that computes the minimum-cost route between two cities using
Dijkstra's algorithm. The system must also detect when no route exists.

Example 1:
    Input: edges = [("A", "B", 4), ("A", "C", 2), ("C", "B", 1), ("B", "D", 5), ("C", "D", 8)], start = "A", end = "D"
    Output: (7, ["A", "C", "B", "D"])
    Explanation: A->C (2) + C->B (1) + B->D (5) = 7, cheaper than A->C->D (10) or A->B->D (9).

Example 2:
    Input: edges = [("X", "Y", 3)], start = "Y", end = "X"
    Output: (-1, [])
    Explanation: No path from Y to X because the edge is one-directional.

Example 3:
    Input: edges = [("A", "B", 1), ("B", "C", 2), ("A", "C", 10)], start = "A", end = "C"
    Output: (3, ["A", "B", "C"])
    Explanation: Going through B costs 3, which beats the direct edge of 10.

Constraints:
    - Edges are directed: (source, destination, weight)
    - All weights are positive integers (>= 1)
    - No duplicate edges (same source and destination)
    - Node names are non-empty strings
    - Return (-1, []) if no path exists
    - Return (0, [start]) if start == end
    - If multiple shortest paths exist, return any one of them
    - The path list includes both start and end nodes
"""


def shortest_path(
    edges: list[tuple[str, str, int]], start: str, end: str
) -> tuple[int, list[str]]:
    """Return (cost, path) for shortest path, or (-1, []) if unreachable."""
    pass  # Your implementation here
