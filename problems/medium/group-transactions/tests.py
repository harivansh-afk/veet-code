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

