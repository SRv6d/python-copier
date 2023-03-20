import os

import nox

CI = bool(os.getenv("CI"))
PYTHON = "{{ python_version.versions | join(', ') }}".split(", ") if not CI else None
LINT_LOCATIONS = "src", "tests", "noxfile.py"
SESSIONS = "ruff", "mypy", "tryceratops", "pytest"

nox.options.sessions = SESSIONS


@nox.session(python=PYTHON)
def ruff(session) -> None:
    """Code Style linting using ruff."""
    session.run("pdm", "install", "--no-self", external=True)

    if session.posargs:
        session.run("ruff", *session.posargs, *LINT_LOCATIONS)
    else:
        session.run("ruff", *LINT_LOCATIONS)

@nox.session(python=PYTHON)
def black(session) -> None:
    """Check if style adheres to black."""
    session.run("pdm", "install", "--no-self", external=True)
    session.run("black", "--check", *LINT_LOCATIONS)

@nox.session(python=PYTHON)
def mypy(session) -> None:
    """Static type checking using mypy."""
    session.run("pdm", "install", "--no-self", external=True)
    session.run("mypy", *LINT_LOCATIONS)

@nox.session(python=PYTHON)
def pytest(session) -> None:
    """Run pytest tests."""
    session.run("pdm", "install", "--no-self", external=True)
    session.run("pytest", "--cov", "tests/unit")

@nox.session(python=PYTHON)
def safety(session) -> None:
    """Scan dependencies for known security vulnerabilities using safety."""
    session.run("pdm", "install", "--no-self", external=True)
    requirements_file = session.poetry.export_requirements()
    session.run("safety", "check", f"--file={requirements_file}", "--full-report")

@nox.session(python=PYTHON)
def codecov(session) -> None:
    """Upload codecov coverage data."""
    session.run("pdm", "install", "--no-self", external=True)
    session.run("coverage", "xml", "--fail-under=0")
    session.run("codecov", "-f", "coverage.xml")
