# yakimka/cookiecutter-pyproject

[![Build status](https://github.com/yakimka/cookiecutter-pyproject/workflows/test/badge.svg?branch=master&event=push)](https://github.com/yakimka/cookiecutter-pyproject/actions?query=workflow%3Atest)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/yakimka/cookiecutter-pyproject/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)

[`Cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) template to create new python packages.

---

## Purpose

This project is used to scaffold a `python` package or project structure.


## Features

- Always [`up-to-date`](https://github.com/yakimka/cookiecutter-pyproject/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot) dependencies with the help of [`@dependabot`](https://dependabot.com/)
- Supports latest `python3.10+`
- [`poetry`](https://github.com/python-poetry/poetry) for managing dependencies
- [`mypy`](https://mypy.readthedocs.io) for optional static typing
- [`pytest`](https://github.com/pytest-dev/pytest) for testing
- `flake8` for linting
- `Github Actions` as the default CI
- [`pre-commit`](https://pre-commit.com/) for running checks before committing (run `pre-commit install` to install git hook)



## Installation

Firstly, you will need to install dependencies:

```bash
pip install cookiecutter
```

Then, create a project itself:

```bash
cookiecutter gh:yakimka/cookiecutter-pyproject
```

In order for the github actions to work smoothly (ie badge), you must, during the setup, use your github username in the `organization` field.
```bash
project_name [my-awesome-project]: foo-project
organization [yakimka]: <github_username>
```


## CI/CD

For properly running CI/CD, you must set the following environment secrets in repo settings:

- `DOCKERHUB_TOKEN`
- `PYPI_TOKEN`
- `CODECOV_TOKEN`

Also you need to duplicate these secrets to Dependabot settings
if you want to run pipelines on Dependabot PRs.


## License

MIT. See [LICENSE](https://github.com/yakimka/cookiecutter-pyproject/blob/master/LICENSE) for more details.


## Credits

Project inspired by:

- [cookiecutter template](https://github.com/wemake-services/wemake-python-package)
- [Dockerfile](https://github.com/python-poetry/poetry/discussions/1879#discussioncomment-216865)
