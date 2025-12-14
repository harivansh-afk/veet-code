"""
LRU Cache

You're building a caching layer for a database-heavy web application.
To reduce load, implement a Least Recently Used (LRU) cache that
automatically evicts the oldest unused entries when capacity is reached.

Example 1:
    cache = LRUCache(capacity=2)
    cache.put("a", 1)
    cache.put("b", 2)
    cache.get("a")       # Returns 1 (a is now most recently used)
    cache.put("c", 3)    # Evicts "b" (least recently used)
    cache.get("b")       # Returns -1 (not found)
    cache.get("c")       # Returns 3

Example 2:
    cache = LRUCache(capacity=1)
    cache.put("x", 10)
    cache.put("y", 20)   # Evicts "x"
    cache.get("x")       # Returns -1
    cache.get("y")       # Returns 20

Constraints:
    - capacity >= 1
    - Keys are strings, values are integers
    - get() returns -1 if key not found
    - put() updates value if key exists (and marks as recently used)
    - Both get() and put() should be O(1) average time
"""


class LRUCache:
    """Least Recently Used cache with O(1) operations."""

    def __init__(self, capacity: int):
        """Initialize cache with given capacity."""
        pass  # Your implementation here

    def get(self, key: str) -> int:
        """Return value for key, or -1 if not found."""
        pass  # Your implementation here

    def put(self, key: str, value: int) -> None:
        """Insert or update key-value pair, evicting LRU if needed."""
        pass  # Your implementation here

