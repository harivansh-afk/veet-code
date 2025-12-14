#!/usr/bin/env bash
set -e

REPO="harivansh-afk/veet-code"
INSTALL_DIR="$HOME/.veetcode"
CLAUDE_COMMANDS="$HOME/.claude/commands"

echo "Installing veetcode..."

# Check for uv
if ! command -v uv &> /dev/null; then
    echo "Installing uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.local/bin:$PATH"
fi

# Clone or update
if [ -d "$INSTALL_DIR" ]; then
    echo "Updating existing installation..."
    cd "$INSTALL_DIR" && git pull
else
    echo "Cloning repository..."
    git clone "https://github.com/$REPO.git" "$INSTALL_DIR"
fi

cd "$INSTALL_DIR"
uv sync

# Create symlink for CLI
mkdir -p "$HOME/.local/bin"
ln -sf "$INSTALL_DIR/veet" "$HOME/.local/bin/veet"

# Install Claude slash commands
if [ -d "$HOME/.claude" ]; then
    echo "Installing Claude slash commands..."
    mkdir -p "$CLAUDE_COMMANDS"
    for cmd in "$INSTALL_DIR/.claude/commands"/veet-*.md; do
        ln -sf "$cmd" "$CLAUDE_COMMANDS/$(basename "$cmd")"
    done
    echo "  ✓ /veet-generate, /veet-hint, /veet-explain, /veet-add-tests"
fi

echo ""
echo "✓ veetcode installed!"
echo ""
echo "Commands:"
echo "  veet                    Launch TUI"
echo "  veet open               Open problem in \$EDITOR"
echo "  veet list               List all problems"
echo "  cd \$(veet problems-dir) Navigate to problems"
echo ""
echo "Claude slash commands:"
echo "  /veet-generate          Generate a new problem"
echo "  /veet-hint              Get a hint"
echo "  /veet-explain           Explain the solution"
echo "  /veet-add-tests         Add more test cases"
echo ""
echo "Make sure ~/.local/bin is in your PATH:"
echo '  export PATH="$HOME/.local/bin:$PATH"'
