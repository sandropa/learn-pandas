import builtins
import code
import io
import readline  # noqa: F401 — enables arrow keys and history in the REPL
import sys

import numpy as np
import pandas as pd

from rich import box
from rich.console import Console
from rich.table import Table

from ui import print_correct, print_hint, print_incorrect

_console = Console()


class _Solved(SystemExit):
    pass


class _Failed(SystemExit):
    pass


class _Command:
    def __init__(self, fn):
        self._fn = fn

    def __call__(self, *args, **kwargs):
        return self._fn(*args, **kwargs)

    def __repr__(self):
        self._fn()
        return ""


class _TrackingConsole(code.InteractiveConsole):
    def __init__(self, locals=None):
        super().__init__(locals=locals)
        self.last_result = None

    def write(self, data):
        sys.stderr.write("\n")
        for line in data.split("\n"):
            if line:
                sys.stderr.write(f"  \033[31m{line}\033[0m\n")
            else:
                sys.stderr.write("\n")
        sys.stderr.write("\n")

    def runcode(self, code_obj):
        old_displayhook = sys.displayhook
        def hook(value):
            if value is not None and not isinstance(value, _Command):
                self.last_result = value
            if value is not None:
                builtins._ = value
                if isinstance(value, (pd.DataFrame, pd.Series)):
                    df = value.to_frame() if isinstance(value, pd.Series) else value
                    rt = Table(box=box.SIMPLE, show_edge=False, padding=(0, 1))
                    rt.add_column("", style="dim")
                    for col in df.columns:
                        rt.add_column(str(col))
                    for idx, row in df.iterrows():
                        rt.add_row(str(idx), *[str(v) for v in row])
                    print()
                    from rich.padding import Padding
                    _console.print(Padding(rt, (0, 0, 0, 2)))
                    print()
                else:
                    text = repr(value)
                    if text:
                        print()
                        for line in text.split("\n"):
                            print(f"  {line}")
                        print()
        sys.displayhook = hook
        try:
            super().runcode(code_obj)
        finally:
            sys.displayhook = old_displayhook


def run_repl(exercise_data):
    tables = exercise_data["tables"]
    expected = exercise_data["expected"]
    exercise = exercise_data["exercise"]

    ns = {"pd": pd, "np": np}

    for tbl in tables:
        ns[tbl["name"]] = pd.read_csv(io.StringIO(tbl["csv"]))

    expected_df = pd.read_csv(io.StringIO(expected["expected_csv"]))
    solution_code = exercise["solution_code"]

    repl = _TrackingConsole(locals=ns)
    hint_used = False

    def submit(result=None):
        if result is None:
            result = repl.last_result
        if isinstance(result, pd.Series):
            result = result.reset_index()

        if not isinstance(result, pd.DataFrame):
            print_incorrect(solution_code)
            raise _Failed()

        r = result.reset_index(drop=True).copy()
        e = expected_df.reset_index(drop=True).copy()

        if set(r.columns) == set(e.columns):
            r = r[e.columns]

        for col in r.columns:
            if pd.api.types.is_datetime64_any_dtype(r[col]):
                r[col] = r[col].dt.strftime("%Y-%m-%d")
            elif hasattr(r[col], "cat"):
                r[col] = r[col].astype(str)

        r = r.sort_values(by=list(r.columns)).reset_index(drop=True)
        e = e.sort_values(by=list(e.columns)).reset_index(drop=True)

        try:
            pd.testing.assert_frame_equal(r, e, check_dtype=False, atol=0.01)
        except AssertionError:
            print_incorrect(solution_code)
            raise _Failed()

        print_correct(solution_code)
        raise _Solved()

    def hint():
        nonlocal hint_used
        hint_used = True
        print_hint(exercise["hint"])

    def quit_app():
        raise SystemExit()

    def help_text(*args):
        if args:
            builtins.help(*args)
            return
        print("  s / submit      Check last result")
        print("  submit(df)      Check specific answer")
        print("  h / hint        Get a hint")
        print("  help            Show this message")
        print("  help(x)         Python help on x")
        print("  q / exit        Quit")

    submit_cmd = _Command(submit)
    hint_cmd = _Command(hint)
    help_cmd = _Command(help_text)
    quit_cmd = _Command(quit_app)

    ns["submit"] = submit_cmd
    ns["s"] = submit_cmd
    ns["hint"] = hint_cmd
    ns["h"] = hint_cmd
    ns["help"] = help_cmd
    ns["q"] = quit_cmd
    ns["exit"] = quit_cmd
    ns["quit"] = quit_cmd

    try:
        repl.interact(banner="", exitmsg="")
    except _Solved:
        return "hint" if hint_used else "solved"
    except _Failed:
        return "failed"
    except SystemExit:
        return "quit"

    return "quit"
