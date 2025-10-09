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

    with open("pyproject.toml", "w") as fp:
        fp.write(content)


def remove_files():
    """Remove unnecessary files."""
    if LINTER == "ruff":
        os.remove("setup.cfg")


finalize_pyproject_toml()
apply_flake_dependencies_to_pre_commit_config()
print_further_instructions()
