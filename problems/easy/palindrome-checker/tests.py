"""Tests for palindrome-checker."""
import pytest
from solution import is_palindrome


class TestBasicCases:
    """Test basic functionality with typical inputs."""

    def test_example_one(self):
        """Test first example from problem description."""
        assert is_palindrome("A man, a plan, a canal: Panama") == True

    def test_example_two(self):
        """Test second example from problem description."""
        assert is_palindrome("race a car") == False

    def test_simple_palindrome(self):
        """Test basic palindrome word."""
        assert is_palindrome("racecar") == True


class TestEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_empty_input(self):
        """Test with empty or minimal input."""
        assert is_palindrome("") == True

    def test_single_element(self):
        """Test with single element input."""
        assert is_palindrome("a") == True

    def test_only_spaces(self):
        """Test with only whitespace."""
        assert is_palindrome("   ") == True

