.PHONY: install install-dev serve serve-dev lint format test converage help

install:
	# uv pip install -e .
	pip install -r requirements.txt

install-dev:
	# uv pip install -e ".[dev]"
	pip install -r requirements-dev.txt

serve:
	# uv run server.py
	python server.py

serve-dev:
	# uv run server.py --reload
	python server.py --reload

lint:
	# uv run black --check .
	black --check .

format:
	# uv run black .
	black .

test:
	# uv run pytest tests
	pytest tests

coverage:
	# uv run coverage run -m pytest
	coverage run -m pytest
	coverage report

help:
	python server.py --help
