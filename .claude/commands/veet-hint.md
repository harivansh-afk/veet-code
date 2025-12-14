---
description: Get a hint for the current problem without spoiling the solution
argument-hint: [problem-name]
---

# Get a Hint

The user needs a hint for a problem they're working on.

## Problem to hint on
Problem name: $ARGUMENTS (if empty, ask which problem they need help with)

## How to give hints

1. First, read the problem's solution.py to understand what they're solving
2. Give hints in progressive levels - start vague, get more specific only if asked

### Hint Levels:

**Level 1 - Conceptual** (give first):
- What data structure would be useful here?
- What's the key insight or pattern?
- Example: "Think about how you could avoid checking every pair..."

**Level 2 - Approach** (if they ask for more):
- General algorithm approach without code
- Time/space complexity target
- Example: "A hash map could let you check in O(1) if you've seen a complement..."

**Level 3 - Pseudocode** (if still stuck):
- Step-by-step logic without actual code
- Key operations to perform
- Example: "For each element: calculate what you need, check if you've seen it, store current..."

## Rules
- NEVER show the actual solution code
- NEVER give away the answer directly
- Ask if they want more specific hints after each level
- Encourage them to try implementing after each hint

## Find the problem
First, find the veetcode problems directory:
```bash
VEET_DIR=$(veet problems-dir 2>/dev/null || echo "$HOME/.veetcode/problems")
```

Then read: $VEET_DIR/*/$ARGUMENTS/solution.py (find the matching problem directory)
