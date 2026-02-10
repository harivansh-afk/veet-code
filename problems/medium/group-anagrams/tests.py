"""Tests for group-anagrams."""
import pytest
from solution import group_anagrams


class TestBasicCases:
    """Test basic functionality with typical inputs."""

    def test_example_one(self):
        """Test first example from problem description."""
        assert group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [
            ["ate", "eat", "tea"], ["bat"], ["nat", "tan"]
        ]

    def test_example_two(self):
        """Test second example with no anagrams."""
        assert group_anagrams(["hello", "world"]) == [["hello"], ["world"]]

    def test_example_three(self):
        """Test third example with empty strings."""
        assert group_anagrams(["", ""]) == [["", ""]]

    def test_single_word(self):
        """Test with a single word."""
        assert group_anagrams(["abc"]) == [["abc"]]


class TestEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_empty_list(self):
        """Test with no words."""
        assert group_anagrams([]) == []

    def test_all_same_word(self):
        """Test with identical words."""
        assert group_anagrams(["abc", "abc", "abc"]) == [["abc", "abc", "abc"]]

    def test_single_character_words(self):
        """Test with single character strings."""
        assert group_anagrams(["a", "b", "a"]) == [["a", "a"], ["b"]]

    def test_different_lengths_not_grouped(self):
        """Test that words of different lengths are never grouped."""
        assert group_anagrams(["ab", "abc", "ba"]) == [["ab", "ba"], ["abc"]]
