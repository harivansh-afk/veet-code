# Veetcode

Built for people who enjoy programming, vim, claude code, ghostty panes and TUIs

## Features

- Browse problems by difficulty (easy/medium/hard)
- Auto-run tests on file write
- Claude code slash command to generate problems, tests on demand

## Installation

```bash
# Clone the repo
git clone https://github.com/harivansh-afk/veetcode.git
cd veetcode

# Install with uv
uv sync
```

## Usage

```bash
# Launch the TUI
uv run veetcode

# Or if installed globally
veetcode
```

### Workflow

1. Launch the TUI
2. Select a problem with Enter
3. Open `problems/<difficulty>/<name>/solution.py` in your editor
4. Implement the solution
5. Write file - tests run automatically
6. Generate more problems :)