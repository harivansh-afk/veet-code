---
description: Generate a new practice problem with tests
argument-hint: [difficulty] [topic]
allowed-tools: Write, Bash(mkdir:*), Bash(cd:*), Bash(python:*), Bash(rm:*)
---

# Generate a New Practice Problem

**Reference**: @.claude/problem-examples.md for consistent formatting and quality examples.

You are generating a practical implementation problem for veetcode.

## Arguments Provided
- Difficulty: $1 (if empty, ask user to choose: easy, medium, or hard)
- Topic: $2 (if empty, ask user what concept/topic they want to practice)

## Generation Workflow

### Step 1: Gather Requirements
If arguments not provided, ask user:
1. Difficulty: easy, medium, or hard
2. Topic/concept they want to practice
3. Confirm with a one-line problem summary before proceeding

### Step 2: Design the Problem (in your head)
Before writing any files, mentally design:
- The problem scenario (real-world context)
- Function signature with types
- The ACTUAL SOLUTION (keep this secret - never write to files)
- Test cases that verify the solution
- Edge cases

### Step 3: Create Directory
First, find the veetcode problems directory:
```bash
VEET_DIR=$(veet problems-dir 2>/dev/null || echo "$HOME/.veetcode/problems")
mkdir -p "$VEET_DIR/{difficulty}/{problem-name}"
```

All file operations should use `$VEET_DIR/{difficulty}/{problem-name}/` as the base path.

### Step 4: Write solution.py (SKELETON ONLY)
Write ONLY the skeleton - never include the solution!

```python
"""
{Problem Title}

{Story-based description in 2-3 sentences with real-world context.
Frame it as a real task: "You're building...", "Your team needs...", etc.}

Example 1:
    Input: {param1} = {value1}, {param2} = {value2}
    Output: {expected}
    Explanation: {brief explanation}

Example 2:
    Input: {param1} = {value1}, {param2} = {value2}
    Output: {expected}

Constraints:
    - {constraint 1}
    - {constraint 2}
    - {constraint 3}
"""


def {function_name}({params}: {types}) -> {return_type}:
    """{One-line description of what to return}."""
    pass  # Your implementation here
```

### Step 5: Write tests.py (CONSISTENT FORMAT)

Follow this EXACT format for all tests. **CRITICAL: Use single-line assertions so the TUI can show inputs!**

```python
"""Tests for {problem_name}."""
import pytest
from solution import {function_name}


class TestBasicCases:
    """Test basic functionality with typical inputs."""

    def test_example_one(self):
        """Test first example from problem description."""
        # ALWAYS use single-line assert with function call inline
        assert {function_name}(input1, input2) == expected_output

    def test_example_two(self):
        """Test second example from problem description."""
        assert {function_name}(input1, input2) == expected_output

    def test_typical_case(self):
        """Test another common case."""
        assert {function_name}(input1, input2) == expected_output


class TestEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_empty_input(self):
        """Test with empty or minimal input."""
        assert {function_name}([]) == []  # or appropriate empty case

    def test_single_element(self):
        """Test with single element input."""
        assert {function_name}([1]) == expected

    def test_boundary_values(self):
        """Test boundary conditions."""
        assert {function_name}(boundary_input) == expected


# IMPORTANT TEST FORMAT RULES:
# 1. ALWAYS use single-line assertions: assert func(args) == expected
# 2. NEVER use: result = func(); assert result == expected (hides inputs in TUI)
# 3. If output order doesn't matter, wrap in sorted(): assert sorted(func(...)) == sorted([...])
# 4. Keep assertions simple - avoid 'or' conditions, use separate tests instead
#
# Test count by difficulty:
# Easy: 4-5 tests (2 basic, 2-3 edge)
# Medium: 6-8 tests (3 basic, 3-5 edge)
# Hard: 8-12 tests (4 basic, 4-8 edge)
```

### Step 6: VERIFY TESTS WORK (CRITICAL)

You MUST verify the tests are solvable before telling the user. Run this verification using inline Python - DO NOT write the solution to any file:

```bash
cd "$VEET_DIR/{difficulty}/{problem-name}" && python -c "
import sys
from types import ModuleType

# Define the actual solution INLINE (user cannot see this)
def {function_name}({params}):
    # YOUR SOLUTION HERE - implement it fully
    ...

# Create a fake 'solution' module
solution_module = ModuleType('solution')
solution_module.{function_name} = {function_name}
sys.modules['solution'] = solution_module

# Run pytest
import pytest
exit_code = pytest.main(['tests.py', '-v'])
sys.exit(exit_code)
"
```

If tests FAIL:
- Fix the tests (not the solution approach)
- Re-run verification
- Do NOT proceed until all tests pass

If tests PASS:
- Proceed to tell user the problem is ready

### Step 7: Confirm to User

Only after verification passes, tell the user:

```
✅ Problem created and verified!

📁 Location: $VEET_DIR/{difficulty}/{problem-name}/
📝 Open: veet open {problem-name}
🚀 Run: veet → select "{problem-name}"

Good luck!
```

## Problem Style Guide

### DO:
- Real-world business context ("You're building a payment API...")
- Clear function signatures with type hints
- 2-3 concrete examples with explanations
- Explicit constraints
- Practical skills: data transformation, validation, business logic

### DON'T:
- Abstract algorithmic puzzles without context
- Mathematical framing ("Given an array of integers...")
- Textbook exercise style
- Overly complex for the difficulty level

## Difficulty Calibration

**Easy** (15-25 min):
- Single data structure (list, dict, set)
- 1-2 concepts
- 4-5 test cases
- ~20-30 line solution

**Medium** (30-40 min):
- Multiple data structures
- 3-4 concepts
- 6-8 test cases
- ~40-60 line solution

**Hard** (45-60 min):
- Custom classes or complex structures
- 5+ concepts
- 8-12 test cases
- ~80+ line solution

## Topic Ideas

- **Arrays**: frequency counting, deduplication, sliding window, two pointers
- **Strings**: parsing, validation, transformation, pattern matching
- **Hash Maps**: grouping, caching, lookup optimization, counting
- **Classes**: state management, encapsulation, business entities
- **Data Processing**: filtering, aggregation, transformation pipelines

Now, let's generate a problem! Ask for difficulty and topic if not provided.
