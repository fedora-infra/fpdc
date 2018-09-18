# fpdc
> Fedora Product Definition Center

This application aims to provide a single source of truth for the data used during the Fedora distribution release process

## Local Development

fpdc requires Python 3.6.0+ to run. You can setup a local development environment using Python virtual environments.

Create a virtual environment

```
$ python3.6 -m venv .venv
```

Activate the virtual environment

```
$ source .venv/bin/activate
```

First upgrade pip and then install the dependencies

```
$ pip install -U pip
$ pip install -r requirements-dev.txt
```

### Running the tests

You can run the tests with the following command.

```
$ py.test
```

You can also run all the checks (linting, format and licenses) that are validated by the CI pipeline using the tox command.

```
$ tox
```
