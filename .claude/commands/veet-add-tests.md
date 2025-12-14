---
description: Add more test cases to an existing problem
argument-hint: [problem-name]
allowed-tools: Read, Edit
---

# Add More Test Cases

Add additional test cases to an existing problem to make it more challenging or cover more edge cases.

## Problem
Problem name: $ARGUMENTS (if empty, ask which problem)

## Find the problem
First, find the veetcode problems directory:
```bash
VEET_DIR=$(veet problems-dir 2>/dev/null || echo "$HOME/.veetcode/problems")
```

## Process

1. Read the existing solution.py and tests.py from $VEET_DIR/*/{problem-name}/
2. Analyze what edge cases are NOT covered
3. Ask the user what kind of tests they want:
   - Edge cases (empty, single element, boundaries)
   - Performance tests (large inputs)
   - Tricky cases (duplicates, negative numbers, special characters)
   - Custom scenario they describe

4. Add new test functions to tests.py using the Edit tool

## Test naming convention
```python
def test_edge_case_{description}():
    """Clear description of what this tests."""
    ...

def test_tricky_{description}():
    """Description of the tricky scenario."""
    ...
```

## Do NOT:
- Remove existing tests
- Modify the solution.py
- Add tests that are impossible given the constraints
