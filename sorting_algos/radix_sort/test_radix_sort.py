"""Tests for radix sort."""
from .radix_sort import radix_sort


def test_radix_sort(radix_list):
    """Test the sort with the passed in list."""
    expected = [45, 144, 202, 304, 983, 999]
    actual = radix_sort(radix_list)
    assert expected == actual


def test_larger_list(bigger_radix_list):
    """Try again with a bigger, more variant list."""
    expected = [1, 22, 183, 3828, 39295, 654443, 853333, 3858283]
    actual = radix_sort(bigger_radix_list)
    assert expected == actual


def test_empty_list(empty):
    """Test the sort with an empty list."""
    expected = 'empty list!'
    actual = radix_sort(empty)
    assert expected == actual


def test_singleton(singleton):
    """Test the sort with a single item."""
    expected = [333]
    actual = radix_sort(singleton)
    assert expected == actual
