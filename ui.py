import io
import textwrap

import pandas as pd
from rich import box
from rich.console import Console
from rich.padding import Padding
from rich.table import Table

console = Console()

def _rule_w():
    return console.width - 4


def _heavy_rule():
    console.print(f"  {'━' * _rule_w()}", style="blue")


def _light_rule():
    console.print(f"  {'─' * _rule_w()}", style="dim")


def render_banner():
    console.print()
    console.print("  [bold blue]PANDAS[/bold blue] [dim]TRAINER[/dim]")
    _heavy_rule()


def render_exercise(data, level, streak, failed_count=0, redeemed=0):
    ex = data["exercise"]
    tables = data["tables"]

    console.print()

    streak_dots = "[yellow]●[/yellow]" * streak + "[dim]○[/dim]" * (3 - streak)
    if failed_count > 0:
        failed_dots = "[yellow]●[/yellow]" * redeemed + "[dim]○[/dim]" * (failed_count - redeemed)
        console.print(f"  [bold blue]LEVEL {level}[/bold blue]  {streak_dots}  {failed_dots}")
    else:
        console.print(f"  [bold blue]LEVEL {level}[/bold blue]  {streak_dots}")
    console.print()

    for line in textwrap.wrap(ex["statement"], width=_rule_w()):
        console.print(f"  {line}")
    console.print()

    rich_tables = []
    for tbl in tables:
        df = pd.read_csv(io.StringIO(tbl["csv"]))
        rt = Table(
            title=tbl["name"],
            title_style="bold yellow",
            title_justify="left",
            box=box.SIMPLE_HEAVY,
            show_edge=False,
            padding=(0, 1),
            expand=False,
        )
        for col in df.columns:
            rt.add_column(col, header_style="yellow")
        for _, row in df.iterrows():
            rt.add_row(*[str(v) for v in row])
        rich_tables.append(rt)

    for rt in rich_tables:
        console.print(Padding(rt, (0, 2, 0, 2)))
        console.print()
    _light_rule()
    console.print()


def print_correct(solution_code):
    w = _rule_w()
    bar = " " * w
    console.print()
    console.print(f"  [bold black on green]{bar}[/bold black on green]")
    console.print()
    console.print(f"  Solution: {solution_code}", highlight=False)
    console.print()


def print_incorrect(solution_code):
    w = _rule_w()
    bar = " " * w
    console.print()
    console.print(f"  [bold black on red]{bar}[/bold black on red]")
    console.print()
    console.print(f"  Solution: {solution_code}", highlight=False)
    console.print()



def print_hint(text):
    console.print()
    prefix = "  ■ "
    for i, line in enumerate(textwrap.wrap(text, width=_rule_w() - 2)):
        if i == 0:
            console.print(f"  [blue bold]●[/blue bold] {line}", highlight=False)
        else:
            console.print(f"    {line}", highlight=False)
    console.print()