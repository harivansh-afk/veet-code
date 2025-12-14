"""CLI entry point for veetcode."""

import typer

from veetcode.app import run_app

app = typer.Typer(
    name="veetcode",
    help="Terminal-based LeetCode practice with auto-testing",
    add_completion=False,
)


@app.command()
def main() -> None:
    """Launch the Veetcode TUI."""
    run_app()


if __name__ == "__main__":
    app()
