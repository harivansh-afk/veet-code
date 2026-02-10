"""Tests for valid-parentheses."""
import pytest
from solution import is_valid


class TestBasicCases:
    """Test basic functionality with typical inputs."""

    def test_example_one(self):
        """Test first example from problem description."""
        assert is_valid("([]){}") is True

    def test_example_two(self):
        """Test second example from problem description."""
        assert is_valid("([)]") is False

    def test_example_three(self):
        """Test third example from problem description."""
        assert is_valid("{{") is False

    def test_simple_pairs(self):
        """Test simple matched pairs."""
        assert is_valid("()") is True
        assert is_valid("[]") is True
        assert is_valid("{}") is True


class TestEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_empty_string(self):
        """Test with empty input."""
        assert is_valid("") is True

    def test_single_bracket(self):
        """Test with a single unmatched bracket."""
        assert is_valid("(") is False
        assert is_valid("]") is False

    def test_deeply_nested(self):
        """Test with deeply nested brackets."""
        assert is_valid("{[({[]})]}") is True

    def test_close_before_open(self):
        """Test closing bracket appearing before any opener."""
        assert is_valid(")(") is False

    def test_mismatched_types(self):
        """Test opening one type and closing another."""
        assert is_valid("{)") is False
        assert is_valid("[}") is False
