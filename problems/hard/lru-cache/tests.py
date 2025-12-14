"""Tests for lru-cache."""
import pytest
from solution import LRUCache


class TestBasicCases:
    """Test basic functionality with typical inputs."""

    def test_example_one(self):
        """Test first example from problem description."""
        cache = LRUCache(2)
        cache.put("a", 1)
        cache.put("b", 2)
        assert cache.get("a") == 1
        cache.put("c", 3)
        assert cache.get("b") == -1
        assert cache.get("c") == 3

    def test_example_two(self):
        """Test second example from problem description."""
        cache = LRUCache(1)
        cache.put("x", 10)
        cache.put("y", 20)
        assert cache.get("x") == -1
        assert cache.get("y") == 20

    def test_basic_put_get(self):
        """Test basic put and get operations."""
        cache = LRUCache(2)
        cache.put("a", 1)
        cache.put("b", 2)
        assert cache.get("a") == 1
        assert cache.get("b") == 2


class TestEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_capacity_one(self):
        """Test with capacity of 1."""
        cache = LRUCache(1)
        cache.put("a", 1)
        cache.put("b", 2)
        assert cache.get("a") == -1
        assert cache.get("b") == 2

    def test_get_nonexistent(self):
        """Test getting a key that doesn't exist."""
        cache = LRUCache(2)
        assert cache.get("missing") == -1

    def test_put_updates_recency(self):
        """Test that put on existing key updates recency."""
        cache = LRUCache(2)
        cache.put("a", 1)
        cache.put("b", 2)
        cache.put("a", 10)    # a is now most recent
        cache.put("c", 3)     # b should be evicted
        assert cache.get("b") == -1
        assert cache.get("a") == 10

    def test_many_operations(self):
        """Test a sequence of many operations."""
        cache = LRUCache(3)
        cache.put("a", 1)
        cache.put("b", 2)
        cache.put("c", 3)
        cache.get("a")
        cache.put("d", 4)     # evicts b
        cache.put("e", 5)     # evicts c
        assert cache.get("a") == 1
        assert cache.get("b") == -1
        assert cache.get("c") == -1
        assert cache.get("d") == 4
        assert cache.get("e") == 5

    def test_get_updates_recency(self):
        """Test that get updates the access order."""
        cache = LRUCache(2)
        cache.put("a", 1)
        cache.put("b", 2)
        cache.get("a")        # touch a
        cache.put("c", 3)     # evicts b, not a
        assert cache.get("a") == 1
        assert cache.get("b") == -1

