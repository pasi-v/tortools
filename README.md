# The One Ring RPG Tools (tortools)

[![CI](https://github.com/yourusername/tortools/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/yourusername/tortools/actions/workflows/ci.yml)

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

1. Install development dependencies and pre-commit hooks:
   ```bash
   ./scripts/dev.sh install
   ```

   This will:
   - Install all project dependencies
   - Install pre-commit hooks for code quality

### Development Workflow

The project includes a development script (`scripts/dev.sh`) to help with common tasks:

```bash
# Run all checks (format, test, type-check)
./scripts/dev.sh check

# Run tests only
./scripts/dev.sh test

# Run type checking only
./scripts/dev.sh type-check

# Format code
./scripts/dev.sh format

# Show help
./scripts/dev.sh help
```

### Code Quality

This project uses pre-commit hooks to ensure code quality. The hooks will run automatically on each commit and:

- Format code with black
- Sort imports with isort
- Remove trailing whitespace
- Ensure files end with a newline
- Check YAML syntax
- Prevent large files from being committed

To manually run the hooks on all files:
```bash
./scripts/dev.sh format
```

### Testing

The project uses pytest for testing. Tests are located in the `tests/` directory and follow these conventions:

- `test_*.py` files contain test cases
- `conftest.py` contains shared test fixtures
- Tests use a fixed random seed for reproducibility

To run the tests:
```bash
./scripts/dev.sh test
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
