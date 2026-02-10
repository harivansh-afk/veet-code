"""
Task Scheduler

You're building a CI/CD pipeline orchestrator. Given a set of build tasks
with durations and dependency requirements, determine the minimum total
time to complete all tasks when independent tasks can run in parallel.
Also detect if the dependency graph contains a cycle (making the build
impossible).

Each task is represented as (name, duration, dependencies) where
dependencies is a list of task names that must complete before this
task can start.

Example 1:
    Input: tasks = [("compile", 3, []), ("test", 5, ["compile"]), ("lint", 2, []), ("deploy", 1, ["test", "lint"])]
    Output: (9, ["compile", "test", "deploy"])
    Explanation: compile(3) -> test(5) -> deploy(1) = 9. lint(2) runs in parallel and finishes before deploy starts. The critical path is compile -> test -> deploy.

Example 2:
    Input: tasks = [("A", 2, ["B"]), ("B", 3, ["A"])]
    Output: (-1, [])
    Explanation: Circular dependency between A and B makes execution impossible.

Example 3:
    Input: tasks = [("X", 4, []), ("Y", 4, []), ("Z", 1, ["X", "Y"])]
    Output: (5, ["X", "Z"])
    Explanation: X and Y run in parallel (both take 4). Z waits for both, then takes 1. Critical path is X(4) -> Z(1) = 5 (or equivalently Y -> Z). Return either.

Constraints:
    - Task names are unique non-empty strings
    - Durations are positive integers (>= 1)
    - Dependencies reference other task names in the list
    - Return (-1, []) if a cycle exists
    - The critical path is the longest path through the dependency graph
    - If multiple critical paths have the same length, return any one
    - The critical path list is ordered from first task to last
    - All tasks must be completed; the answer is the makespan
"""


def schedule_tasks(
    tasks: list[tuple[str, int, list[str]]],
) -> tuple[int, list[str]]:
    """Return (min_total_time, critical_path) or (-1, []) if cycle exists."""
    pass  # Your implementation here
