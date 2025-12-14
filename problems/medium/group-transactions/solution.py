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

