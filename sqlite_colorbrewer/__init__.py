import sqlite3
from . import colorbrewer

try:
    from datasette import hookimpl

    has_datasette = True
except ImportError:
    has_datasette = False


if has_datasette:

    @hookimpl
    def prepare_connection(conn):
        register(conn)


def register(conn):
    conn.create_function("colorbrewer", 3, color, deterministic=True)


def color(scheme, count, n):
    if not hasattr(colorbrewer, scheme):
        raise sqlite3.ProgrammingError(f"No scheme called {scheme}")

    scale = getattr(colorbrewer, scheme).get(count, None)
    if count is None:
        raise sqlite3.ProgrammingError(f"Invalid scheme length: {count}")

    try:
        return scale[n]
    except IndexError:
        return sqlite3.ProgrammingError(f"Index out of range: {n}")
