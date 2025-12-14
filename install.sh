#!/usr/bin/env bash
set -e

REPO="harivansh-afk/veet-code"
INSTALL_DIR="$HOME/.veetcode"

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

# Create symlink
mkdir -p "$HOME/.local/bin"
ln -sf "$INSTALL_DIR/veet" "$HOME/.local/bin/veet"

echo ""
echo "✓ veetcode installed!"
echo ""
echo "Run: veet"
echo ""
echo "Make sure ~/.local/bin is in your PATH:"
echo '  export PATH="$HOME/.local/bin:$PATH"'

