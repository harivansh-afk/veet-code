"""
Rate Limiter

You're building an API gateway for a SaaS platform. To prevent abuse
and ensure fair usage, you need to implement a rate limiter that tracks
requests per user using a sliding window algorithm.

The limiter should allow at most `max_requests` per user within any
`window_seconds` time period.

Example 1:
    limiter = RateLimiter(max_requests=3, window_seconds=60)
    limiter.allow_request("user1", timestamp=0)   # True (1st request)
    limiter.allow_request("user1", timestamp=30)  # True (2nd request)
    limiter.allow_request("user1", timestamp=45)  # True (3rd request)
    limiter.allow_request("user1", timestamp=50)  # False (limit reached)
    limiter.allow_request("user1", timestamp=61)  # True (1st expired)

Example 2:
    limiter = RateLimiter(max_requests=2, window_seconds=10)
    limiter.allow_request("user1", timestamp=0)   # True
    limiter.allow_request("user2", timestamp=0)   # True (different user)
    limiter.allow_request("user1", timestamp=5)   # True
    limiter.allow_request("user1", timestamp=8)   # False

Constraints:
    - max_requests >= 1
    - window_seconds >= 1
    - Timestamps are non-negative integers (seconds)
    - Timestamps are non-decreasing per user
    - user_id is a non-empty string
"""


class RateLimiter:
    """Sliding window rate limiter for API request throttling."""

    def __init__(self, max_requests: int, window_seconds: int):
        """Initialize with request limit and time window."""
        pass  # Your implementation here

    def allow_request(self, user_id: str, timestamp: int) -> bool:
        """Return True if request allowed, False if rate limited."""
        pass  # Your implementation here

    def get_remaining(self, user_id: str, timestamp: int) -> int:
        """Return remaining requests allowed for user at timestamp."""
        pass  # Your implementation here

