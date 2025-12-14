---
description: Generate a new practice problem with tests
argument-hint: [difficulty] [topic]
allowed-tools: Write, Bash(mkdir:*)
---

# Generate a New Practice Problem

You are generating a practical implementation problem for veetcode - a terminal-based coding practice tool.

## Arguments Provided
- Difficulty: $1 (if empty, ask user to choose: easy, medium, or hard)
- Topic: $2 (if empty, ask user what concept/topic they want to practice)

## Problem Style Guide

Generate **practical implementation** problems, NOT abstract LeetCode puzzles:

### DO:
- Use real-world business context (e.g., "You are building a payment system...")
- Provide clear function signatures with type hints
- Include 2-3 concrete examples with explanations
- List explicit constraints
- Focus on practical skills: data transformation, validation, API-like operations

### DON'T:
- Create pure algorithmic puzzles without context
- Use abstract mathematical framing
- Make problems that feel like textbook exercises

## Difficulty Calibration

**Easy** (15-25 min):
- Single data structure (list, dict, set)
- 1-2 core concepts
- 3-4 test cases
- ~20-30 lines solution

**Medium** (30-40 min):
- Multiple data structures
- 3-4 concepts (sorting, hash maps, two pointers)
- 5-6 test cases including edge cases
- ~40-60 lines solution

**Hard** (45-60 min):
- Custom classes or complex data structures
- 5+ concepts (DP, graphs, sliding window + state)
- 7-10 test cases with tricky edge cases
- ~80+ lines solution

## Output Format

### 1. First, confirm with the user:
- The difficulty level
- The topic/concept
- A one-line problem summary

### 2. Generate the problem name
Create a kebab-case name (e.g., `validate-transactions`, `rate-limiter`, `word-frequency`)

### 3. Create the directory
```bash
mkdir -p problems/{difficulty}/{problem-name}
```

### 4. Create solution.py

Structure:
```python
"""
{Problem Title}

{Story-based description in 2-3 sentences with real-world context}

Example 1:
    Input: {param1} = {value1}, {param2} = {value2}
    Output: {expected}
    Explanation: {why this is the answer}

Example 2:
    Input: {param1} = {value1}, {param2} = {value2}
    Output: {expected}

Constraints:
    - {constraint 1}
    - {constraint 2}
    - {constraint 3}
"""


def {function_name}({params_with_types}) -> {return_type}:
    """{One-line docstring describing what to return}."""
    pass  # Your implementation here
```

### 5. Create tests.py

Structure:
```python
import pytest
from solution import {function_name}


def test_basic_case():
    """Test the example from the problem description."""
    assert {function_name}(...) == ...


def test_another_case():
    """Test another typical case."""
    assert {function_name}(...) == ...


def test_edge_case_empty():
    """Test empty or minimal input."""
    assert {function_name}(...) == ...


def test_edge_case_boundary():
    """Test boundary conditions."""
    assert {function_name}(...) == ...


# Add more tests based on difficulty:
# Easy: 3-4 tests
# Medium: 5-6 tests
# Hard: 7-10 tests
```

## Example Problems by Topic

**Arrays/Lists**: frequency counting, deduplication, sliding window, two pointers
**Strings**: parsing, validation, transformation, pattern matching
**Hash Maps**: grouping, caching, lookup optimization
**Trees/Graphs**: traversal, path finding, hierarchy operations
**OOP Design**: class design, state management, encapsulation
**Data Processing**: ETL operations, aggregation, filtering pipelines

## After Generation

Tell the user:
1. The path to their new problem: `problems/{difficulty}/{problem-name}/`
2. How to start practicing: `uv run veetcode` then select the problem
3. The file to edit: `solution.py`

Now, let's generate a problem! If difficulty or topic weren't provided, ask the user to choose.
