"""Noxfile."""

import shutil
from pathlib import Path

import nox

nox.options.default_venv_backend = "none"
nox.options.sessions = ["lints"]


CLEANABLE_TARGETS = [
    "./dist",
    "./build",
    "./.nox",
    "./.coverage",
    "./.coverage.*",
    "./coverage.json",
    "./**/.mypy_cache",
    "./**/.pytest_cache",
    "./**/__pycache__",
    "./**/*.pyc",
    "./**/*.pyo",
]


@nox.session
def install(session: nox.Session) -> None:
    """Install the project."""
    session.run("python", "-m", "pip", "install", "--editable", ".[dev,tests]")


@nox.session
def tests(session: nox.Session) -> None:
    """Run tests."""
    session.run("pytest")


@nox.session
def lints(session: nox.Session) -> None:
    """Run lints."""
    session.run("pre-commit", "run", "--all-files")
    session.run("ruff", "check", "--fix", ".")
    session.run("ruff", "format", ".")
    session.run("mypy", "--strict", "src/")


@nox.session
def clean(_: nox.Session) -> None:
    """Clean cache, .pyc, .pyo, and test/build artifact files from project."""
    count = 0
    for searchpath in CLEANABLE_TARGETS:
        for filepath in Path().glob(searchpath):
            if filepath.is_dir():
                shutil.rmtree(filepath)
            else:
                filepath.unlink()
            count += 1
