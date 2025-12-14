"""Tests for word-frequency."""
import pytest
from solution import top_words


class TestBasicCases:
    """Test basic functionality with typical inputs."""

    def test_basic_frequency(self):
        """Test basic word counting."""
        result = top_words("the quick brown fox jumps over the lazy dog the fox", 2)
        assert result == [("the", 3), ("fox", 2)]

    def test_all_unique(self):
        """Test when all words are unique."""
        result = top_words("one two three", 2)
        assert result == [("one", 1), ("three", 1)] or result == [("one", 1), ("two", 1)]

    def test_single_word_repeated(self):
        """Test with one word repeated."""
        result = top_words("hello hello hello", 1)
        assert result == [("hello", 3)]


class TestEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_empty_string(self):
        """Test with empty input."""
        result = top_words("", 5)
        assert result == []

    def test_n_greater_than_unique_words(self):
        """Test when n exceeds unique word count."""
        result = top_words("hello world", 10)
        assert len(result) == 2

    def test_case_insensitive(self):
        """Test that counting is case-insensitive."""
        result = top_words("Hello HELLO hello", 1)
        assert result == [("hello", 3)]

    def test_punctuation_ignored(self):
        """Test that punctuation is stripped."""
        result = top_words("hello, world! hello.", 1)
        assert result == [("hello", 2)]

    def test_alphabetical_tiebreaker(self):
        """Test alphabetical ordering for same frequency."""
        result = top_words("cat bat ant", 3)
        assert result == [("ant", 1), ("bat", 1), ("cat", 1)]

