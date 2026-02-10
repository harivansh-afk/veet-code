"""
Group Anagrams

You're building a word game assistant that groups words which are
anagrams of each other. Two words are anagrams if they contain
the same letters in any order.

Given a list of strings, group the anagrams together. Each group
should be a sorted list of words, and the groups themselves should
be sorted by their first element.

Example 1:
    Input: words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    Output: [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]
    Explanation: "eat", "tea", and "ate" are all anagrams of each other

Example 2:
    Input: words = ["hello", "world"]
    Output: [["hello"], ["world"]]
    Explanation: No words are anagrams of each other

Example 3:
    Input: words = ["", ""]
    Output: [["", ""]]
    Explanation: Empty strings are anagrams of each other

Constraints:
    - 0 <= len(words) <= 10^4
    - 0 <= len(words[i]) <= 100
    - Words consist of lowercase English letters
    - Each group is sorted alphabetically
    - Groups are sorted by their first element
"""


def group_anagrams(words: list[str]) -> list[list[str]]:
    """Return a list of anagram groups, each sorted, groups sorted by first element."""
    pass  # Your implementation here
