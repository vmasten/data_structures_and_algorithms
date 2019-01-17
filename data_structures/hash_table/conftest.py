"""Fixtures for testing hash table implementation."""
from .hash_table import HashTable
import pytest


@pytest.fixture
def empty_hash_table():
    """Empty hash table for testing."""
    h = HashTable()
    return h


@pytest.fixture
def very_simple_hash_table():
    """Hash table for testing."""
    h = HashTable()
    h.setter('blue', '2')
    h.setter('red', 5)
    h.setter('green', 7)
    return h


@pytest.fixture
def str_hash_table():
    """Hash table made up of strings for testing."""
    h = HashTable()
    h.setter('cat', 'bad')
    h.setter('dog', 'good')
    h.setter('catdog', 'badgood')
    return h
