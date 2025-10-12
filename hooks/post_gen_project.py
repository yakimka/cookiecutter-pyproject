"""
This module is called after project is created.

From pydanny's cookiecutter-django:
https://github.com/pydanny/cookiecutter-django

"""

import os
import textwrap

# Get the root project directory:
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
PROJECT_NAME = "{{ cookiecutter.project_name }}"
LINTER = "{{ cookiecutter.linter }}"
DEPENDENCY_UPDATER = "{{ cookiecutter.dependency_updater }}"
MINIMUM_PYTHON_VERSION = "{{ cookiecutter.minimum_python_version }}"
MAXIMUM_PYTHON_VERSION = "{{ cookiecutter.maximum_python_version }}"


def print_further_instructions():
    """Shows user what to do next after project creation."""
    message = """
    Your project {0} is created.
    Now you can start working on it:

        cd {0}
    """
    print(textwrap.dedent(message.format(PROJECT_NAME)))  # noqa: WPS421


def apply_flake_dependencies_to_pre_commit_config():
    """Add flake8 dependencies to pre-commit config."""
    indent = " " * 10
    with open("requirements.flake8.txt", "r") as requirements_file:
        requirements = [
            f'{indent}"{line.strip()}",'  # noqa: E231
            for line in requirements_file
            if not line.startswith("#")
        ]
    with open(".pre-commit-config.yaml", "r") as pre_commit_config:
        pre_commit_config_content = pre_commit_config.read()

    marker = f"{indent}# Insert flake8 additional dependencies here"
    new_config = pre_commit_config_content.replace(marker, "\n".join(requirements))
    with open(".pre-commit-config.yaml", "w") as pre_commit_config:
        pre_commit_config.write(new_config)

    os.remove("./requirements.flake8.txt")


def finalize_pyproject_toml():
    with open("pyproject.toml", "r") as fp:
        content = fp.read()

    content = content.replace("cookiecutter.project_name", PROJECT_NAME)
    content = content.replace("'true'", "true")
    content = content.replace("'false'", "false")
    content = content.replace(
        'requires-python = ">=3.10,<4.0.0"',
        f'requires-python = ">={MINIMUM_PYTHON_VERSION},<4.0.0"',
    )
    content = content.replace(
        '  "Programming Language :: Python :: 3",',
        _generate_py_version_classifier(),
    )

    with open("pyproject.toml", "w") as fp:
        fp.write(content)


def finalize_ci_config():
    with open(".github/workflows/workflow-ci.yml", "r") as fp:
        content = fp.read()

    content = content.replace(
        "python-version: ['3']",
        f"python-version: {_python_versions_list()!r}",
    )

    with open(".github/workflows/workflow-ci.yml", "w") as fp:
        fp.write(content)


def remove_files():
    """Remove unnecessary files."""
    if LINTER == "ruff":
        os.remove("./setup.cfg")
    if DEPENDENCY_UPDATER in ("dependabot", "none"):
        os.remove("./.github/renovate.json")
    if DEPENDENCY_UPDATER in ("renovate", "none"):
        os.remove("./.github/dependabot.yml")


def _generate_py_version_classifier() -> str:
    versions = ["3", *_python_versions_list()]
    classifiers = [
        f'  "Programming Language :: Python :: {version}",' for version in versions
    ]
    return "\n".join(classifiers)


def _python_versions_list() -> list[str]:
    min_version = int(MINIMUM_PYTHON_VERSION.split(".")[1])
    max_version = int(MAXIMUM_PYTHON_VERSION.split(".")[1])
    return [f"3.{version}" for version in range(min_version, max_version + 1)]


finalize_pyproject_toml()
finalize_ci_config()
apply_flake_dependencies_to_pre_commit_config()
print_further_instructions()
remove_files()
