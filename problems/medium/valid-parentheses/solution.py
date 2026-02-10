"""
Valid Parentheses

You're building a syntax checker for a code editor. Before running
any code, the editor needs to verify that all brackets are properly
matched and nested. Given a string containing only parentheses,
square brackets, and curly braces, determine if the input is valid.

A string is valid if:
    - Open brackets are closed by the same type of bracket
    - Open brackets are closed in the correct order
    - Every close bracket has a corresponding open bracket

Example 1:
    Input: s = "([]){}"
    Output: True
    Explanation: All brackets are properly matched and nested

Example 2:
    Input: s = "([)]"
    Output: False
    Explanation: The square bracket closes before the parenthesis

Example 3:
    Input: s = "{{"
    Output: False
    Explanation: Opening braces are never closed

Constraints:
    - 0 <= len(s) <= 10^4
    - s consists only of characters '(){}[]'
"""


def is_valid(s: str) -> bool:
    """Return True if the bracket string is valid, False otherwise."""
    pass  # Your implementation here
