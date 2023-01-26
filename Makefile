.DEFAULT_GOAL := install-dev

default: init install-dev

.PHONY: init
init:
	python -m pip install --upgrade pip wheel setuptools build

.PHONY: install
install:
	python -m pip install --upgrade .

.PHONY: install-dev
install-dev:
	python -m pip install --upgrade --editable .[dev,tests,docs]

.PHONY: lint
lint:
	python -m isort src/
	python -m black src/

.PHONY: pylint
pylint:
	python -m pylint src/

.PHONY: test
test:
	python -m pytest

.PHONY: build-dist
build-dist:
	python -m pip install --upgrade build
	python -m build

.PHONY: clean
clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -rf {} +
	find . -name '.mypy_cache' -exec rm -rf {} +
	rm -rf .tox
	rm -f coverage.xml
	rm -f coverage.json
	rm -rf htmlcov
	rm -rf .coverage
	rm -rf .coverage.*
	find . -name '.pytest_cache' -exec rm -rf {} +
	rm -rf dist
	rm -rf build
