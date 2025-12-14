# Problem Examples Reference

Reference examples for generating consistent, high-quality practice problems.

## Easy Example: Email Validator

**solution.py**:
```python
"""
Email Validator

You're building a user registration system. Before storing emails in your
database, you need to validate that they follow the correct format.

Write a function that checks if an email address is valid.

Example 1:
    Input: email = "user@example.com"
    Output: True
    Explanation: Has username, @, domain with dot

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
    - Valid emails have: non-empty username, exactly one @, domain with at least one dot
    - No spaces allowed anywhere in the email
"""


def is_valid_email(email: str) -> bool:
    """Return True if email is valid, False otherwise."""
    pass  # Your implementation here
```

**tests.py**:
```python
import pytest
from solution import is_valid_email


def test_valid_simple():
    assert is_valid_email("user@example.com") == True


def test_valid_with_dots():
    assert is_valid_email("user.name@example.co.uk") == True


def test_invalid_no_at():
    assert is_valid_email("userexample.com") == False


def test_invalid_no_domain_dot():
    assert is_valid_email("user@examplecom") == False


def test_invalid_empty_username():
    assert is_valid_email("@example.com") == False


def test_invalid_spaces():
    assert is_valid_email("user @example.com") == False
```

---

## Medium Example: Group Transactions

**solution.py**:
```python
"""
Transaction Grouper

You're building a financial dashboard. Users want to see their transactions
grouped by category, with totals calculated for each group.

Given a list of transactions (each with amount, category, and date),
return a dictionary grouping transactions by category with their total.

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
    - Each transaction has "amount" (positive int), "category" (string), "date" (string)
    - Categories are case-sensitive
    - Return categories in any order
"""


def group_transactions(transactions: list[dict]) -> dict[str, int]:
    """Return dictionary mapping category to total amount."""
    pass  # Your implementation here
```

**tests.py**:
```python
import pytest
from solution import group_transactions


def test_multiple_categories():
    txns = [
        {"amount": 50, "category": "food", "date": "2024-01-01"},
        {"amount": 30, "category": "food", "date": "2024-01-02"},
        {"amount": 100, "category": "transport", "date": "2024-01-01"}
    ]
    assert group_transactions(txns) == {"food": 80, "transport": 100}


def test_empty_list():
    assert group_transactions([]) == {}


def test_single_transaction():
    txns = [{"amount": 25, "category": "entertainment", "date": "2024-01-01"}]
    assert group_transactions(txns) == {"entertainment": 25}


def test_single_category_multiple_transactions():
    txns = [
        {"amount": 10, "category": "food", "date": "2024-01-01"},
        {"amount": 20, "category": "food", "date": "2024-01-02"},
        {"amount": 30, "category": "food", "date": "2024-01-03"}
    ]
    assert group_transactions(txns) == {"food": 60}


def test_case_sensitive_categories():
    txns = [
        {"amount": 10, "category": "Food", "date": "2024-01-01"},
        {"amount": 20, "category": "food", "date": "2024-01-02"}
    ]
    result = group_transactions(txns)
    assert result == {"Food": 10, "food": 20}


def test_many_categories():
    txns = [
        {"amount": 1, "category": "a", "date": "2024-01-01"},
        {"amount": 2, "category": "b", "date": "2024-01-01"},
        {"amount": 3, "category": "c", "date": "2024-01-01"},
        {"amount": 4, "category": "d", "date": "2024-01-01"}
    ]
    assert group_transactions(txns) == {"a": 1, "b": 2, "c": 3, "d": 4}
```

---

## Hard Example: Rate Limiter

**solution.py**:
```python
"""
Rate Limiter

You're building an API gateway that needs to prevent abuse. Implement a
rate limiter that tracks requests per user and enforces limits using
a sliding window algorithm.

The rate limiter should allow at most `max_requests` per user within
any `window_seconds` time period.

Example 1:
    limiter = RateLimiter(max_requests=3, window_seconds=60)
    limiter.allow_request("user1", timestamp=0)   # True (1st request)
    limiter.allow_request("user1", timestamp=30)  # True (2nd request)
    limiter.allow_request("user1", timestamp=45)  # True (3rd request)
    limiter.allow_request("user1", timestamp=50)  # False (4th in 60s window)
    limiter.allow_request("user1", timestamp=61)  # True (1st request expired)

Example 2:
    limiter = RateLimiter(max_requests=2, window_seconds=10)
    limiter.allow_request("user1", timestamp=0)   # True
    limiter.allow_request("user2", timestamp=0)   # True (different user)
    limiter.allow_request("user1", timestamp=5)   # True
    limiter.allow_request("user1", timestamp=8)   # False (limit reached)

Constraints:
    - max_requests >= 1
    - window_seconds >= 1
    - timestamps are non-negative integers (seconds)
    - timestamps are always non-decreasing for a given user
    - user_id is a non-empty string
"""


class RateLimiter:
    """Sliding window rate limiter."""

    def __init__(self, max_requests: int, window_seconds: int):
        """Initialize rate limiter with request limit and time window."""
        pass  # Your implementation here

    def allow_request(self, user_id: str, timestamp: int) -> bool:
        """Return True if request is allowed, False if rate limited."""
        pass  # Your implementation here

    def get_remaining(self, user_id: str, timestamp: int) -> int:
        """Return number of remaining requests allowed for user."""
        pass  # Your implementation here
```

**tests.py**:
```python
import pytest
from solution import RateLimiter


def test_basic_allow():
    limiter = RateLimiter(max_requests=3, window_seconds=60)
    assert limiter.allow_request("user1", 0) == True
    assert limiter.allow_request("user1", 30) == True
    assert limiter.allow_request("user1", 45) == True


def test_rate_limit_exceeded():
    limiter = RateLimiter(max_requests=2, window_seconds=60)
    assert limiter.allow_request("user1", 0) == True
    assert limiter.allow_request("user1", 30) == True
    assert limiter.allow_request("user1", 45) == False


def test_window_expiration():
    limiter = RateLimiter(max_requests=2, window_seconds=60)
    assert limiter.allow_request("user1", 0) == True
    assert limiter.allow_request("user1", 30) == True
    assert limiter.allow_request("user1", 45) == False
    assert limiter.allow_request("user1", 61) == True  # First request expired


def test_multiple_users_independent():
    limiter = RateLimiter(max_requests=1, window_seconds=60)
    assert limiter.allow_request("user1", 0) == True
    assert limiter.allow_request("user2", 0) == True
    assert limiter.allow_request("user1", 30) == False
    assert limiter.allow_request("user2", 30) == False


def test_get_remaining():
    limiter = RateLimiter(max_requests=3, window_seconds=60)
    assert limiter.get_remaining("user1", 0) == 3
    limiter.allow_request("user1", 0)
    assert limiter.get_remaining("user1", 0) == 2
    limiter.allow_request("user1", 30)
    assert limiter.get_remaining("user1", 30) == 1


def test_get_remaining_after_expiration():
    limiter = RateLimiter(max_requests=2, window_seconds=60)
    limiter.allow_request("user1", 0)
    limiter.allow_request("user1", 30)
    assert limiter.get_remaining("user1", 30) == 0
    assert limiter.get_remaining("user1", 61) == 1  # First expired


def test_single_request_limit():
    limiter = RateLimiter(max_requests=1, window_seconds=10)
    assert limiter.allow_request("user1", 0) == True
    assert limiter.allow_request("user1", 5) == False
    assert limiter.allow_request("user1", 10) == False
    assert limiter.allow_request("user1", 11) == True


def test_new_user_has_full_allowance():
    limiter = RateLimiter(max_requests=5, window_seconds=60)
    limiter.allow_request("user1", 0)
    limiter.allow_request("user1", 10)
    assert limiter.get_remaining("new_user", 20) == 5


def test_rapid_requests():
    limiter = RateLimiter(max_requests=3, window_seconds=1)
    assert limiter.allow_request("user1", 0) == True
    assert limiter.allow_request("user1", 0) == True
    assert limiter.allow_request("user1", 0) == True
    assert limiter.allow_request("user1", 0) == False
```

---

## Topic Ideas by Concept

### Arrays/Lists
- Remove duplicates preserving order
- Find pairs that sum to target
- Merge sorted arrays
- Rotate array by k positions
- Find missing number in sequence

### Strings
- Validate email/URL/phone format
- Count word frequency
- Find longest palindromic substring
- Parse CSV line with quotes
- Compress string (aaabbc -> a3b2c1)

### Hash Maps
- Group items by property
- Find first non-repeating character
- Two sum / three sum variations
- LRU Cache implementation
- Anagram grouping

### Classes/OOP
- Shopping cart with discounts
- Bank account with transaction history
- Task scheduler with priorities
- Event emitter / pub-sub
- State machine implementation

### Data Processing
- Filter and transform records
- Aggregate statistics
- Merge overlapping intervals
- Topological sort of dependencies
- Pagination with cursor
