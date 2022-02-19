from datasette.app import Datasette
import pytest
import sqlite3
import sqlite_colorbrewer


@pytest.mark.asyncio
async def test_plugin_is_installed():
    datasette = Datasette([], memory=True)
    response = await datasette.client.get("/-/plugins.json")
    assert response.status_code == 200
    installed_plugins = {p["name"] for p in response.json()}
    assert "sqlite-colorbrewer" in installed_plugins


@pytest.mark.asyncio
async def test_use_plugin():
    datasette = Datasette([], memory=True)
    db = datasette.get_database()
    result = await db.execute("SELECT colorbrewer('Blues', 9, 0);")

    assert result.single_value() == "rgb(247,251,255)"


def test_register_function():
    conn = sqlite3.connect(":memory:")
    sqlite_colorbrewer.register(conn)


def test_query_color():
    conn = sqlite3.connect(":memory:")
    sqlite_colorbrewer.register(conn)

    cursor = conn.execute("SELECT colorbrewer('Blues', 9, 0);")
    result = next(cursor)

    assert result[0] == "rgb(247,251,255)"


def test_errors():
    conn = sqlite3.connect(":memory:")
    sqlite_colorbrewer.register(conn)

    with pytest.raises(sqlite3.OperationalError):
        conn.execute("SELECT colorbrewer('blues', 9, 0);")

    with pytest.raises(sqlite3.OperationalError):
        conn.execute("SELECT colorbrewer('blues', 10, 0);")

    with pytest.raises(sqlite3.OperationalError):
        conn.execute("SELECT colorbrewer('blues', 9, 10);")
