#!/usr/bin/env sh

set -o errexit
set -o nounset

# This file is used to setup fake project,
# run tests inside it,
# and remove this project completely.

# Creating a test directory:
mkdir -p ".test" && cd ".test"

# Scaffold the project:
PROJECT_NAME="fake-project"

cookiecutter "$GITHUB_WORKSPACE" \
  --no-input \
  --overwrite-if-exists \
  project_name="$PROJECT_NAME" \
  project_description="My custom app" \
  license="MIT" \
  organization="yakimka"

cd "$PROJECT_NAME"

# Create new venv:
python3 -m venv .venv
. .venv/bin/activate
pip install -U pip

# Testing the project:
POETRY_VIRTUALENVS_CREATE=false poetry install
# create git repo for pre-commit
git init && git add -A
./ci.sh
