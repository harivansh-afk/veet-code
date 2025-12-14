"""Tests for word-frequency."""
import pytest
from solution import top_words


class TestBasicCases:
    """Test basic functionality with typical inputs."""

    def test_example_one(self):
        """Test first example from problem description."""
        assert top_words("the quick brown fox jumps over the lazy dog the fox", 2) == [("the", 3), ("fox", 2)]

    def test_example_two(self):
        """Test second example from problem description."""
        assert top_words("hello world hello", 5) == [("hello", 2), ("world", 1)]

    def test_single_word_repeated(self):
        """Test with one word repeated."""
        assert top_words("hello hello hello", 1) == [("hello", 3)]


class TestEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_empty_input(self):
        """Test with empty or minimal input."""
        assert top_words("", 5) == []

    def test_n_greater_than_unique_words(self):
        """Test when n exceeds unique word count."""
        assert len(top_words("hello world", 10)) == 2

    def test_case_insensitive(self):
        """Test that counting is case-insensitive."""
        assert top_words("Hello HELLO hello", 1) == [("hello", 3)]

    def test_punctuation_ignored(self):
        """Test that punctuation is stripped."""
        assert top_words("hello, world! hello.", 1) == [("hello", 2)]

    def test_alphabetical_tiebreaker(self):
        """Test alphabetical ordering for same frequency."""
        assert top_words("cat bat ant", 3) == [("ant", 1), ("bat", 1), ("cat", 1)]

