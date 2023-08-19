SHELL:=/usr/bin/env bash

POETRY_RUN=poetry run

.PHONY: all
all: help

.PHONY: pre-commit
pre-commit:
	poetry run pre-commit $(args)

.PHONY: lint
lint:  ## Run flake8, mypy, other linters and verify formatting
	@make pre-commit args="run --all-files"
	@make mypy

.PHONY: mypy
mypy:  ## Run mypy
	$(POETRY_RUN) mypy

.PHONY: unit
unit:  ## Run unit tests
	$(POETRY_RUN) pytest --cov
	$(POETRY_RUN) pytest --dead-fixtures

.PHONY: package
package:  ## Run packages (dependencies) checks
	poetry check
	$(POETRY_RUN) pip check

.PHONY: test
test: lint package unit  ## Run linting and tests

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
