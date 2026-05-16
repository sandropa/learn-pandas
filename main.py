import random

from db import get_exercises_for_level, init_db, seed_db
from levels import LEVELS
from repl import run_repl
from ui import _heavy_rule, render_banner, render_exercise

MAX_LEVEL = max(LEVELS)


def _continue():
    response = input("  Press Enter to continue...")
    print()
    _heavy_rule()
    return response.strip().lower() in ("q", "quit", "exit")


def main():
    init_db()
    seed_db()
    render_banner()

    level = 1

    while True:
        exercises = get_exercises_for_level(level)
        random.shuffle(exercises)

        streak = 0
        failed = []
        outcome = None

        for data in exercises:
            render_exercise(data, level, streak, len(failed), 0)
            result = run_repl(data)

            if result == "quit":
                outcome = "quit"
                break

            if result == "solved":
                streak += 1
            else:
                streak = 0
                failed.append(data)
                if len(failed) > 3:
                    outcome = "fail"
                    if _continue():
                        outcome = "quit"
                    break

            if _continue():
                outcome = "quit"
                break

            if streak >= 3:
                break

        if outcome == "quit":
            break

        if outcome is None and failed:
            for i, data in enumerate(failed):
                render_exercise(data, level, 3, len(failed), i)
                result = run_repl(data)

                if result == "quit":
                    outcome = "quit"
                    break

                if result != "solved":
                    outcome = "fail"
                    if _continue():
                        outcome = "quit"
                    break

                if _continue():
                    outcome = "quit"
                    break

        if outcome == "quit":
            break

        if outcome is None:
            outcome = "pass"

        if outcome == "pass":
            if level < MAX_LEVEL:
                level += 1
        else:
            if level > 1:
                level -= 1


if __name__ == "__main__":
    main()
