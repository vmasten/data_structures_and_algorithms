"""Fixtures for testing radix sort."""
import pytest


@pytest.fixture
def radix_list():
    """List of integers for testing the sort."""
    return [999, 45, 304, 202, 144, 983]


@pytest.fixture
def bigger_radix_list():
    """More variable list for testing the sort."""
    return [3828, 39295, 183, 22, 1, 853333, 654443, 3858283]


@pytest.fixture
def empty():
    """Empty list for testing empty list edge case."""
    return []


@pytest.fixture
def singleton():
    """Singleton list for testing."""
    return [333]
