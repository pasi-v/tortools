"""Test configuration and fixtures."""

import random

import pytest


@pytest.fixture(autouse=True)
def set_random_seed():
    """Set a fixed random seed for reproducible tests."""
    random.seed(42)
    yield
    random.seed()
