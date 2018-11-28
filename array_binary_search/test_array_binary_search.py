"""Tests to ensure proper output of array_binary_search."""
from array_binary_search import binary_search


def test_simple_array():
    """Tests whether a minimal array returns the correct result."""
    actual = [1, 2]
    key = 2
    expected = 1
    assert binary_search(actual, key) == expected


def test_lower():
    """Tests if key in bottom half of array returns as expected."""
    actual = [1, 2, 3, 4, 5]
    key = 2
    expected = 1
    assert binary_search(actual, key) == expected


def test_higher():
    """Tests if key in top half of array returns as expected."""
    actual = [1, 2, 3, 4, 5]
    key = 4
    expected = 3
    assert binary_search(actual, key) == expected


def test_lower_bound():
    """Tests if key in lower bound returns as expected."""
    actual = [1, 2, 3, 4, 5, 6, 7, 8]
    key = 1
    expected = 0
    assert binary_search(actual, key) == expected


def test_upper_bound():
    """Tests if key in upper bound returns as expected."""
    actual = [1, 2, 3, 4, 5, 6, 7, 8]
    key = 8
    expected = 7
    assert binary_search(actual, key) == expected
