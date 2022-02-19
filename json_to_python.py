#!/usr/bin/env python3
"""
Turn colorbrewer.json into colorbrewer.py
"""
import json
import pathlib
import sys

heading = """# colorbrewer.py

"""

HERE = pathlib.Path(__file__).parent
SOURCE = HERE / "sqlite_colorbrewer" / "colorbrewer.json"
DEST = HERE / "sqlite_colorbrewer" / "colorbrewer.py"


def main():
    with SOURCE.open() as f, DEST.open("w") as sink:
        source = json.load(f)
        sink.write(heading)
        for scheme, counts in source.items():
            _type = counts.pop("type", None)
            counts = {int(k): v for k, v in counts.items()}
            counts["type"] = _type
            sink.write(f"{scheme} = {counts}\n")


if __name__ == "__main__":
    main()
