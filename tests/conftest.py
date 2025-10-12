import pytest


@pytest.fixture()
def context():
    """Creates default prompt values."""
    return {
        "project_name": "test-project",
        "module_name": "test_project",
        "project_description": "Custom description",
        "github_username": "custom-org",
        "dockerhub_username": "myusername",
    }
