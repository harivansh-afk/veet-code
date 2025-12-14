# Problem Examples Reference

Reference examples for generating consistent, high-quality practice problems.

---

## Easy Example: Email Validator

**solution.py**:
```python
"""
Email Validator

You're building a user registration system for an e-commerce platform.
Before storing customer emails in your database, you need to validate
that they follow the correct format to prevent data quality issues.

Example 1:
    Input: email = "user@example.com"
    Output: True
    Explanation: Has username, single @, domain with dot

Example 2:
    Input: email = "invalid-email"
    Output: False
    Explanation: Missing @ symbol

Example 3:
    Input: email = "@nodomain.com"
    Output: False
    Explanation: Empty username before @

Constraints:
    - Input is always a string
    - Valid: non-empty username, exactly one @, domain with at least one dot
    - No spaces allowed anywhere
"""


def is_valid_email(email: str) -> bool:
    """Return True if email is valid, False otherwise."""
    pass  # Your implementation here
```

**tests.py**:
```python
"""Tests for email-validator."""
import pytest
from solution import is_valid_email


class TestBasicCases:
    """Test basic functionality with typical inputs."""

    def test_valid_simple_email(self):
        """Test standard email format."""
        assert is_valid_email("user@example.com") == True

    def test_valid_with_subdomain(self):
        """Test email with subdomain."""
        assert is_valid_email("user.name@mail.example.co.uk") == True

    def test_invalid_missing_at(self):
        """Test email without @ symbol."""
        assert is_valid_email("userexample.com") == False


class TestEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_empty_string(self):
        """Test with empty input."""
        assert is_valid_email("") == False

    def test_empty_username(self):
        """Test with nothing before @."""
        assert is_valid_email("@example.com") == False

    def test_no_domain_dot(self):
        """Test domain without dot."""
        assert is_valid_email("user@examplecom") == False

    def test_spaces_in_email(self):
        """Test email containing spaces."""
        assert is_valid_email("user @example.com") == False
```

---

## Medium Example: Group Transactions

**solution.py**:
```python
"""
Transaction Grouper

You're building a financial dashboard for a budgeting app. Users want
to see their spending grouped by category with totals, so they can
understand where their money is going each month.

Example 1:
    Input: transactions = [
        {"amount": 50, "category": "food", "date": "2024-01-01"},
        {"amount": 30, "category": "food", "date": "2024-01-02"},
        {"amount": 100, "category": "transport", "date": "2024-01-01"}
    ]
    Output: {"food": 80, "transport": 100}
    Explanation: food: 50+30=80, transport: 100

Example 2:
    Input: transactions = []
    Output: {}
    Explanation: No transactions means empty result

Constraints:
    - Each transaction has "amount" (positive int), "category" (str), "date" (str)
    - Categories are case-sensitive
    - Return categories in any order
    - Amount is always positive
"""


def group_transactions(transactions: list[dict]) -> dict[str, int]:
    """Return dictionary mapping each category to its total amount."""
    pass  # Your implementation here
```

**tests.py**:
```python
"""Tests for group-transactions."""
import pytest
from solution import group_transactions


class TestBasicCases:
    """Test basic functionality with typical inputs."""

    def test_multiple_categories(self):
        """Test grouping across different categories."""
        txns = [
            {"amount": 50, "category": "food", "date": "2024-01-01"},
            {"amount": 30, "category": "food", "date": "2024-01-02"},
            {"amount": 100, "category": "transport", "date": "2024-01-01"}
        ]
        assert group_transactions(txns) == {"food": 80, "transport": 100}

    def test_single_category(self):
        """Test all transactions in one category."""
        txns = [
            {"amount": 10, "category": "food", "date": "2024-01-01"},
            {"amount": 20, "category": "food", "date": "2024-01-02"},
            {"amount": 30, "category": "food", "date": "2024-01-03"}
        ]
        assert group_transactions(txns) == {"food": 60}

    def test_single_transaction(self):
        """Test with just one transaction."""
        txns = [{"amount": 25, "category": "entertainment", "date": "2024-01-01"}]
        assert group_transactions(txns) == {"entertainment": 25}


class TestEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_empty_list(self):
        """Test with no transactions."""
        assert group_transactions([]) == {}

    def test_case_sensitive_categories(self):
        """Test that categories are case-sensitive."""
        txns = [
            {"amount": 10, "category": "Food", "date": "2024-01-01"},
            {"amount": 20, "category": "food", "date": "2024-01-02"}
        ]
        result = group_transactions(txns)
        assert result == {"Food": 10, "food": 20}

    def test_many_categories(self):
        """Test with many different categories."""
        txns = [
            {"amount": 1, "category": "a", "date": "2024-01-01"},
            {"amount": 2, "category": "b", "date": "2024-01-01"},
            {"amount": 3, "category": "c", "date": "2024-01-01"},
            {"amount": 4, "category": "d", "date": "2024-01-01"}
        ]
        assert group_transactions(txns) == {"a": 1, "b": 2, "c": 3, "d": 4}

    def test_large_amounts(self):
        """Test with large transaction amounts."""
        txns = [
            {"amount": 1000000, "category": "salary", "date": "2024-01-01"},
            {"amount": 500000, "category": "salary", "date": "2024-02-01"}
        ]
        assert group_transactions(txns) == {"salary": 1500000}
```

---

## Hard Example: Rate Limiter

**solution.py**:
```python
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
```

**tests.py**:
```python
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

    def test_remaining_after_expiration(self):
        """Test remaining increases as requests expire."""
        limiter = RateLimiter(max_requests=2, window_seconds=60)
        limiter.allow_request("user1", 0)
        limiter.allow_request("user1", 30)
        assert limiter.get_remaining("user1", 30) == 0
        assert limiter.get_remaining("user1", 61) == 1

    def test_rapid_same_timestamp(self):
        """Test multiple requests at same timestamp."""
        limiter = RateLimiter(max_requests=3, window_seconds=1)
        assert limiter.allow_request("user1", 0) == True
        assert limiter.allow_request("user1", 0) == True
        assert limiter.allow_request("user1", 0) == True
        assert limiter.allow_request("user1", 0) == False

    def test_exact_window_boundary(self):
        """Test behavior at exact window boundary."""
        limiter = RateLimiter(max_requests=1, window_seconds=10)
        assert limiter.allow_request("user1", 0) == True
        assert limiter.allow_request("user1", 10) == False
        assert limiter.allow_request("user1", 11) == True
```

---

## Topic Quick Reference

### Arrays/Lists
- Frequency counting, deduplication, sliding window
- Two pointers, rotation, merging sorted arrays

### Strings
- Validation (email, URL, phone), parsing CSV/JSON
- Pattern matching, compression, transformation

### Hash Maps
- Grouping by property, counting occurrences
- Two sum variants, caching, anagram detection

### Classes/OOP
- Shopping cart, bank account, task scheduler
- State machines, event systems, entity modeling

### Data Processing
- Filter/map/reduce pipelines, aggregation
- Interval merging, pagination, deduplication
