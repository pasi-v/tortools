# The One Ring RPG Tools (tortools)

A collection of command-line tools for The One Ring RPG game masters, helping with action resolution, combat simulation, and other game mechanics.

## Features

- Skill test resolution with advantage/disadvantage
- Combat simulation (coming soon)
- Character management (coming soon)

## Installation

This project uses Poetry for dependency management. You can install it in two ways:

### Quick Setup (Recommended)

Use the provided setup script which will handle everything automatically:

```bash
# Make the script executable
chmod +x setup.sh

# Run the setup script
./setup.sh
```

The script will:
- Check Python version (requires 3.9+)
- Create a virtual environment
- Install Poetry if not present
- Install all project dependencies

### Manual Installation

If you prefer to install manually:

1. Install Poetry if you haven't already:
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. Clone this repository and install dependencies:
   ```bash
   git clone https://github.com/yourusername/tortools.git
   cd tortools
   poetry install
   ```

## Usage

After installation, you can use the tools through the `tortools` command:

```bash
# Show available commands
poetry run tortools --help

# Resolve a skill test
poetry run tortools resolve-action --skill 3 --tn 14 --advantage

# Get help for a specific command
poetry run tortools resolve-action --help
```

### Available Commands

- `resolve-action`: Resolve a skill test in The One Ring RPG
  - `--skill, -s`: Skill rating of the character (required)
  - `--tn, -t`: Target number for the test (required)
  - `--advantage, -a`: Whether the character has advantage
  - `--disadvantage, -d`: Whether the character has disadvantage

## Development

### Setting Up the Development Environment

1. Install development dependencies:
   ```bash
   poetry install --with dev
   ```

2. Format code:
   ```bash
   poetry run black .
   poetry run isort .
   ```

3. Type checking:
   ```bash
   poetry run mypy .
   ```

### Testing

The project uses pytest for testing. Tests are located in the `tests/` directory and follow these conventions:

- `test_*.py` files contain test cases
- `conftest.py` contains shared test fixtures
- Tests use a fixed random seed for reproducibility

To run the tests:

```bash
# Run all tests
poetry run pytest

# Run tests with verbose output
poetry run pytest -v

# Run a specific test file
poetry run pytest tests/test_mechanics.py

# Run tests with coverage report
poetry run pytest --cov=tortools
```

The test suite includes:
- Input validation tests
- Game mechanics tests
- Edge case handling
- Success/failure scenarios

## Project Structure

```
tortools/
├── tortools/
│   ├── __init__.py
│   ├── cli.py          # Command-line interface
│   └── mechanics.py    # Core game mechanics
├── tests/
│   ├── __init__.py
│   ├── conftest.py     # Test configuration
│   └── test_mechanics.py
├── pyproject.toml
├── setup.sh
└── README.md
```

## License

This project is licensed under the terms of the license included in the repository.
