# python-project-builder

This project aims to provide some good practices for every Python project template (Documenting, testing, virtual-environment, setuptools). It's inspired on seanfisk's [python-project-template](https://github.com/seanfisk/python-project-template) but aims to be simpler and focus  on Python3.

----

## Quick links
- [Features](#features)
- [Requirements](#requirements)
- [Project Setup](#project-setup)
- [Usage](#usage)
  - [Positional Arguments](#positional-arguments)
  - [Optional Arguments](#optional-arguments)
- [Egg Template](#egg-template)
- [Contribute](#to-contribute)
- [Project Structure](#project-structure)
- [License](#license)

[↑](#python-project-builder)

----

## Features

* [setuptools](https://pypi.python.org/pypi/setuptools): for distribution
* [sphinx](http://www.sphinx-doc.org/en/stable/): for documentation
* [doctest](https://docs.python.org/3/library/doctest.html): for simple testing (for advanced testing consider the use of [pytest](http://docs.pytest.org/) instead)
* [venv](https://docs.python.org/3/library/venv.html): for virtual environment

See Kenneth Reitz's [Hitchhiker's Guide to Python](http://docs.python-guide.org/en/latest/) if you are new to the Python or programming.

[↑](#quick-links)

----

## Requirements

* [python](https://www.python.org/download/releases/3.0/) >= 3.2
* *(optional)* [pip](https://pypi.python.org/pypi/pip/)
* *(optional)* [venv](https://docs.python.org/3/library/venv.html)

[↑](#quick-links)

----

## Project Setup

To download this template:

* **Clone** the template project

If you want to create your own project:

* *(Optional)* Edit **config.ini** file
* **Generate** project files
* Move into the new created **project dir**
* *(Optional)* Change **README** file
* *(Optional)* Create a new **virtual environment**
* *(Optional)* Install project's **requirements-dev** file
* *(Optional)* Generate **documentation**
* *(Optional)* Run the **tests**
* *(Optional)* **Install** the project
* **Run** the project

**Step 1**: Clone the template project:

    git clone https://github.com/nullhack/python-project-builder.git

**Step 2**: *(Optional)* Edit config.ini file to fit your project:

    gedit ./python-project-builder/config.ini

**Step 3**: Generate project files based on egg template dir:

    python3 ./python-project-builder/gen.py

If you've edited conf.ini file or want to use it directly:

    python3 ./python-project-builder/gen.py -c

If you want to generate files in specific DIRNAME:

    python3 ./python-project-builder/gen.py DIRNAME

For a complete list of commands, please see [Usage](#usage) section.

**Step 4**: Move into the new created project DIRNAME:

    cd DIRNAME

**Step 5**: *(Optional)* Change README file with your own text

**Step 6**: *(Optional, but good practice)* Create a new virtual environment (ENV) for your project:

    python3 -m venv ENV
    source ENV/bin/activate

If you want to deactivate the virtual environment:

    deactivate

If you are new to virtual environments, please see the `Virtual Environment section` of Kenneth Reitz's [Hitchhiker's Guide to Python](http://docs.python-guide.org/en/latest/).

**Step 7**: *(Optional)* Install project's requirements-dev file:

    pip3 install -r requirements-dev.txt

**Step 8**: *(Optional)* Generate documentation for new modules:

    sphinx-apidoc -f -o ./docs/source/_apidoc/ ./
    python3 setup.py build_sphinx

The html generated should be in ./docs/build/html

**Step 9**: *(Optional)* Run the tests:

    python3 -m doctest -v ./tests/*

**Step 10**: *(Optional)* Install the project:

    python3 setup.py install

If the project is being developed or you have not set a virtual environment yet:

    python3 setup.py develop

**Step 11**: Run the project:

    python3 main.py

[↑](#quick-links)

----

## Usage:

    gen.py [-h] [-c] [-d] [-e PATH] [-f] [dir_name]

### Positional arguments:

    dir_name             directory where the project will be generated

### Optional arguments:

    -h, --help           show this help message and exit
    -c, --config-file    use config file info instead of asking
    -d, --delete         delete project builder files after project creation
    -e PATH, --egg PATH  specify another egg template to use
    -f, --force          force project deletion if it already exist

[↑](#quick-links)

----

## Egg template

An egg is just a project template or another directory.

Special keywords may be used inside files or names, they will be substituted after project creation.
Keywords may be those defined in config.ini and by license files:

    [config.ini]
    author
    email
    keywords
    license
    package
    project
    python_version
    release
    short_description
    topic_area
    topic_sub_area
    url
    version
    year

    [util.py]
    license_name
    license_description
    license_text

To use keywords, just write the keyword like **${keyword}**.

**E.g.** A file named ${package} whose content is "${short_description} licensed under ${license}".
Using default configuration will generate a file called "package_name" whose content is
"A short description for the project licensed under gpl".

Additional config.ini may be included under egg dir, new keywords will overlap the old.

[↑](#quick-links)

----

## To contribute

The general workflow that GitHub supports is:

* **Fork** this repo to your own account.
* **Clone** the repo to your machine.
* Check out a new **"topic branch"** and make changes.
* **Push** your topic branch to your fork.
* Use the diff viewer on GitHub to create a **pull request** via a discussion.
* Make any requested **changes**.
* The pull request is then **merged** and the "topic branch" is deleted from the upstream (target) repo.

The naming conventions for topic branches are: issue_ID, where the ID  is the ID # of a GitHub issue.

Use official guides:

* https://help.github.com/articles/fork-a-repo/
* https://guides.github.com/activities/forking/

Or the reference [tutorial](https://code.tutsplus.com/tutorials/how-to-collaborate-on-github--net-34267) for this documentation.

Some commands that would complete the workflow above:

**Step 1**: Forking

In the top-right corner of the page, click **Fork Button**

**Step 2**: Cloning

Clone the repo using your own github login (YOUR_USERNAME):

    git clone git@github.com:YOUR_USERNAME/python-project-builder.git

**Step 3**: Adding the Upstream Remote

Change into the directory and then you can add the upstream remote:

    cd python-project-builder
    git remote add upstream git@github.com:nullhack/python-project-builder.git

To pull in changes from the source locally and merge them:

    git fetch upstream
    git merge upstream/master

**Step 4**: Checking Out a Topic Branch

Checkout a topic branch using the issue ID:

    git checkout -b issue_ID

**Step 5**: Committing

**Make your changes** and create a commit that tracks those changes.

    git commit -am "adding some specific change."

**Step 6**: Pushing

Push this topic branch to your own fork of the project.

    git push origin issue_ID

**Step 7**: Creating a Pull Request

Now you may create a pull request:

* Go to your fork of the repo
* Click on issue_ID at  "your recently pushed branches"
* Choose "Compare and Pull Request"

Or:

* Select your branch from the dropdown
* click "Pull Request" or "Compare"

[↑](#quick-links)

----

## Project Structure

    python-project-builder/
    ├── config.ini
    ├── egg
    │   ├── docs
    │   │   ├── make.bat
    │   │   ├── Makefile
    │   │   └── source
    │   │       ├── conf.py
    │   │       └── index.rst
    │   ├── main.py.tpl
    │   ├── MANIFEST.in
    │   ├── ${package}
    │   │   ├── __init__.py.tpl
    │   │   └── metadata.py.tpl
    │   ├── README.md.tpl
    │   ├── requirements-dev.txt
    │   ├── requirements.txt
    │   ├── setup.cfg
    │   ├── setup.py.tpl
    │   └── tests
    │       └── test_metadata.txt.tpl
    ├── gen.py
    ├── LICENSE
    ├── licenses
    │   ├── __init__.py
    │   ├── agpl.py
    │   ├── apache.py
    │   ├── bsd2.py
    │   ├── bsd3.py
    │   ├── gpl.py
    │   ├── lgpl.py
    │   ├── mit.py
    │   ├── mozilla.py
    │   └── util.py
    └── README.md

[↑](#quick-links)

----

## License

This project is released under MIT license.

Copyright (c) 2016 Eric Lopes

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Original license text can be found at the [LICENSE](LICENSE) file.

[↑](#quick-links)

----

**Inspired by**:

* https://github.com/bitprophet/contribution-guide.org
* https://github.com/cjolowicz/hypermodern-python
* https://github.com/tiangolo/fastapi
* https://github.com/sphinx-contrib/napoleon
* https://github.com/carloscuesta/gitmoji
