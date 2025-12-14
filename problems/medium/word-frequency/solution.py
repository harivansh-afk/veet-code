"""
Word Frequency Counter

You're building a text analytics tool for a content marketing team.
Given a block of text, return the top N most frequently used words,
sorted by frequency (highest first), then alphabetically for ties.

Example 1:
    Input: text = "the quick brown fox jumps over the lazy dog the fox"
           n = 2
    Output: [("the", 3), ("fox", 2)]
    Explanation: "the" appears 3 times, "fox" appears 2 times

Example 2:
    Input: text = "hello world hello"
           n = 5
    Output: [("hello", 2), ("world", 1)]
    Explanation: Only 2 unique words, return all of them

Constraints:
    - Words are separated by whitespace
    - Case-insensitive (convert to lowercase)
    - Ignore punctuation attached to words
    - n >= 1
    - If fewer than n unique words exist, return all of them
"""


def top_words(text: str, n: int) -> list[tuple[str, int]]:
    """Return top n words by frequency as list of (word, count) tuples."""
    pass  # Your implementation here

