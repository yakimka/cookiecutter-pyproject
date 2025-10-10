# How to contribute


## Dependencies

We use [uv](https://docs.astral.sh/uv/) to manage the dependencies.

To install them you would need to run `install` command:

```bash
uv sync
```


## One magic command

Run `make checks` to run everything we have!


## Tests

We use `pytest` and `flake8|ruff` for quality control.

To run all tests:

```bash
make test
```

To run linting:

```bash
make lint
```

## Type checks

We use `mypy` to run type checks on our code.
To use it:

```bash
make mypy
```


## Submitting your code

What are the point of this method?

1. We use protected `{{ cookiecutter.main_branch }}` branch,
   so the only way to push your code is via pull request
2. We use issue branches: to implement a new feature or to fix a bug
   create a new branch
3. Then create a pull request to `{{ cookiecutter.main_branch }}` branch
4. We use `git tag`s to make releases, so we can track what has changed
   since the latest release

In this method, the latest version of the app is always in the `{{ cookiecutter.main_branch }}` branch.
