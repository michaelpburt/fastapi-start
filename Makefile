lint:
	isort --profile black --check-only .
	mypy doodlebug
	black . --check --diff

fix-lint:
	isort --profile black
	black . --experimental-string-processing

test-all: lint test

test:
	pytest tests
