"""Tests for merge-intervals."""
import pytest
from solution import merge


class TestBasicCases:
    """Test basic functionality with typical inputs."""

    def test_example_one(self):
        """Test first example from problem description."""
        assert merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]

    def test_example_two(self):
        """Test second example from problem description."""
        assert merge([[1, 4], [4, 5]]) == [[1, 5]]

    def test_example_three(self):
        """Test third example with unsorted input."""
        assert merge([[1, 4], [0, 4]]) == [[0, 4]]

    def test_no_overlaps(self):
        """Test intervals with no overlaps."""
        assert merge([[1, 2], [5, 6], [9, 10]]) == [[1, 2], [5, 6], [9, 10]]


class TestEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_empty_list(self):
        """Test with no intervals."""
        assert merge([]) == []

    def test_single_interval(self):
        """Test with exactly one interval."""
        assert merge([[1, 5]]) == [[1, 5]]

    def test_all_overlapping(self):
        """Test when all intervals merge into one."""
        assert merge([[1, 4], [2, 5], [3, 6]]) == [[1, 6]]

    def test_contained_interval(self):
        """Test when one interval is fully inside another."""
        assert merge([[1, 10], [3, 5]]) == [[1, 10]]

    def test_unsorted_input(self):
        """Test with input not sorted by start time."""
        assert merge([[5, 6], [1, 3], [2, 4]]) == [[1, 4], [5, 6]]
