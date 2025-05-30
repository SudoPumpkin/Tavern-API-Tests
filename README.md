
# Tavern API Tests

This repository contains API tests and utility scripts for API validation using [Tavern](https://tavern.dev/) and Python.

## Getting Started

### 1. Set up a Python 3.11 virtual environment

```sh
python3.11 -m venv venv311
source venv311/bin/activate
```

### 2. Install dependencies

```sh
pip install --upgrade pip
pip install 'tavern[pytest]'
pip install requests
```

### 3. Run Tavern API tests

```sh
pytest
# or run a specific test file:
pytest tests/test_api.tavern.yaml
```

### 4. Run Python scripts

To run a utility script (e.g., book details fetcher):

```sh
python tests/book_details.py
```


## Makefile Usage

This repository includes a `Makefile` with helpful commands for common tasks:

| Command         | Description                                      |
|----------------|--------------------------------------------------|
| `make test`    | Run all Tavern API tests                         |
| `make python`  | Run all Python scripts in the `tests/` directory |
| `make env-reset` | Rebuild the Python 3.11 virtual environment and install dependencies |
| `make env-reenter` | Print a message and activate the virtualenv in the current shell |
| `make env-shell` | Spawn a new shell with the virtualenv activated |

**Examples:**

```sh
# Run all Tavern tests
make test

# Run all Python scripts in tests/
make python

# Rebuild the virtual environment and install requirements
make env-reset

# Enter a shell with the virtualenv activated
make env-shell
```

## Project Structure

- `tests/` - Contains Tavern YAML test files and Python scripts
  - `test_*.tavern.yaml` - Tavern API test cases
  - `book_details.py` - Example Python script for API calls and validation
- `.vscode/` - VS Code workspace settings (auto-formatting, YAML custom tags)
- `venv311/` - Python 3.11 virtual environment (not tracked by git)

## Documentation

- This README contains instructions on how to run the tests and scripts.
- For more details, see the [Tavern Documentation](https://tavern.dev/).
