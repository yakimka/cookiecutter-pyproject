SHELL:=/usr/bin/env bash

POETRY_RUN=poetry run
SRC_DIR=.

.PHONY: all
all: help

.PHONY: lint
lint:  ## Run flake8, mypy, other linters and verify formatting
	@make flake8
	@make mypy
	@make verify_format
	$(POETRY_RUN) doc8 -q docs
	$(POETRY_RUN) yamllint -s .

.PHONY: flake8
flake8:  ## Run flake8
	$(POETRY_RUN) flake8 $(SRC_DIR)

.PHONY: mypy
mypy:  ## Run mypy
	$(POETRY_RUN) mypy $(SRC_DIR)

.PHONY: unit
unit:  ## Run unit tests
	$(POETRY_RUN) pytest
	$(POETRY_RUN) pytest --dead-fixtures

.PHONY: package
package:  ## Run packages (dependencies) checks
	poetry check
	$(POETRY_RUN) pip check
	$(POETRY_RUN) safety check --full-report

.PHONY: test
test: lint package unit  ## Run linting and tests

.PHONY: format
format:  ## Format python files with black and isort
	$(POETRY_RUN) black --preview $(SRC_DIR)
	$(POETRY_RUN) isort $(SRC_DIR)


.PHONY: verify_format
verify_format:  ## Verify python files formatting with black and isort
	$(POETRY_RUN) black --preview --check --diff $(SRC_DIR)
	$(POETRY_RUN) isort --check-only --diff $(SRC_DIR)


.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
