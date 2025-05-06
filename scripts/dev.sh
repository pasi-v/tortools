#!/usr/bin/env bash

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored messages
print_message() {
    echo -e "${GREEN}==>${NC} $1"
}

print_error() {
    echo -e "${RED}Error:${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}Warning:${NC} $1"
}

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Function to check if we're in a poetry environment
check_poetry() {
    if ! command_exists poetry; then
        print_error "Poetry is not installed. Please install it first."
        exit 1
    fi
}

# Function to ensure dependencies are installed
ensure_dependencies() {
    if [ ! -d ".venv" ]; then
        print_message "Installing dependencies..."
        poetry install
    fi
}

# Function to run pre-commit hooks
run_pre_commit() {
    ensure_dependencies
    print_message "Running pre-commit hooks..."
    poetry run pre-commit run --all-files
}

# Function to run tests
run_tests() {
    ensure_dependencies
    print_message "Running tests..."
    poetry run pytest
}

# Function to run type checking
run_type_check() {
    ensure_dependencies
    print_message "Running type checking..."
    poetry run mypy .
}

# Function to run all checks
run_all_checks() {
    ensure_dependencies
    print_message "Running all checks..."
    run_pre_commit
    run_tests
    run_type_check
}

# Main script
check_poetry

case "$1" in
    "install")
        print_message "Installing dependencies..."
        poetry install
        print_message "Installing pre-commit hooks..."
        poetry run pre-commit install
        ;;
    "test")
        run_tests
        ;;
    "type-check")
        run_type_check
        ;;
    "format")
        run_pre_commit
        ;;
    "check")
        run_all_checks
        ;;
    "help"|"")
        echo "Development script for tortools"
        echo
        echo "Usage: ./scripts/dev.sh <command>"
        echo
        echo "Commands:"
        echo "  install    Install dependencies and pre-commit hooks"
        echo "  test       Run tests"
        echo "  type-check Run type checking"
        echo "  format     Run code formatting"
        echo "  check      Run all checks (format, test, type-check)"
        echo "  help       Show this help message"
        ;;
    *)
        print_error "Unknown command: $1"
        echo "Run './scripts/dev.sh help' for usage information."
        exit 1
        ;;
esac
