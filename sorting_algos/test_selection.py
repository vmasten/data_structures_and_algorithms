"""Tests for selection sort."""
from .selection import selection_sort


def test_selection_sort(sample_list):
    """Test selection sort based on expected result."""
    actual = selection_sort(sample_list)
    expected = [1, 3, 8, 9, 10, 33]
    assert actual == expected


def test_empty(empty_list):
    """Test the function with an empty list."""
    actual = selection_sort(empty_list)
    expected = 'empty list!'
    assert expected == actual


def test_singleton(singleton_list):
    """Test that a list with a single item doesn't break anything."""
    actual = selection_sort(singleton_list)
    expected = [42]
    assert expected == actual
