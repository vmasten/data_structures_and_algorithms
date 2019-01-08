"""Tests for binary tree FizzBuzz algorithm."""
from ...data_structures.binary_search_tree.bst import BST
from .fizz_buzz_tree import FizzBuzzTree
import pytest


@pytest.fixture()
def empty_bst():
    """Empty BST for testing."""
    return BST()


@pytest.fixture()
def test_bst():
    """BST with a variety of nodes that should be replaced."""
    bst = BST()
    bst.insert(5, bst.root)
    bst.insert(1, bst.root)
    bst.insert(3, bst.root)
    bst.insert(15, bst.root)
    bst.insert(30, bst.root)
    bst.insert(9, bst.root)

    return bst


@pytest.fixture()
def test_fizz_bst():
    """Simple BST to test Fizz condition."""
    bst = BST()
    bst.insert(3, bst.root)
    bst.insert(1, bst.root)

    return bst


@pytest.fixture()
def test_fizzbuzz_bst():
    """Simple BST to test FizzBuzz condition."""
    bst = BST()
    bst.insert(15, bst.root)
    bst.insert(1, bst.root)

    return bst


def test_fizz(test_fizz_bst):
    """Test that root is changed to Fizz."""
    FizzBuzzTree(test_fizz_bst.root)
    expected = 'Fizz'  # 3
    actual = test_fizz_bst.root.val
    assert expected == actual


def test_fizzbuzz(test_fizzbuzz_bst):
    """Test that root is changed to FizzBuzz."""
    FizzBuzzTree(test_fizzbuzz_bst.root)
    expected = 'FizzBuzz'  # 15
    actual = test_fizzbuzz_bst.root.val
    assert expected == actual


def test_buzz(test_bst):
    """Test that root was changed to Buzz."""
    FizzBuzzTree(test_bst.root)
    expected = 'Buzz'  # 5
    actual = test_bst.root.val
    assert actual == expected


def test_fizzbuzz_traversal(test_bst):
    """Test that the BST has been modified in place."""
    FizzBuzzTree(test_bst.root)
    test_bst.in_order(test_bst.root, test_bst.enlist)
    # The easiest way to test that FizzBuzzTree is working along
    # the whole tree is to use my built-in traversal and then
    # compare the list output to the expected order.
    actual = test_bst.traversal_list
    expected = [1, 'Fizz', 'Buzz', 'Fizz', 'FizzBuzz', 'FizzBuzz']
    # [1, 3, 5, 9, 15, 30]
    assert actual == expected


def test_empty_fizzbuzz(empty_bst):
    """Test whether FizzBuzzTree can handle an empty list."""
    FizzBuzzTree(empty_bst.root)
    assert empty_bst.root.val is None
