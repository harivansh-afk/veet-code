# Veetcode

Built for people vim users who enjoy claude code, ghostty panes and TUIs

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

## CLI Commands

```bash
veet                    # Launch TUI
veet list               # List all problems  
veet install-commands   # Install Claude slash commands
veet path               # Show install location
```

## Generate Problems

Use Claude slash commands (works anywhere after install):

- `/veet-generate` — create a new problem
- `/veet-hint` — get a hint
- `/veet-explain` — explain the solution
- `/veet-add-tests` — add more test cases

## Themes

Gruvbox by default. Change via `Ctrl+P` → "Change theme".
