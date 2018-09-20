# Contributing

Welcome! Thank you for taking the time to contribute. This project relies on an active and involved community, and we really appreciate your support.

## Quickstart

1. Look for an [existing issue](https://github.com/fedora-infra/fpdc/issues)
   about the bug or feature you're interested in. If you can't find an existing issue,
   create a [new one](https://github.com/fedora-infra/fpdc/issues/new).

2. Fork the [repository on GitHub](https://github.com/fedora-infra/fpdc).

3. Fix the bug or add the feature, and then write one or more tests which show
   the bug is fixed or the feature works.

4. Submit a pull request and wait for a maintainer to review it.

More detailed guidelines to help ensure your submission goes smoothly are
below.

## Guidelines

### Python Support

fpdc supports Python 3.6 version. This is automatically enforced by the continuous integration (CI) suite.

### Code Style

We follow the [PEP8](https://www.python.org/dev/peps/pep-0008/) style guide
for Python. This is automatically enforced by the CI suite.

We are using [Black](https://github.com/ambv/black) to automatically format
the source code. It is also checked in CI. The Black webpage contains
instructions to configure your editor to run it on the files you edit.

Note : The max line length is configured to be 100.

### Tests

The test suites can be run using [tox](http://tox.readthedocs.io/) by simply
running ``tox`` from the repository root. We aim for all code to have test coverage or
be explicitly marked as not covered using the ``# no-qa`` comment. We encourage the [Test
Driven Development Practice](http://www.extremeprogramming.org/rules/testfirst.html)

Your pull request should contain tests for your new feature or bug fix. If
you're not certain how to write tests, we will be happy to help you.
