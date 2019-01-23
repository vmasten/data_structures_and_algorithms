"""Tests for quick sort."""
from .quick_sort import quick_sort


def test_quick_sort(sample_list):
    """Test quick sort based on expected result."""
    actual = quick_sort(sample_list, 0, len(sample_list)-1)
    expected = [1, 3, 8, 9, 10, 33]
    assert actual == expected


def test_empty(empty_list):
    """Test the function with an empty list."""
    actual = quick_sort(empty_list, 0, 0)
    expected = []
    assert expected == actual


def test_singleton(singleton_list):
    """Test that a list with a single item doesn't break anything."""
    actual = quick_sort(singleton_list, 0, 0)
    expected = [42]
    assert expected == actual
