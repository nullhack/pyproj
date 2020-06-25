"""Nox file to automate testing and build."""
import shutil
import tempfile
from pathlib import Path

import toml

import nox
from nox.sessions import Session

versions = ["3.6", "3.7", "3.8"]
venv_backend = "venv"
session_kwargs = {"python": versions, "venv_backend": venv_backend}
one_session_kwargs = {"python": max(versions), "venv_backend": venv_backend}

nox.options.sessions = "black", "behave", "coverage"

pyproject_config = toml.load("pyproject.toml")

include_paths = pyproject_config["tool"]["poetry"]["include"]


def expand_files(paths, ext=".py"):
    """Extract files with specific extension from paths.

    Returns:
        list: A list of files with specific extension
    """
    lf = set()
    for path in paths:
        p = Path(path)
        if p.exists() and p.is_file() and p.suffix == ext:
            lf.add(p)
        else:
            lf.update(p.rglob(f"*{ext}"))
    return lf


python_files = expand_files(include_paths)


class PoetrySession:
    """Provide default arguments to session."""

    def __init__(self, session):
        """Initialize poetry's environments."""
        self.session = session
        self.session.install("poetry")
        self.session.run("poetry", "config", "virtualenvs.create", "true", "--local")
        self.session.run(
            "poetry", "config", "virtualenvs.in-project", "true", "--local"
        )
        self.session.run("poetry", "env", "use", session.python)
        dpath = Path("dist")
        if not dpath.exists():
            self.session.run("poetry", "build", "-f", "wheel", "-n")
        self.dist = next(dpath.rglob("*.whl"))

    def run(self, *args, **kwargs):
        """Provide extra arguments to session.run."""
        if "poetry" not in args:
            args = ("poetry", "run") + args
        self.session.run(*args, **kwargs)

    def install(self, *args, **kwargs):
        """Install using poetry constraints."""
        if not args and not kwargs:
            self.session.install(str(self.dist))
        else:
            with tempfile.NamedTemporaryFile() as requirements:
                self.session.run(
                    "poetry",
                    "export",
                    "--dev",
                    "--format=requirements.txt",
                    f"--output={requirements.name}",
                )
                self.session.install(
                    f"--constraint={requirements.name}", *args, **kwargs
                )


@nox.session(**one_session_kwargs)
def build(session):
    """Initialize poetry's python environments."""
    args = session.posargs or ["-f", "wheel", "-n"]
    session = PoetrySession(session)
    session.run("poetry", "build", *args)


@nox.session(**session_kwargs)
def behave(session: Session) -> None:
    """Build the documentation."""
    session = PoetrySession(session)
    session.install()
    session.install("behave")
    session.install("coverage[toml]")
    session.run("coverage", "run")


@nox.session(**one_session_kwargs)
def coverage(session):
    """Run coverage report."""
    session = PoetrySession(session)
    session.install()
    session.install("behave")
    session.install("coverage[toml]")
    session.run("coverage", "run")
    session.run("coverage", "report")
    session.run("coverage", "html")


@nox.session(**one_session_kwargs)
def xdoctest(session):
    """Run doctests."""
    args = session.posargs or ["all"]
    session = PoetrySession(session)
    session.install()
    session.install("xdoctest")
    session.install("pygments")
    for path in include_paths:
        session.run("xdoctest", path, *args)


@nox.session(**one_session_kwargs)
def black(session):
    """Perform lint on python scripts using black."""
    session = PoetrySession(session)
    for path in include_paths:
        session.run("black", str(path))


@nox.session(**one_session_kwargs)
def safety(session):
    """Perform safety check of installed packages."""
    session = PoetrySession(session)
    session.install("safety")
    session.run("safety", "check")


@nox.session(**one_session_kwargs)
def isort(session):
    """Perform sort of imported packages using isort."""
    session = PoetrySession(session)
    session.install("isort")
    for f in python_files:
        session.run("isort", str(f))


@nox.session(**one_session_kwargs)
def precommit(session):
    """Perform pre-commit checks."""
    session = PoetrySession(session)
    session.install("pre-commit")
    session.run("pre-commit", "run", "--all-files")


@nox.session(**session_kwargs)
def version(session):
    """Show python version being used."""
    session = PoetrySession(session)
    session.run("python", "--version")


@nox.session(**one_session_kwargs)
def mkdocs(session):
    """Generate documentation."""
    args = session.posargs or ["build", "-c"]
    session = PoetrySession(session)

    nox_mkdocs = pyproject_config["nox"]["mkdocs"]
    build_reference = nox_mkdocs.get("build_reference", False)
    clean_reference = nox_mkdocs.get("clean_reference", False)
    build_specification = nox_mkdocs.get("build_specification", False)
    clean_specification = nox_mkdocs.get("clean_specification", False)

    def build_ref(
        path_list,
        ref_docs_path="",
        ext="",
        language="",
        sep="",
        create_files=True,
        clean_before_create=True,
    ):
        docs_path = Path("docs")
        files = expand_files(path_list, ext)

        if clean_before_create and ref_docs_path != "" and "." not in ref_docs_path:
            shutil.rmtree(docs_path / ref_docs_path, ignore_errors=True)

        if create_files:
            for file_path in files:
                filemd_name = file_path.name + ".md"
                path = file_path.parent
                if sep != "":
                    filemd_name = Path(*filemd_name.split(sep))
                d = docs_path / ref_docs_path / path / filemd_name
                d.parent.mkdir(parents=True, exist_ok=True)
                d.touch()
                with open(d, "w") as o:
                    o.write(f"```{language}\n{{!../{file_path}!}}\n```")

    build_ref(
        ["features"],
        "specification",
        ".feature",
        "gherkin",
        "_",
        create_files=build_reference,
        clean_before_create=clean_specification,
    )
    build_ref(
        include_paths,
        "reference",
        ".py",
        "python",
        create_files=build_specification,
        clean_before_create=clean_reference,
    )
    session.install("mkdocs-minify-plugin")
    session.install("markdown")
    session.install("markdown-include")
    session.install("mkdocs-material-extensions")
    session.run("mkdocs", *args)
