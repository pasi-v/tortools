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

To set up the development environment:

1. Install development dependencies:
   ```bash
   poetry install --with dev
   ```

2. Run tests:
   ```bash
   poetry run pytest
   ```

3. Format code:
   ```bash
   poetry run black .
   poetry run isort .
   ```

4. Type checking:
   ```bash
   poetry run mypy .
   ```

## Project Structure

```
tortools/
├── tortools/
│   ├── __init__.py
│   └── cli.py
├── pyproject.toml
├── setup.sh
└── README.md
```

## License

This project is licensed under the terms of the license included in the repository.
