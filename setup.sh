#!/bin/bash

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print status messages
print_status() {
    echo -e "${GREEN}==>${NC} $1"
}

# Function to print error messages
print_error() {
    echo -e "${RED}Error:${NC} $1"
}

# Function to print warning messages
print_warning() {
    echo -e "${YELLOW}Warning:${NC} $1"
}

# Check if Python 3.9+ is installed
if ! command -v python3 &> /dev/null; then
    print_error "Python 3 is not installed. Please install Python 3.9 or higher."
    exit 1
fi

# Check Python version
PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
PYTHON_MAJOR=$(echo $PYTHON_VERSION | cut -d. -f1)
PYTHON_MINOR=$(echo $PYTHON_VERSION | cut -d. -f2)

if [ "$PYTHON_MAJOR" -lt 3 ] || ([ "$PYTHON_MAJOR" -eq 3 ] && [ "$PYTHON_MINOR" -lt 9 ]); then
    print_error "Python 3.9 or higher is required. Found version $PYTHON_VERSION"
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    print_status "Creating virtual environment..."
    python3 -m venv venv
    if [ $? -ne 0 ]; then
        print_error "Failed to create virtual environment"
        exit 1
    fi
fi

# Activate virtual environment
print_status "Activating virtual environment..."
source venv/bin/activate
if [ $? -ne 0 ]; then
    print_error "Failed to activate virtual environment"
    exit 1
fi

# Upgrade pip
print_status "Upgrading pip..."
python -m pip install --upgrade pip
if [ $? -ne 0 ]; then
    print_warning "Failed to upgrade pip, but continuing..."
fi

# Install Poetry if not already installed
if ! command -v poetry &> /dev/null; then
    print_status "Installing Poetry..."
    curl -sSL https://install.python-poetry.org | python3 -
    if [ $? -ne 0 ]; then
        print_error "Failed to install Poetry"
        exit 1
    fi

    # Add Poetry to PATH for current session
    export PATH="$HOME/.local/bin:$PATH"

    # Add Poetry to PATH permanently if not already there
    if [[ ":$PATH:" != *":$HOME/.local/bin:"* ]]; then
        print_status "Adding Poetry to PATH..."
        if [ -f ~/.bashrc ]; then
            echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
        elif [ -f ~/.zshrc ]; then
            echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc
        fi
    fi
else
    print_status "Poetry is already installed"
fi

# Install project dependencies
print_status "Installing project dependencies..."
poetry install
if [ $? -ne 0 ]; then
    print_error "Failed to install project dependencies"
    exit 1
fi

print_status "Setup completed successfully!"
print_status "To activate the virtual environment, run: source venv/bin/activate"
print_status "To start using the tools, run: poetry run tortools --help"
print_status ""
print_status "Note: If you just installed Poetry, you may need to:"
print_status "1. Start a new shell session, or"
print_status "2. Run: source ~/.bashrc (if using bash) or source ~/.zshrc (if using zsh)"
