# Contributing to FOSS Projects

Contributing to open source is easier than most people may think. It's just matter
of learning a couple of basic tools and concepts. This guide will show some good practices
that most FOSS (free and open source software) follow.

## Submiting issues

Before sending new issues:


* Are you on the **latest version?**
* Have you tried **older versions?**
* Have you searched for **old related issues?**
* Have you tried the project's **mailing list, IRC channel, etc.**?
* If **nothing worked** for you, It's time to create an issue report

## Writing a meaningful issue report

* Which version of the **interpreter** are you using?
* Which **operating system** are you using?
* Which version (tag) of **this project** are you using?
* What are the **steps** to reproduce the issue?

## Contributing changes

### Branching

* It's important to make your changes on a new branch. This makes easy for
the maintainers to add your changes into the main project.
* Always branch off from the main/development branch. Ask if you are not sure.

### Code formating

* Follow the style of the main repository
(e.g. [PEP-8](http://www.python.org/dev/peps/pep-0008/)).
Consistency is the key, always ask if you are not sure.

### Documenting

* Documenting a project relies on some sort of tool (mkdocs, sphinx, pdoc3, etc.),
python projects use docstrings to help making this process easier.
There's a plenty of docstring styles out there (e.g.
[Google](https://github.com/google/styleguide),
[Numpy](https://numpydoc.readthedocs.io/en/latest/format.html), etc.).
Just follow the style of the project you're working on and
ask if you're not sure.

### Testing

* Any good project include tests, if you are working on a bugfix, strive to achieve
100% code coverage and keep diverse set of unit tests using whatever package the
project rely on (e.g. [Pytest](https://docs.pytest.org/en/latest/), [Behave](https://behave.readthedocs.io/en/latest/), [Xdoctest](https://github.com/Erotemic/xdoctest), etc.).

---

## <span style="color:red"><b>Workflow example</b></span>

The following workflow is specific for this project and might not work for other FOSS

### Preparing your Branch

1. Click the button `Fork` on Github. This will create a project with same name inside
your repository list
2. Clone the forked repo: `git clone git@github.com:USERNAME/PROJECT_NAME`
3. On terminal type: `cd PROJECT_NAME`
4. Create a branch: `git checkout -b BRANCH_NAME`

### Creating commits

1. Install the development requirements: `pip install -r dev-requirements.txt`
2. Install the project dependencies under a poetry virtual environment: `poetry install`
3. Activate poetry shell: `poetry shell`
4. Make your changes
5. Run tests, coverage report and pre-commit checks: `nox`
8. Repeat steps `4` and `5` until all tests passed
9. Commit the changes: `gitmoji --commit`

### Creating Pull Requests

1. Push your changes to the forked repo: `git push`
2. Go to Github website and click the button `Pull request`
3. Write a description that explains the changes you've done and steps to reproduce
4. Click submit
5. Invite maintainers to review your code
