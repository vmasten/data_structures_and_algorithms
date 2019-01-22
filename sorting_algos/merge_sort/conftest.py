"""Fixtures for testing the selection sort."""
import pytest


@pytest.fixture
def sample_list():
    """A list of random numbers for testing."""
    return [3, 1, 9, 33, 8, 10]


@pytest.fixture
def empty_list():
    """An empty list for testing."""
    return list()


@pytest.fixture
def singleton_list():
    """A list with one item for testing."""
    return [42]
