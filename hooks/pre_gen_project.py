import re
import sys

PROJECT_REGEX = r"^[a-z][a-z0-9\-_]+[a-z0-9]$"
PROJECT_NAME = "{{ cookiecutter.project_name }}"
MODULE_NAME = "{{ cookiecutter.module_name }}"
MAX_LINE_LENGTH = "{{ cookiecutter.max_line_length }}"
MINIMUM_PYTHON_VERSION = "{{ cookiecutter.minimum_python_version }}"
MAXIMUM_PYTHON_VERSION = "{{ cookiecutter.maximum_python_version }}"


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


def validate_max_line_length():
    try:
        max_length = int(MAX_LINE_LENGTH)
    except ValueError:
        raise ValueError("ERROR: The max line length must be an integer.")
    if not 79 <= max_length <= 120:
        message = [
            "ERROR: The max line length {0} is not a valid option.",
            "Valid values are between 79 and 120.",
        ]
        raise ValueError(" ".join(message).format(MAX_LINE_LENGTH))


def validate_python_version():
    _check_py_version(MINIMUM_PYTHON_VERSION)
    _check_py_version(MAXIMUM_PYTHON_VERSION)
    if MINIMUM_PYTHON_VERSION > MAXIMUM_PYTHON_VERSION:
        message = [
            "ERROR: The minimum python version {0} is greater than",
            "the maximum python version {1}.",
        ]
        raise ValueError(
            " ".join(message).format(MINIMUM_PYTHON_VERSION, MAXIMUM_PYTHON_VERSION)
        )


def _check_py_version(version: str) -> None:
    pattern = r"^3\.[1-9]\d$"
    if not re.match(pattern, version):
        message = [
            "ERROR: The python version {0} is not a valid option.",
            "Valid versions are from 3.10 to 3.99",
        ]
        raise ValueError(" ".join(message).format(version))


validators = (
    validate_project_name,
    validate_module_name,
    validate_max_line_length,
    validate_python_version,
)

for validator in validators:
    try:
        validator()
    except ValueError as ex:
        print(ex)
        sys.exit(1)
