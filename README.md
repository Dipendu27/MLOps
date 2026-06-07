# MLOps

120-day production ML engineering portfolio project.

## Overview

This repository contains a Python package for building and testing reusable
machine learning engineering utilities, scripts, and configuration patterns.

Current focus:

- Project packaging with editable installs
- Utility functions for configs, dataframe validation, statistics, and logging
- Development tooling with Black, isort, Flake8, pytest, and pre-commit
- A training entry point that will expand as the project grows

## Setup

Use Python 3.10 or newer.

```bash
pip install -e ".[dev]"
pre-commit install
```

If `pip` is not available directly, use:

```bash
python -m pip install -e ".[dev]"
```

## Development

Run linting:

```bash
make lint
```

Run tests:

```bash
make test
```

Run the training entry point:

```bash
make train
```

## Project Structure

```text
configs/              Project configuration files
scripts/              CLI-style project entry points
src/ml_engineering/   Python package source code
tests/                Test suite
```
