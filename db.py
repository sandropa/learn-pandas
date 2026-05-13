import os
import sqlite3

from levels import LEVELS

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "exercises.db")

SCHEMA = """\
CREATE TABLE IF NOT EXISTS exercises (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    statement TEXT NOT NULL,
    solution_code TEXT NOT NULL,
    hint TEXT,
    level INTEGER DEFAULT 1,
    category TEXT
);

CREATE TABLE IF NOT EXISTS exercise_tables (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    exercise_id INTEGER NOT NULL REFERENCES exercises(id),
    name TEXT NOT NULL,
    display_csv TEXT NOT NULL,
    test_csv TEXT NOT NULL,
    sort_order INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS exercise_expected (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    exercise_id INTEGER NOT NULL REFERENCES exercises(id),
    display_expected_csv TEXT NOT NULL,
    test_expected_csv TEXT NOT NULL
);
"""


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    conn.executescript(SCHEMA)
    conn.commit()
    conn.close()


def seed_db():
    conn = get_connection()

    total_expected = sum(len(exs) for exs in LEVELS.values())
    total_actual = conn.execute("SELECT COUNT(*) FROM exercises").fetchone()[0]
    if total_actual == total_expected:
        conn.close()
        return

    conn.execute("DELETE FROM exercise_expected")
    conn.execute("DELETE FROM exercise_tables")
    conn.execute("DELETE FROM exercises")

    for level, exercises in LEVELS.items():
        for ex in exercises:
            cursor = conn.execute(
                "INSERT INTO exercises (statement, solution_code, hint, level, category) "
                "VALUES (?, ?, ?, ?, ?)",
                (ex["statement"], ex["solution_code"], ex["hint"], level, ex["category"]),
            )
            ex_id = cursor.lastrowid
            for i, tbl in enumerate(ex["tables"]):
                conn.execute(
                    "INSERT INTO exercise_tables (exercise_id, name, display_csv, test_csv, sort_order) "
                    "VALUES (?, ?, ?, ?, ?)",
                    (ex_id, tbl["name"], tbl["display_csv"], tbl["test_csv"], i),
                )
            conn.execute(
                "INSERT INTO exercise_expected (exercise_id, display_expected_csv, test_expected_csv) "
                "VALUES (?, ?, ?)",
                (ex_id, ex["display_expected_csv"], ex["test_expected_csv"]),
            )

    conn.commit()
    conn.close()


def get_exercises_for_level(level):
    conn = get_connection()
    rows = conn.execute(
        "SELECT * FROM exercises WHERE level = ? ORDER BY id", (level,)
    ).fetchall()
    if not rows:
        rows = conn.execute(
            "SELECT * FROM exercises WHERE level = 1 ORDER BY id"
        ).fetchall()

    exercises = []
    for row in rows:
        exercise = dict(row)
        tables = [
            dict(r)
            for r in conn.execute(
                "SELECT * FROM exercise_tables WHERE exercise_id = ? ORDER BY sort_order",
                (exercise["id"],),
            ).fetchall()
        ]
        expected = dict(
            conn.execute(
                "SELECT * FROM exercise_expected WHERE exercise_id = ?",
                (exercise["id"],),
            ).fetchone()
        )
        exercises.append({"exercise": exercise, "tables": tables, "expected": expected})

    conn.close()
    return exercises
