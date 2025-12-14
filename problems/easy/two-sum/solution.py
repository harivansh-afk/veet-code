"""
Two Sum

You are a cashier at a busy store. A customer wants to pay exactly
a target amount using exactly two items from their basket.

Given a list of item prices and a target total, find the indices
of the two items that add up to the target.

Example 1:
    Input: prices = [2, 7, 11, 15], target = 9
    Output: [0, 1]
    Explanation: prices[0] + prices[1] = 2 + 7 = 9

Example 2:
    Input: prices = [3, 2, 4], target = 6
    Output: [1, 2]

Constraints:
    - 2 <= len(prices) <= 10^4
    - Each price is a positive integer
    - Exactly one solution exists
"""


def two_sum(prices: list[int], target: int) -> list[int]:
    """Return indices of two prices that add up to target."""
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] + prices[j] == target:
                return [i,j]
