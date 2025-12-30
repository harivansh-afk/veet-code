# Veetcode

[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](#)
[![Last Commit](https://img.shields.io/github/last-commit/harivansh-afk/veet-code)](https://github.com/harivansh-afk/veet-code/commits/main)
[![Repo Size](https://img.shields.io/github/repo-size/harivansh-afk/veet-code)](https://github.com/harivansh-afk/veet-code)
[![Release](https://img.shields.io/github/v/release/harivansh-afk/veet-code?display_name=release&sort=date)](https://github.com/harivansh-afk/veet-code/releases/latest)

Built for vim users who enjoy claude code, ghostty panes and TUIs

<img width="1800" height="1169" alt="image" src="https://github.com/user-attachments/assets/d28c2acb-edcb-4d14-8155-e09d65d14a6b" />

**Requires:** [uv](https://docs.astral.sh/uv/) and [Claude Code](https://claude.ai/code) (for problem generation)

- Browse problems by difficulty (easy/medium/hard)
- Auto-run tests on file write
- Claude code slash command to generate problems, tests on demand

## Install

```bash
curl -fsSL https://raw.githubusercontent.com/harivansh-afk/veet-code/main/install.sh | bash
```

Then run:

```bash
veet
```

<details>
<summary>Manual install</summary>

```bash
git clone https://github.com/harivansh-afk/veet-code.git
cd veet-code
uv sync
./veet install-commands  # optional: install Claude slash commands
./veet
```

</details>

## Quick Start

```bash
veet                    # Launch TUI (first time: no problems yet)
# In Claude: /veet-generate easy arrays
veet open               # Opens solution.py in vim/nvim
# Edit, save → tests auto-run in TUI
```

## Workflow

1. Generate a problem: `/veet-generate` (in Claude Code)
2. `veet` — opens TUI with problem list
3. Select a problem, press Enter
4. `veet open` — edit solution in your editor (nvim/vim)
5. Save — tests run automatically in TUI

## Keys

|   Key    | Action          |
|----------|-----------------|
| `j/k`    | Navigate        |
| `Enter`  | Select          |
| `Esc`    | Back            |
| `r`      | Rerun tests     |
| `q`      | Quit            |
| `Ctrl+P` | Command palette |

## CLI Commands

```bash
veet                    # Launch TUI
veet open               # Open a problem in $EDITOR (vim)
veet open two-sum       # Open specific problem
veet list               # List all problems  
veet update             # Update to latest version
veet install-commands   # Install Claude slash commands
cd $(veet problems-dir) # cd to problems folder
```

## Generate Problems

Use Claude slash commands (works anywhere after install):

- `/veet-generate` — create a new problem
- `/veet-hint` — get a hint
- `/veet-explain` — explain the solution
- `/veet-add-tests` — add more test cases

## Themes

Gruvbox by default. Change via `Ctrl+P` → "Change theme".
