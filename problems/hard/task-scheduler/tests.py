"""Tests for task-scheduler."""
import pytest
from solution import schedule_tasks


class TestBasicCases:
    """Test basic functionality with typical inputs."""

    def test_example_one(self):
        """Test first example from problem description."""
        tasks = [("compile", 3, []), ("test", 5, ["compile"]), ("lint", 2, []), ("deploy", 1, ["test", "lint"])]
        assert schedule_tasks(tasks) == (9, ["compile", "test", "deploy"])

    def test_example_two_cycle(self):
        """Test second example with circular dependency."""
        tasks = [("A", 2, ["B"]), ("B", 3, ["A"])]
        assert schedule_tasks(tasks) == (-1, [])

    def test_example_three_parallel(self):
        """Test parallel tasks with shared dependency."""
        tasks = [("X", 4, []), ("Y", 4, []), ("Z", 1, ["X", "Y"])]
        cost, path = schedule_tasks(tasks)
        assert cost == 5
        assert path[0] in ("X", "Y") and path[-1] == "Z"

    def test_linear_chain(self):
        """Test simple linear dependency chain."""
        tasks = [("A", 2, []), ("B", 3, ["A"]), ("C", 4, ["B"])]
        assert schedule_tasks(tasks) == (9, ["A", "B", "C"])


class TestEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_single_task(self):
        """Test with a single task and no dependencies."""
        tasks = [("solo", 5, [])]
        assert schedule_tasks(tasks) == (5, ["solo"])

    def test_all_independent(self):
        """Test all tasks run in parallel with no dependencies."""
        tasks = [("A", 3, []), ("B", 7, []), ("C", 5, [])]
        cost, path = schedule_tasks(tasks)
        assert cost == 7
        assert path == ["B"]

    def test_diamond_dependency(self):
        """Test diamond-shaped dependency graph."""
        tasks = [("A", 1, []), ("B", 5, ["A"]), ("C", 2, ["A"]), ("D", 1, ["B", "C"])]
        assert schedule_tasks(tasks) == (7, ["A", "B", "D"])

    def test_three_node_cycle(self):
        """Test cycle involving three nodes."""
        tasks = [("A", 1, ["C"]), ("B", 1, ["A"]), ("C", 1, ["B"])]
        assert schedule_tasks(tasks) == (-1, [])

    def test_wide_fan_in(self):
        """Test many tasks feeding into one final task."""
        tasks = [("A", 1, []), ("B", 2, []), ("C", 3, []), ("D", 4, []), ("final", 1, ["A", "B", "C", "D"])]
        assert schedule_tasks(tasks) == (5, ["D", "final"])

    def test_deep_chain_with_parallel_branch(self):
        """Test long chain alongside a shorter parallel branch."""
        tasks = [
            ("A", 1, []), ("B", 1, ["A"]), ("C", 1, ["B"]), ("D", 1, ["C"]),
            ("shortcut", 2, []),
            ("end", 1, ["D", "shortcut"]),
        ]
        assert schedule_tasks(tasks) == (5, ["A", "B", "C", "D", "end"])

    def test_partial_cycle_with_valid_tasks(self):
        """Test graph where some tasks form a cycle but others don't."""
        tasks = [("A", 1, []), ("B", 2, ["C"]), ("C", 3, ["B"])]
        assert schedule_tasks(tasks) == (-1, [])

    def test_large_durations(self):
        """Test with large task durations."""
        tasks = [("A", 1000000, []), ("B", 1000000, ["A"])]
        assert schedule_tasks(tasks) == (2000000, ["A", "B"])
