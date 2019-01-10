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


@pytest.fixture()
def city_graph():
    """Graph to simulate cost to travel between cities."""
    g = Graph()
    g.graph = {
        'Seattle': {'SF': 50, 'NY': 200},
        'SF': {'Seattle': 50, 'LA': 25},
        'LA': {'SF': 25, 'Houston': 75},
        'Houston': {'LA': 75, 'NY': 100},
        'NY': {'Houston': 100, 'Seattle': 200},
    }
    return g

@pytest.fixture()
def df_graph():
    """A graph to emulate the sample to test DFS."""
    g = Graph()
    g.graph = {
        'A': {'B': 1, 'D': 2},
        'B': {'C': 2, 'D': 4},
        'C': {'G': 3},
        'D': {'E': 2, 'F': 4, 'H': 6},
        'E': {'D': 2},
        'F': {'H': 3, 'F': 6},
        'G': {'C': 2},
        'H': {'D': 5, 'F': 10},
    }
    return g
