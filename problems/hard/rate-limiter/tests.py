"""Tests for rate-limiter."""
import pytest
from solution import RateLimiter


class TestBasicCases:
    """Test basic functionality with typical inputs."""

    def test_allow_within_limit(self):
        """Test requests within the limit are allowed."""
        limiter = RateLimiter(max_requests=3, window_seconds=60)
        assert limiter.allow_request("user1", 0) == True
        assert limiter.allow_request("user1", 30) == True
        assert limiter.allow_request("user1", 45) == True

    def test_block_over_limit(self):
        """Test requests over limit are blocked."""
        limiter = RateLimiter(max_requests=2, window_seconds=60)
        assert limiter.allow_request("user1", 0) == True
        assert limiter.allow_request("user1", 30) == True
        assert limiter.allow_request("user1", 45) == False

    def test_multiple_users_independent(self):
        """Test each user has independent limits."""
        limiter = RateLimiter(max_requests=1, window_seconds=60)
        assert limiter.allow_request("user1", 0) == True
        assert limiter.allow_request("user2", 0) == True
        assert limiter.allow_request("user1", 30) == False
        assert limiter.allow_request("user2", 30) == False

    def test_get_remaining_basic(self):
        """Test remaining count decreases with requests."""
        limiter = RateLimiter(max_requests=3, window_seconds=60)
        assert limiter.get_remaining("user1", 0) == 3
        limiter.allow_request("user1", 0)
        assert limiter.get_remaining("user1", 0) == 2


class TestEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_window_expiration(self):
        """Test old requests expire from window."""
        limiter = RateLimiter(max_requests=2, window_seconds=60)
        assert limiter.allow_request("user1", 0) == True
        assert limiter.allow_request("user1", 30) == True
        assert limiter.allow_request("user1", 45) == False
        assert limiter.allow_request("user1", 61) == True

    def test_single_request_limit(self):
        """Test with limit of 1 request."""
        limiter = RateLimiter(max_requests=1, window_seconds=10)
        assert limiter.allow_request("user1", 0) == True
        assert limiter.allow_request("user1", 5) == False
        assert limiter.allow_request("user1", 11) == True

    def test_new_user_full_allowance(self):
        """Test new users start with full allowance."""
        limiter = RateLimiter(max_requests=5, window_seconds=60)
        limiter.allow_request("user1", 0)
        assert limiter.get_remaining("new_user", 20) == 5

    def test_rapid_same_timestamp(self):
        """Test multiple requests at same timestamp."""
        limiter = RateLimiter(max_requests=3, window_seconds=1)
        assert limiter.allow_request("user1", 0) == True
        assert limiter.allow_request("user1", 0) == True
        assert limiter.allow_request("user1", 0) == True
        assert limiter.allow_request("user1", 0) == False

