.PHONY: install lint test train clean

install:
	pip install -e ".[dev]"
	pre-commit install

lint:
	black src/ tests/ scripts/
	isort src/ tests/ scripts/
	flake8 src/ tests/ scripts/

test:
	pytest tests/ -v

train:
	python scripts/train.py

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf .pytest_cache .coverage htmlcov/
