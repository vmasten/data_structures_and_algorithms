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
    h.setter(2)
    h.setter(5)
    h.setter(7)
    return h


@pytest.fixture
def str_hash_table():
    """Hash table made up of strings for testing."""
    h = HashTable()
    h.setter('cat')
    h.setter('dog')
    h.setter('catdog')
    return h
