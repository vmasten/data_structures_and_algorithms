"""Fixtures for testing the left join function."""
from ...data_structures.hash_table.hash_table import HashTable
import pytest


@pytest.fixture
def hash_table():
    """Simple hash table for testing."""
    h = HashTable()
    h.setter('fond', 'enamored')
    h.setter('wrath', 'anger')
    h.setter('diligent', 'employed')
    h.setter('outfit', 'garb')

    return h


@pytest.fixture
def hash_table_two():
    """Second simple hash table for testing."""
    h = HashTable()
    h.setter('fond', 'averse')
    h.setter('wrath', 'delight')
    h.setter('diligent', 'idle')
    h.setter('guide', 'follow')

    return h


@pytest.fixture
def empty_hash_table():
    """Empty hash table for testing."""
    h = HashTable()

    return h
