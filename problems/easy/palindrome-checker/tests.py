"""Tests for palindrome-checker."""
import pytest
from solution import is_palindrome


class TestBasicCases:
    """Test basic functionality with typical inputs."""

    def test_simple_palindrome(self):
        """Test basic palindrome word."""
        assert is_palindrome("racecar") == True

    def test_sentence_palindrome(self):
        """Test palindrome with spaces and punctuation."""
        assert is_palindrome("A man, a plan, a canal: Panama") == True

    def test_not_palindrome(self):
        """Test non-palindrome string."""
        assert is_palindrome("hello") == False


class TestEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_empty_string(self):
        """Test with empty input."""
        assert is_palindrome("") == True

    def test_single_character(self):
        """Test with single character."""
        assert is_palindrome("a") == True

    def test_only_spaces(self):
        """Test with only whitespace."""
        assert is_palindrome("   ") == True

    def test_mixed_case(self):
        """Test case insensitivity."""
        assert is_palindrome("RaceCar") == True

    def test_numbers_in_string(self):
        """Test with numbers."""
        assert is_palindrome("12321") == True

