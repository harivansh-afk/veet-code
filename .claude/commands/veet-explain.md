---
description: Explain the solution approach for a completed problem
argument-hint: [problem-name]
---

# Explain Solution

After the user has solved a problem (or given up), explain the optimal solution approach.

## Problem
Problem name: $ARGUMENTS (if empty, ask which problem)

## Find the problem
First, find the veetcode problems directory:
```bash
VEET_DIR=$(veet problems-dir 2>/dev/null || echo "$HOME/.veetcode/problems")
```

## Process

1. Read their solution.py from $VEET_DIR/*/{problem-name}/ to see their implementation
2. Provide explanation covering:

### For a CORRECT solution:
- Confirm their approach works
- Explain time/space complexity
- Show alternative approaches if any exist
- Mention any optimizations they could make

### For an INCORRECT or INCOMPLETE solution:
- Identify what's wrong without just giving the answer
- Explain the correct approach conceptually
- Walk through the algorithm step by step
- Show the optimal solution with detailed comments

## Explanation Format

```
## Your Approach
{What they did and why it works/doesn't work}

## Optimal Solution
{The best approach with complexity analysis}

## Key Insight
{The "aha" moment or trick that makes this problem tractable}

## Code Walkthrough
{Step-by-step explanation of the solution}

## Similar Problems
{Related concepts to practice}
```
