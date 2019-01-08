"""Fixtures for testing graph implementation."""
import pytest
from .graph import Graph


@pytest.fixture()
def graph_empty():
    """Empty graph for testing."""
    g = Graph()
    return g


@pytest.fixture()
def graph_one():
    """Graph of vertices and weights for testing."""
    g = Graph()
    g.graph = {
        # value: weight
        'A': {'B': 10},
        'B': {'A': 5, 'D': 15, 'C': 20},
        'C': {'E': 1},
        'D': {'A': 5},
        'E': {'F': 2, 'B': 4},
        'F': {'D': 11}
    }
    return g


@pytest.fixture()
def graph_two():
    """Second graph with different vertices and weights for testing."""
    g = Graph()
    g.graph = {
        'A': {'B': 10, 'C': 15},
        'B': {'D': 15, 'E': 5, 'C': 2},
        'C': {'F': 50, 'G': 25},
        'D': {},
        'E': {'C': 5},
        'F': {'E': 10},
        'G': {'F': 20}
    }
    return g
