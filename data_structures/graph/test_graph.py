"""Tests for graph implementation."""


def test_graph_instantiation(graph_one):
    """Proof of life."""
    assert graph_one.graph


def test_graph_len(graph_one):
    """Test of the len function."""
    expected = 6
    actual = len(graph_one.graph)
    assert expected == actual


def test_graph_two_len(graph_two):
    """Make sure len is actually working correctly."""
    expected = 7
    actual = len(graph_two.graph)
    assert expected == actual


def test_graph_one_str(graph_one):
    """Test str method by printing graph."""
    print(str(graph_one))


def test_graph_has_vert(graph_one):
    """Test the has_vert function."""
    expected = True
    actual = graph_one.has_vert('A')
    assert expected == actual


def test_graph_has_vert_false(graph_one):
    """Make sure has_vert returns false when the value already exists."""
    expected = False
    actual = graph_one.has_vert('Z')
    assert expected == actual


def test_graph_add(graph_one):
    """Test the add_vert function."""
    graph_one.add_vert('Z')
    print(graph_one)


def test_graph_add_already_exists(graph_one):
    """Test that add_vert doesn't do anything if the value exists."""
    expected = graph_one.graph
    actual = graph_one.add_vert('A')
    assert expected == actual


def test_add_edge(graph_one):
    """Test add edge function."""
    graph_one.add_vert('Z')
    graph_one.add_edge('A', 'Z', 5)
    print(graph_one)

def test_get_neightbors(graph_one):
    """Test get neighbors function."""
    print(graph_one.get_neighbors('A'))

