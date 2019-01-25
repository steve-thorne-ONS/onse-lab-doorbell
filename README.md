# Doorbell Application - the TDD lab

This is the starting project for the TDD lab. Open it in PyCharm and work
through the provided instructions.

## Setup

Make sure you have the latest version of Python installed (currently 3.7.1) from
the [Python website](https://www.python.org/downloads/release/python-371/).

From within the repository folder, please install the following in order to run
the project:

```bash
# install the dependencies from Pipfile:
pipenv install --dev
```

Pipenv "automatically creates and manages a virtualenv for your projects, as well
as adds/removes packages from your Pipfile as you install/uninstall packages. It
also generates the ever-important Pipfile.lock, which is used to produce
deterministic builds." [1](https://pipenv.readthedocs.io/en/latest/)

## Running the Tests

Run the tests as follows:

```bash
pipenv run python -m pytest
```

## PyCharm Run Configuration

Add a run configuration of type `Python tests -> pytest` with the following
settings:

![PyCharm Test Config](pycharm-test-config.png)
