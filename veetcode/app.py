"""Veetcode TUI - Terminal-based LeetCode practice with auto-testing."""

from __future__ import annotations

import json
import re
import subprocess
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path

from textual import work
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical, VerticalScroll
from textual.screen import Screen
from textual.widgets import Footer, Header, OptionList, RichLog, Static
from textual.widgets.option_list import Option


# ─────────────────────────────────────────────────────────────────────────────
# Data
# ─────────────────────────────────────────────────────────────────────────────


@dataclass(frozen=True)
class Problem:
    name: str
    difficulty: str
    path: Path

    @property
    def solution_file(self) -> Path:
        return self.path / "solution.py"


@dataclass
class TestCase:
    name: str
    passed: bool
    error: str = ""
    input_line: str = ""  # The function call with inputs
    expected: str = ""
    actual: str = ""


@dataclass
class SolutionStats:
    lines: int = 0
    code_lines: int = 0
    functions: int = 0
    complexity_hint: str = ""


@dataclass
class TestResult:
    passed: bool
    output: str
    test_cases: list[TestCase] = field(default_factory=list)
    total: int = 0
    failed_count: int = 0
    passed_count: int = 0
    execution_time_ms: float = 0.0


def strip_ansi(text: str) -> str:
    """Remove ANSI escape codes from text."""
    return re.sub(r"\x1b\[[0-9;]*m", "", text)


def find_repo_root(start: Path | None = None) -> Path:
    cur = (start or Path.cwd()).resolve()
    for p in (cur, *cur.parents):
        if (p / "pyproject.toml").exists():
            return p
    return cur


def load_solved(path: Path) -> set[str]:
    if path.exists():
        try:
            return set(json.loads(path.read_text()))
        except (json.JSONDecodeError, TypeError):
            pass
    return set()


def save_solved(path: Path, solved: set[str]) -> None:
    path.write_text(json.dumps(sorted(solved)))


def scan_problems(problems_dir: Path) -> list[Problem]:
    problems: list[Problem] = []
    for difficulty in ("easy", "medium", "hard"):
        diff_dir = problems_dir / difficulty
        if not diff_dir.exists():
            continue
        for problem_dir in sorted(diff_dir.iterdir()):
            if problem_dir.is_dir() and (problem_dir / "solution.py").exists():
                problems.append(
                    Problem(name=problem_dir.name, difficulty=difficulty, path=problem_dir)
                )
    return problems


def analyze_solution(solution_file: Path) -> SolutionStats:
    stats = SolutionStats()
    if not solution_file.exists():
        return stats
    try:
        code = solution_file.read_text()
        lines = code.split("\n")
        stats.lines = len(lines)
        for line in lines:
            stripped = line.strip()
            if stripped and not stripped.startswith("#"):
                stats.code_lines += 1
            if stripped.startswith("def "):
                stats.functions += 1

        # Simple complexity hints
        hints = []
        if "for " in code and "for " in code[code.find("for ") + 4:]:
            hints.append("O(n²)")
        elif "while " in code or "for " in code:
            hints.append("O(n)")
        if "sorted(" in code or ".sort(" in code:
            hints.append("sort")
        stats.complexity_hint = ", ".join(hints[:2]) if hints else "—"
    except Exception:
        pass
    return stats


def parse_pytest_output(output: str) -> tuple[list[TestCase], float]:
    """Parse pytest output to extract test results with detailed failure info."""
    test_cases: list[TestCase] = []
    total_time = 0.0

    # Strip ANSI codes for reliable parsing
    clean = strip_ansi(output)

    # Match: tests.py::ClassName::test_name or tests.py::test_name PASSED/FAILED
    for match in re.finditer(r"tests\.py::(?:\w+::)?(\w+)\s+(PASSED|FAILED)", clean):
        test_cases.append(TestCase(
            name=match.group(1),
            passed=match.group(2) == "PASSED"
        ))

    # Extract timing from summary like "4 passed in 0.12s"
    time_match = re.search(r"in\s+([\d.]+)s", clean)
    if time_match:
        total_time = float(time_match.group(1)) * 1000

    # Parse failure blocks for detailed info
    # Split by test failure headers like "_______ TestClass.test_name _______"
    failure_blocks = re.split(r"_{10,}\s+[\w.]+\s+_{10,}", clean)
    
    for block in failure_blocks[1:]:  # Skip the part before first failure
        # Extract test name from the block
        name_match = re.search(r"in\s+(\w+)\n", block)
        if not name_match:
            continue
        test_name = name_match.group(1)
        
        # Find the input/function call from the test
        # Look for either: "assert func(...) == ..." OR "result = func(...)" pattern
        input_line = ""
        lines_list = block.split('\n')
        for i, line in enumerate(lines_list):
            stripped = line.strip()
            # Skip E lines (pytest error output)
            if stripped.startswith('E'):
                continue
            # Pattern 1: Single-line assertion with function call
            # e.g., "assert two_sum([2,7], 9) == [0,1]"
            if stripped.startswith('assert') and '(' in stripped and '==' in stripped:
                # Extract the function call part (left side of ==)
                match = re.match(r'assert\s+(.+?)\s*==', stripped)
                if match:
                    call = match.group(1).strip()
                    # Unwrap sorted/list/set wrappers to show actual call
                    inner = re.search(r'(?:sorted|list|set|tuple)\((.+)\)$', call)
                    input_line = inner.group(1) if inner else call
                    break
            # Pattern 2: Two-line format - "result = func(...)" followed by "assert result"
            if '=' in stripped and not stripped.startswith('assert') and '(' in stripped:
                # This looks like "result = func(...)"
                match = re.search(r'=\s*(.+\(.*\))', stripped)
                if match:
                    input_line = match.group(1).strip()
                    break
        
        # Extract actual and expected from AssertionError/assert lines
        actual = ""
        expected = ""
        
        # Find lines with assert comparisons (either "AssertionError: assert X == Y" or "E   assert X == Y")
        for line in block.split('\n'):
            if 'assert' in line and '==' in line and line.strip().startswith('E'):
                # Split on == to get actual and expected
                parts = line.split('==', 1)
                # actual is after "assert " and before ==
                actual_match = re.search(r'assert\s+(.+)$', parts[0])
                if actual_match:
                    actual = actual_match.group(1).strip()
                if len(parts) > 1:
                    expected = parts[1].strip()
                break
        
        # Update the matching test case
        for tc in test_cases:
            if tc.name == test_name and not tc.passed:
                tc.input_line = input_line[:200]  # Truncate if too long
                tc.expected = expected[:100]
                tc.actual = actual[:100]
                tc.error = f"expected {expected}, got {actual}" if expected else ""
                break

    # Fallback: parse summary line for counts if no individual tests found
    if not test_cases:
        passed_match = re.search(r"(\d+)\s+passed", clean)
        failed_match = re.search(r"(\d+)\s+failed", clean)
        if passed_match or failed_match:
            passed_count = int(passed_match.group(1)) if passed_match else 0
            failed_count = int(failed_match.group(1)) if failed_match else 0
            for i in range(passed_count):
                test_cases.append(TestCase(name=f"test_{i+1}", passed=True))
            for i in range(failed_count):
                test_cases.append(TestCase(name=f"test_{passed_count+i+1}", passed=False))

    return test_cases, total_time


def run_tests(problem_path: Path) -> TestResult:
    tests_file = problem_path / "tests.py"
    if not tests_file.exists():
        return TestResult(passed=False, output="No tests.py found")

    try:
        start = time.perf_counter()
        result = subprocess.run(
            [sys.executable, "-m", "pytest", "tests.py", "-v", "--tb=short", "--no-header"],
            cwd=problem_path,
            capture_output=True,
            text=True,
            timeout=30,
        )
        elapsed = (time.perf_counter() - start) * 1000
        output = result.stdout + result.stderr

        test_cases, parsed_time = parse_pytest_output(output)
        passed_count = sum(1 for tc in test_cases if tc.passed)
        failed_count = len(test_cases) - passed_count

        return TestResult(
            passed=result.returncode == 0,
            output=output,
            test_cases=test_cases,
            total=len(test_cases),
            passed_count=passed_count,
            failed_count=failed_count,
            execution_time_ms=parsed_time or elapsed,
        )
    except subprocess.TimeoutExpired:
        return TestResult(passed=False, output="Timeout (30s)")
    except Exception as e:
        return TestResult(passed=False, output=str(e))


# ─────────────────────────────────────────────────────────────────────────────
# Screens
# ─────────────────────────────────────────────────────────────────────────────


class ProblemListScreen(Screen):
    BINDINGS = [
        Binding("q", "quit", "Quit"),
        Binding("r", "rescan", "Rescan"),
        Binding("j", "cursor_down", show=False),
        Binding("k", "cursor_up", show=False),
    ]

    def __init__(self) -> None:
        super().__init__()
        self.repo_root = find_repo_root()
        self.problems_dir = self.repo_root / "problems"
        self.solved_file = self.repo_root / ".solved.json"
        self.problems: list[Problem] = []
        self.solved: set[str] = set()

    def compose(self) -> ComposeResult:
        yield Header()
        yield Vertical(
            Static("veetcode", id="title"),
            OptionList(id="problem-list"),
            id="main-container",
        )
        yield Footer()

    def on_mount(self) -> None:
        self.load_problems()
        self.query_one("#problem-list", OptionList).focus()

    def load_problems(self) -> None:
        self.problems = scan_problems(self.problems_dir)
        self.solved = load_solved(self.solved_file)

        ol = self.query_one("#problem-list", OptionList)
        ol.clear_options()

        if not self.problems:
            ol.add_option(Option("[dim]No problems found[/dim]", disabled=True))
            return

        for p in self.problems:
            diff_colors = {
                "easy": "[green]Easy[/green]",
                "medium": "[yellow]Medium[/yellow]",
                "hard": "[red]Hard[/red]",
            }
            diff = diff_colors.get(p.difficulty, "?")
            check = "[green]✓[/green] " if p.name in self.solved else "  "
            ol.add_option(Option(f"{check}{diff} {p.name}", id=p.name))

    def action_rescan(self) -> None:
        self.load_problems()
        self.notify("Rescanned")

    def action_quit(self) -> None:
        self.app.exit()

    def action_cursor_down(self) -> None:
        self.query_one("#problem-list", OptionList).action_cursor_down()

    def action_cursor_up(self) -> None:
        self.query_one("#problem-list", OptionList).action_cursor_up()

    def on_option_list_option_selected(self, event: OptionList.OptionSelected) -> None:
        for p in self.problems:
            if p.name == event.option.id:
                self.app.push_screen(WatchScreen(p, self.solved_file, self.solved))
                break


class WatchScreen(Screen):
    BINDINGS = [
        Binding("escape", "back", "Back"),
        Binding("r", "rerun", "Rerun"),
        Binding("q", "quit", "Quit"),
        Binding("j", "scroll_down", show=False),
        Binding("k", "scroll_up", show=False),
    ]

    def __init__(self, problem: Problem, solved_file: Path, solved: set[str]) -> None:
        super().__init__()
        self.problem = problem
        self.solved_file = solved_file
        self.solved = solved
        self.watcher = None

    def compose(self) -> ComposeResult:
        yield Header()
        yield Vertical(
            Static(f"{self.problem.name} ({self.problem.difficulty})", id="problem-title"),
            Horizontal(
                Vertical(
                    Static("", id="summary-status"),
                    VerticalScroll(Static("", id="test-summary"), id="summary-scroll"),
                    id="summary-pane",
                ),
                Vertical(
                    Static("", id="stats-content"),
                    id="stats-pane",
                ),
                id="info-row",
            ),
            RichLog(id="output", highlight=True, markup=True),
            id="watch-container",
        )
        yield Footer()

    def on_mount(self) -> None:
        self._update_stats()
        self.run_tests_async()
        self.start_watcher()
        self.query_one("#output", RichLog).focus()

    def on_unmount(self) -> None:
        self.stop_watcher()

    def _update_stats(self) -> None:
        stats = analyze_solution(self.problem.solution_file)
        self.query_one("#stats-content", Static).update(
            f"Lines: {stats.lines} ({stats.code_lines} code)\n"
            f"Functions: {stats.functions}\n"
            f"Complexity: {stats.complexity_hint}"
        )

    def start_watcher(self) -> None:
        from watchdog.events import FileSystemEventHandler
        from watchdog.observers import Observer

        screen = self

        class Handler(FileSystemEventHandler):
            def on_modified(self, event):
                if event.src_path.endswith("solution.py"):
                    screen.app.call_from_thread(screen._on_file_change)

        self.watcher = Observer()
        self.watcher.schedule(Handler(), str(self.problem.path), recursive=False)
        self.watcher.start()

    def _on_file_change(self) -> None:
        self._update_stats()
        self.run_tests_async()

    def stop_watcher(self) -> None:
        if self.watcher:
            self.watcher.stop()
            self.watcher.join(timeout=1)
            self.watcher = None

    @work(thread=True, exclusive=True)
    def run_tests_async(self) -> None:
        self.app.call_from_thread(
            lambda: self.query_one("#summary-status", Static).update("Running...")
        )
        result = run_tests(self.problem.path)
        self.app.call_from_thread(self._display_result, result)

    def _display_result(self, result: TestResult) -> None:
        # Status line
        time_str = f"{result.execution_time_ms:.0f}ms"
        if result.passed:
            status = f"[green]✓ {result.total} passed[/green] ({time_str})"
            self.solved.add(self.problem.name)
            save_solved(self.solved_file, self.solved)
        else:
            status = f"[red]✗ {result.failed_count}/{result.total} failed[/red] ({time_str})"
        self.query_one("#summary-status", Static).update(status)

        # Test list with clean separation and input display
        lines = []
        for tc in result.test_cases:
            if tc.passed:
                lines.append(f"[green]✓[/green] {tc.name}")
            else:
                lines.append(f"[red]✗[/red] [bold]{tc.name}[/bold]")
                # Show input/expected/actual for failed tests
                if tc.input_line:
                    lines.append(f"  [dim]Input:[/dim]    {tc.input_line}")
                if tc.expected:
                    lines.append(f"  [dim]Expected:[/dim] [green]{tc.expected}[/green]")
                if tc.actual:
                    lines.append(f"  [dim]Got:[/dim]      [red]{tc.actual}[/red]")
                lines.append("")  # Blank line for separation
        
        # Remove trailing blank line
        while lines and lines[-1] == "":
            lines.pop()
        
        self.query_one("#test-summary", Static).update("\n".join(lines) or "No tests")

        # Verbose output with clean formatting
        out = self.query_one("#output", RichLog)
        out.clear()
        if result.output:
            # Add visual separators for readability
            out.write("[dim]─" * 60 + "[/dim]")
            out.write(result.output)
        else:
            out.write("No output")

    def action_back(self) -> None:
        self.stop_watcher()
        self.app.pop_screen()

    def action_rerun(self) -> None:
        self._update_stats()
        self.run_tests_async()

    def action_quit(self) -> None:
        self.stop_watcher()
        self.app.exit()

    def action_scroll_down(self) -> None:
        self.query_one("#output", RichLog).scroll_down()

    def action_scroll_up(self) -> None:
        self.query_one("#output", RichLog).scroll_up()


# ─────────────────────────────────────────────────────────────────────────────
# App
# ─────────────────────────────────────────────────────────────────────────────


class VeetcodeApp(App):
    CSS_PATH = "veetcode.tcss"
    TITLE = "veetcode"

    def on_mount(self) -> None:
        self.theme = "gruvbox"
        self.push_screen(ProblemListScreen())
        self.auto_update()

    @work(thread=True)
    def auto_update(self) -> None:
        """Silently update veetcode in background."""
        import subprocess
        repo = Path(__file__).parent.parent
        try:
            subprocess.run(
                ["git", "pull", "--quiet"],
                cwd=repo,
                capture_output=True,
                timeout=10,
            )
            subprocess.run(
                ["uv", "sync", "--quiet"],
                cwd=repo,
                capture_output=True,
                timeout=30,
            )
        except Exception:
            pass  # Silently fail - don't disrupt user


def run_app() -> None:
    VeetcodeApp().run()


if __name__ == "__main__":
    run_app()
