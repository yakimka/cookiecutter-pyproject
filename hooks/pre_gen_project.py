import re
import sys

PROJECT_REGEX = r"^[a-z][a-z0-9\-_]+[a-z0-9]$"
PROJECT_NAME = "{{ cookiecutter.project_name }}"
MODULE_NAME = "{{ cookiecutter.module_name }}"
LINTER = "{{ cookiecutter.linter }}"


def validate_project_name():
    """
    This validator is used to ensure that `project_name` is valid.
    Valid inputs starts with the lowercase letter.
    Followed by any lowercase letters, numbers or underscores.
    Valid example: `school_project3`.
    """
    if not re.match(PROJECT_REGEX, PROJECT_NAME):
        # Validates project's module name:
        message = [
            "ERROR: The project slug {0} is not a valid name.",
            "Start with a lowercase letter.",
            "Followed by any lowercase",
            "letters, numbers, slashes, or dashes (-).",
        ]
        raise ValueError(" ".join(message).format(PROJECT_NAME))


def validate_module_name():
    if MODULE_NAME != MODULE_NAME.lower().replace("-", "_"):
        message = [
            "ERROR: The module name {0} is invalid.",
            "Module name must be lowercase and",
            "and consist of letters, numbers, slashes, or slashes (_).",
        ]
        raise ValueError(" ".join(message).format(MODULE_NAME))


def validate_linter():
    valid_linters = ("ruff", "flake8")
    if LINTER not in valid_linters:
        message = [
            "ERROR: The linter {0} is not a valid option.",
            "Choose one of the following: ruff, flake8",
        ]
        raise ValueError(" ".join(message).format(LINTER))


validators = (
    validate_project_name,
    validate_module_name,
    validate_linter,
)

for validator in validators:
    try:
        validator()
    except ValueError as ex:
        print(ex)
        sys.exit(1)
