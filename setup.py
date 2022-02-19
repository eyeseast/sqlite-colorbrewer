from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="sqlite-colorbrewer",
    description="A custom function to use ColorBrewer scales in SQLite queries",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Chris Amico",
    url="https://github.com/eyeseast/sqlite-colorbrewer",
    project_urls={
        "Issues": "https://github.com/eyeseast/sqlite-colorbrewer/issues",
        "CI": "https://github.com/eyeseast/sqlite-colorbrewer/actions",
        "Changelog": "https://github.com/eyeseast/sqlite-colorbrewer/releases",
    },
    license="Apache License, Version 2.0",
    classifiers=[
        "Framework :: Datasette",
        "License :: OSI Approved :: Apache Software License",
    ],
    version=VERSION,
    packages=["sqlite_colorbrewer"],
    entry_points={"datasette": ["sqlite_colorbrewer = sqlite_colorbrewer"]},
    extras_require={"test": ["datasette", "pytest", "pytest-asyncio"]},
    python_requires=">=3.6",
)
