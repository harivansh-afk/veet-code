# Veetcode

Built for people vim users who enjoy claude code, ghostty panes and TUIs

- Browse problems by difficulty (easy/medium/hard)
- Auto-run tests on file write
- Claude code slash command to generate problems, tests on demand

## Installation

```bash
git clone https://github.com/harivansh-afk/veetcode.git
cd veetcode
uv sync
```

## Run

```bash
./veet
```

## Workflow

1. `./veet` — opens problem list
2. Select a problem, press Enter
3. Edit `solution.py` in your editor
4. Save — tests run automatically
5. Repeat

## Keys

|   Key    | Action          |
|----------|-----------------|
| `j/k`    | Navigate        |
| `Enter`  | Select          |
| `Esc`    | Back            |
| `r`      | Rerun tests     |
| `q`      | Quit            |
| `Ctrl+P` | Command palette |

## Generate Problems

Use Claude Code slash commands in `.claude/commands/`:

- `/generate` — create a new problem
- `/hint` — get a hint
- `/explain` — explain the solution
- `/add-tests` — add more test cases

## Themes

Gruvbox by default. Change via `Ctrl+P` → "Change theme".
