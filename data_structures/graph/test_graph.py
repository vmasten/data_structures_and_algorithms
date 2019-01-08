"""Tests for graph implementation."""
from .breadth_first.breadth_first import breadth_first_traversal
from .get_edge.get_edge import get_edges


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


def test_get_neighbors(graph_one):
    """Test get neighbors function."""
    expected = ['A', 'D', 'C']
    actual = graph_one.get_neighbors('B')
    assert expected == actual


def test_breadth_first(graph_one, capsys):
    """Test breadth-first traversal."""
    expected = 'A, B, D, C, E, F\n'
    breadth_first_traversal(graph_one, 'A')
    out, err = capsys.readouterr()
    actual = out
    assert expected == actual


def test_breadth_first_again(graph_two):
    """Test breadth-first traversal return."""
    expected = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    actual = breadth_first_traversal(graph_two, 'A')
    assert expected == actual


def test_sanity(city_graph):
    """Test to make sure I'm pulling out the right bits from the graph."""
    print(city_graph.graph['Seattle']['SF'])


def test_get_edges(city_graph):
    """Test function to get edges."""
    test_cities = ['Seattle', 'SF']
    expected = (True, f'$50')
    actual = get_edges(city_graph, test_cities)
    assert expected == actual


def test_get_edges_false(city_graph):
    """Test impossible route."""
    test_cities = ['Seattle', 'Houston']
    expected = (False, '$0')
    actual = get_edges(city_graph, test_cities)
    assert expected == actual


def test_get_edges_one_city(city_graph):
    """Test case where only one city is specified."""
    test_cities = ['Seattle']
    expected = 'A trip involves at least two cities!'
    actual = get_edges(city_graph, test_cities)
    assert expected == actual


def test_get_edges_multi_city(city_graph):
    """Test multi-hop route."""
    test_cities = ['Seattle', 'SF', 'LA']
    expected = (True, f'$75')
    actual = get_edges(city_graph, test_cities)
    assert expected == actual


def test_multi_hop_invalid(city_graph):
    """Test initially valid route with an impossible hop."""
    test_cities = ['NY', 'Houston', 'SF']
    expected = (False, '$0')
    actual = get_edges(city_graph, test_cities)
    assert expected == actual
