"""Tests for two-sum."""
import pytest
from solution import two_sum


class TestBasicCases:
    """Test basic functionality with typical inputs."""

    def test_example_one(self):
        """Test first example from problem description."""
        assert sorted(two_sum([2, 7, 11, 15], 9)) == [0, 1]

    def test_example_two(self):
        """Test second example from problem description."""
        assert sorted(two_sum([3, 2, 4], 6)) == [1, 2]

    def test_adjacent_elements(self):
        """Test when answer elements are adjacent."""
        assert sorted(two_sum([1, 2, 3, 4], 7)) == [2, 3]


class TestEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_same_value_twice(self):
        """Test with duplicate values that sum to target."""
        assert sorted(two_sum([3, 3], 6)) == [0, 1]

    def test_first_and_last(self):
        """Test when answer is first and last elements."""
        assert sorted(two_sum([2, 4, 6, 8, 10, 7], 9)) == [0, 5]

    def test_negative_numbers(self):
        """Test with negative numbers in the list."""
        assert sorted(two_sum([-1, -2, -3, -4, -5], -8)) == [2, 4]
