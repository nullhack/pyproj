# Running

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
