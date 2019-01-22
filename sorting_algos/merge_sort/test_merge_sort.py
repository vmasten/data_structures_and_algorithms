"""Tests for selection sort."""
from .merge_sort import merge_sort


def test_merge_sort(sample_list):
    """Test merge sort based on expected result."""
    actual = merge_sort(sample_list)
    expected = [1, 3, 8, 9, 10, 33]
    assert actual == expected


def test_empty(empty_list):
    """Test the function with an empty list."""
    actual = merge_sort(empty_list)
    expected = []
    assert expected == actual


def test_singleton(singleton_list):
    """Test that a list with a single item doesn't break anything."""
    actual = merge_sort(singleton_list)
    expected = [42]
    assert expected == actual
