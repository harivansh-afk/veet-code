"""
Merge Intervals

You're building a calendar app that needs to consolidate overlapping
meetings. Given a list of time intervals represented as [start, end]
pairs, merge all overlapping intervals and return the resulting list
of non-overlapping intervals sorted by start time.

Two intervals overlap if one starts before the other ends.

Example 1:
    Input: intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    Output: [[1, 6], [8, 10], [15, 18]]
    Explanation: [1, 3] and [2, 6] overlap, merged into [1, 6]

Example 2:
    Input: intervals = [[1, 4], [4, 5]]
    Output: [[1, 5]]
    Explanation: Intervals sharing an endpoint are considered overlapping

Example 3:
    Input: intervals = [[1, 4], [0, 4]]
    Output: [[0, 4]]
    Explanation: Input is not necessarily sorted

Constraints:
    - 0 <= len(intervals) <= 10^4
    - Each interval is [start, end] where start <= end
    - Start and end are non-negative integers
"""


def merge(intervals: list[list[int]]) -> list[list[int]]:
    """Return a list of merged non-overlapping intervals sorted by start."""
    pass  # Your implementation here
