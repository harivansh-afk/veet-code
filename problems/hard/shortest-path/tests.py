"""Tests for shortest-path."""
import pytest
from solution import shortest_path


class TestBasicCases:
    """Test basic functionality with typical inputs."""

    def test_example_one(self):
        """Test first example from problem description."""
        edges = [("A", "B", 4), ("A", "C", 2), ("C", "B", 1), ("B", "D", 5), ("C", "D", 8)]
        assert shortest_path(edges, "A", "D") == (7, ["A", "C", "B", "D"])

    def test_example_two(self):
        """Test second example with no reverse path."""
        edges = [("X", "Y", 3)]
        assert shortest_path(edges, "Y", "X") == (-1, [])

    def test_example_three(self):
        """Test indirect path cheaper than direct edge."""
        edges = [("A", "B", 1), ("B", "C", 2), ("A", "C", 10)]
        assert shortest_path(edges, "A", "C") == (3, ["A", "B", "C"])

    def test_direct_edge_is_shortest(self):
        """Test when the direct edge is the cheapest route."""
        edges = [("A", "B", 1), ("A", "C", 5), ("C", "B", 5)]
        assert shortest_path(edges, "A", "B") == (1, ["A", "B"])


class TestEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_start_equals_end(self):
        """Test when start and end are the same node."""
        edges = [("A", "B", 1)]
        assert shortest_path(edges, "A", "A") == (0, ["A"])

    def test_no_edges(self):
        """Test with empty edge list and different start/end."""
        assert shortest_path([], "A", "B") == (-1, [])

    def test_single_edge_path(self):
        """Test path that is a single edge."""
        edges = [("A", "B", 7)]
        assert shortest_path(edges, "A", "B") == (7, ["A", "B"])

    def test_long_chain(self):
        """Test shortest path through a long chain of nodes."""
        edges = [("A", "B", 1), ("B", "C", 1), ("C", "D", 1), ("D", "E", 1)]
        assert shortest_path(edges, "A", "E") == (4, ["A", "B", "C", "D", "E"])

    def test_disconnected_graph(self):
        """Test with disconnected components."""
        edges = [("A", "B", 1), ("C", "D", 1)]
        assert shortest_path(edges, "A", "D") == (-1, [])

    def test_multiple_paths_picks_cheapest(self):
        """Test graph with many paths to verify optimal is chosen."""
        edges = [
            ("S", "A", 10), ("S", "B", 3), ("B", "A", 1),
            ("A", "T", 2), ("B", "T", 20),
        ]
        cost, path = shortest_path(edges, "S", "T")
        assert cost == 6
        assert path[0] == "S" and path[-1] == "T"

    def test_large_weights(self):
        """Test with large edge weights."""
        edges = [("A", "B", 1000000), ("B", "C", 1000000)]
        assert shortest_path(edges, "A", "C") == (2000000, ["A", "B", "C"])

    def test_end_node_not_in_graph(self):
        """Test when end node has no edges at all."""
        edges = [("A", "B", 1), ("B", "C", 2)]
        assert shortest_path(edges, "A", "Z") == (-1, [])
