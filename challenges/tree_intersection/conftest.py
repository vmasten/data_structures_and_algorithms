"""Fixtures to test the tree intersection function."""
import pytest
from ...data_structures.binary_search_tree.bst import BST


@pytest.fixture()
def empty_bst():
    """Empty BST for testing."""
    return BST()


@pytest.fixture()
def small_bst():
    """Small BST for testing."""
    bst = BST()
    bst.insert(5, bst.root)
    bst.insert(1, bst.root)
    bst.insert(40, bst.root)
    bst.insert(32, bst.root)
    bst.insert(9, bst.root)
    return bst


@pytest.fixture()
def test_bst():
    """Another test BST."""
    bst = BST()
    bst.insert(10, bst.root)
    bst.insert(8, bst.root)
    bst.insert(20, bst.root)
    bst.insert(5, bst.root)
    bst.insert(9, bst.root)
    bst.insert(11, bst.root)

    return bst


@pytest.fixture()
def string_bst():
    """BST with strings for node values for testing."""
    bst = BST()
    bst.insert('A', bst.root)
    bst.insert('B', bst.root)
    bst.insert('C', bst.root)
    bst.insert('D', bst.root)
    bst.insert('E', bst.root)
    bst.insert('F', bst.root)

    return bst


@pytest.fixture()
def cf_tree():
    """A tree modeled after the Code Fellows example."""
    bst = BST()
    bst.insert(150, bst.root)
    bst.insert(100, bst.root)
    bst.insert(75, bst.root)
    bst.insert(160, bst.root)
    bst.insert(125, bst.root)
    bst.insert(175, bst.root)
    bst.insert(250, bst.root)
    bst.insert(200, bst.root)
    bst.insert(350, bst.root)
    bst.insert(300, bst.root)
    bst.insert(500, bst.root)

    return bst


@pytest.fixture()
def cf_tree2():
    """A tree modeled after the other CF example tree."""
    bst = BST()
    bst.insert(42, bst.root)
    bst.insert(100, bst.root)
    bst.insert(600, bst.root)
    bst.insert(15, bst.root)
    bst.insert(160, bst.root)
    bst.insert(200, bst.root)
    bst.insert(350, bst.root)
    bst.insert(125, bst.root)
    bst.insert(175, bst.root)
    bst.insert(4, bst.root)
    bst.insert(500, bst.root)

    return bst
