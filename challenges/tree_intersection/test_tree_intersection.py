"""Tests for the tree intersection function."""
from .tree_intersection import tree_intersection


def test_tree_intersection(small_bst, test_bst):
    """Test function with two small trees."""
    actual = tree_intersection(small_bst, test_bst)
    expected = {9, 5}
    assert expected == actual


def test_tree_intersection_empty_tree(small_bst, empty_bst):
    """Test that an empty tree doesn't break the function."""
    actual = tree_intersection(small_bst, empty_bst)
    expected = 'Input nodes must be integers!'
    assert expected == actual


def test_tree_intersection_known_result(cf_tree, cf_tree2):
    """Test that the result is correct with known input/output."""
    actual = tree_intersection(cf_tree, cf_tree2)
    expected = {160, 100, 200, 175, 500, 125, 350}
    assert expected == actual


def test_bad_input(string_bst, cf_tree):
    """Test that invalid input type results in error."""
    actual = tree_intersection(cf_tree, string_bst)
    expected = 'Input nodes must be integers!'
    assert expected == actual
