"""CLI entry point for veetcode."""

import typer
from pathlib import Path

app = typer.Typer(
    name="veetcode",
    help="Terminal-based LeetCode practice with auto-testing",
    add_completion=False,
    invoke_without_command=True,
)


def find_repo_root() -> Path:
    """Find veetcode repo root. Prefers current dir, then script location, then ~/.veetcode."""
    candidates = [
        Path.cwd(),
        Path(__file__).parent.parent,
        Path.home() / ".veetcode",
    ]
    for p in candidates:
        if (p / "problems").exists():
            return p
    return Path(__file__).parent.parent


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context) -> None:
    """Launch the Veetcode TUI."""
    if ctx.invoked_subcommand is None:
        from veetcode.app import run_app
        run_app()


@app.command()
def list() -> None:
    """List all problems."""
    from veetcode.app import scan_problems
    
    repo = find_repo_root()
    problems = scan_problems(repo / "problems")
    solved_file = repo / ".solved.json"
    
    solved: set[str] = set()
    if solved_file.exists():
        import json
        solved = set(json.loads(solved_file.read_text()))
    
    if not problems:
        typer.echo("No problems found.")
        return
    
    for p in problems:
        mark = "✓" if p.name in solved else " "
        diff = {"easy": "E", "medium": "M", "hard": "H"}.get(p.difficulty, "?")
        typer.echo(f"{mark} [{diff}] {p.name}")


@app.command()
def install_commands() -> None:
    """Install Claude slash commands to ~/.claude/commands/"""
    repo = find_repo_root()
    source_dir = repo / ".claude" / "commands"
    target_dir = Path.home() / ".claude" / "commands"
    
    if not source_dir.exists():
        typer.echo(f"Commands not found: {source_dir}")
        raise typer.Exit(1)
    
    target_dir.mkdir(parents=True, exist_ok=True)
    
    count = 0
    for cmd in source_dir.glob("veet-*.md"):
        target = target_dir / cmd.name
        if target.exists() or target.is_symlink():
            target.unlink()
        target.symlink_to(cmd)
        typer.echo(f"  ✓ /{cmd.stem}")
        count += 1
    
    typer.echo(f"\nInstalled {count} commands to {target_dir}")


@app.command()
def uninstall_commands() -> None:
    """Remove Claude slash commands from ~/.claude/commands/"""
    target_dir = Path.home() / ".claude" / "commands"
    
    count = 0
    for cmd in target_dir.glob("veet-*.md"):
        cmd.unlink()
        typer.echo(f"  ✗ /{cmd.stem}")
        count += 1
    
    typer.echo(f"\nRemoved {count} commands")


@app.command()
def open(
    name: str = typer.Argument(None, help="Problem name (e.g., two-sum)"),
) -> None:
    """Open a problem in your editor ($EDITOR or vim)."""
    import os
    import subprocess
    from veetcode.app import scan_problems
    
    repo = find_repo_root()
    problems_dir = repo / "problems"
    problems_dir.mkdir(parents=True, exist_ok=True)
    problems = scan_problems(problems_dir)
    
    editor = os.environ.get("EDITOR", "vim")
    
    # No problems - open the problems directory
    if not problems:
        typer.echo(f"No problems yet. Opening {problems_dir} in {editor}...")
        typer.echo("\nGenerate problems with: /veet-generate (in Claude)")
        subprocess.run([editor, str(problems_dir)])
        return
    
    # If no name given, show list and prompt
    if not name:
        typer.echo("Available problems:\n")
        for i, p in enumerate(problems, 1):
            diff = {"easy": "E", "medium": "M", "hard": "H"}.get(p.difficulty, "?")
            typer.echo(f"  {i}. [{diff}] {p.name}")
        typer.echo()
        choice = typer.prompt("Enter number or name")
        
        # Check if it's a number
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(problems):
                name = problems[idx].name
            else:
                typer.echo("Invalid number")
                raise typer.Exit(1)
        except ValueError:
            name = choice
    
    # Find the problem
    problem = next((p for p in problems if p.name == name), None)
    if not problem:
        typer.echo(f"Problem not found: {name}")
        raise typer.Exit(1)
    
    solution_file = problem.path / "solution.py"
    typer.echo(f"Opening {solution_file} in {editor}...")
    subprocess.run([editor, str(solution_file)])


@app.command()
def path() -> None:
    """Show veetcode installation path."""
    repo = find_repo_root()
    typer.echo(repo)


@app.command()
def problems_dir() -> None:
    """Print the problems directory path (useful for cd)."""
    repo = find_repo_root()
    typer.echo(repo / "problems")


if __name__ == "__main__":
    app()
