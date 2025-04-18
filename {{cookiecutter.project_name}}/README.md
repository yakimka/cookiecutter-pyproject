# {{ cookiecutter.project_name }}

[![Build Status](https://github.com/{{ cookiecutter.organization }}/{{ cookiecutter.project_name }}/actions/workflows/workflow-ci.yml/badge.svg?branch={{ cookiecutter.main_branch }}&event=push)](https://github.com/{{ cookiecutter.organization }}/{{ cookiecutter.project_name }}/actions/workflows/workflow-ci.yml)
[![Codecov](https://codecov.io/gh/{{ cookiecutter.organization }}/{{ cookiecutter.project_name }}/branch/{{ cookiecutter.main_branch }}/graph/badge.svg)](https://codecov.io/gh/{{ cookiecutter.organization }}/{{ cookiecutter.project_name }})
[![PyPI - Version](https://img.shields.io/pypi/v/{{ cookiecutter.project_name }}.svg)](https://pypi.org/project/{{ cookiecutter.project_name }}/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_name }})](https://pypi.org/project/picodi/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/{{ cookiecutter.project_name }})](https://pypi.org/project/picodi/)

{{ cookiecutter.project_description }}


## Installation

```bash
pip install {{ cookiecutter.project_name }}
```


## Example

Showcase how your project can be used:

```python
from {{ cookiecutter.module_name }}.example import some_function

print(some_function(3, 4))
# => 7
```

## CI\CD Note (delete this section)

For properly running CI/CD, you must set the following environment secrets in repo settings:

- `DOCKERHUB_TOKEN`
- `PYPI_TOKEN`
- `CODECOV_TOKEN`
- `UPDATE_URL` for [updater](https://github.com/umputun/updater)

## License

[MIT](https://github.com/{{ cookiecutter.organization }}/{{ cookiecutter.project_name }}/blob/{{ cookiecutter.main_branch }}/LICENSE)


## Credits

This project was generated with [`yakimka/cookiecutter-pyproject`](https://github.com/yakimka/cookiecutter-pyproject).
