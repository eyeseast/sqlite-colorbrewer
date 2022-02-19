# sqlite-colorbrewer

[![PyPI](https://img.shields.io/pypi/v/sqlite-colorbrewer.svg)](https://pypi.org/project/sqlite-colorbrewer/)
[![Changelog](https://img.shields.io/github/v/release/eyeseast/sqlite-colorbrewer?include_prereleases&label=changelog)](https://github.com/eyeseast/sqlite-colorbrewer/releases)
[![Tests](https://github.com/eyeseast/sqlite-colorbrewer/workflows/Test/badge.svg)](https://github.com/eyeseast/sqlite-colorbrewer/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/eyeseast/sqlite-colorbrewer/blob/main/LICENSE)

A custom function to use [ColorBrewer](https://colorbrewer2.org/) scales in SQLite queries.

Colors are exported from [here](https://colorbrewer2.org/export/colorbrewer.json).

## Installation

To install as a Python library and use with the [standard SQLite3 module](https://docs.python.org/3/library/sqlite3.html):

    pip install sqlite-colorbrewer

To install this plugin in the same environment as Datasette.

    datasette install sqlite-colorbrewer

## Usage

If you're using this library with Datasette, it will be automatically registered as a plugin and available for use in SQL queries, like so:

```sql
SELECT colorbrewer('Blues', 9, 0);
```

That will return a single value: `"rgb(247,251,255)"`

To use with a SQLite connection outside of Datasette, use the `register` function:

```python
>>> import sqlite3
>>> import sqlite_colorbrewer

>>> conn = sqlite3.connect(':memory')
>>> sqlite_colorbrewer.register(conn)

>>> cursor = conn.execute("SELECT colorbrewer('Blues', 9, 0);")
>>> result = next(cursor)
>>> print(result)
rgb(247,251,255)
```

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:

    cd sqlite-colorbrewer
    python3 -mvenv venv
    source venv/bin/activate

Or if you are using `pipenv`:

    pipenv shell

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest

To build `sqlite_colorbrewer/colorbrewer.py`:

    ./json_to_python.py
    black . # to format the resulting file

## ColorBrewer

Copyright (c) 2002 Cynthia Brewer, Mark Harrower, and The Pennsylvania State University.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

See the [ColorBrewer updates](http://www.personal.psu.edu/cab38/ColorBrewer/ColorBrewer_updates.html) for updates to copyright information.
