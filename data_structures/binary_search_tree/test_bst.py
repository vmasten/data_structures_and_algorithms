"""Tests for binary search tree module."""
from .bst import Node, BST
import pytest


@pytest.fixture()
def bst_node():
    """Instantiate node for testing."""
    return Node(1)


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
def test_bst():
    """Another test BST, written to emulate Code Fellows example."""
    bst = BST()
    bst.insert(10, bst.root)
    bst.insert(8, bst.root)
    bst.insert(20, bst.root)
    bst.insert(5, bst.root)
    bst.insert(9, bst.root)
    bst.insert(11, bst.root)

    return bst


def test_node_instantiation(bst_node):
    """Test that node has a value and null left and right pointers."""
    assert bst_node.val == 1
    assert bst_node.left is None
    assert bst_node.right is None


def test_node_str(bst_node):
    """Test of node __str__ magic method."""
    actual = str(bst_node)
    expected = f'Node: value - 1'
    assert actual == expected


def test_node_repr(bst_node):
    """Test of node __repr__ magic method."""
    actual = repr(bst_node)
    expected = f'<Node: value - 1 left - None right - None>'
    assert actual == expected


def test_bst_instantiation(empty_bst):
    """Test that BST is instantiated correctly."""
    assert empty_bst.root.val is None
    assert empty_bst.root.left is None
    assert empty_bst.root.right is None


def test_bst_str(empty_bst):
    """Test BST __str__ magic method."""
    actual = str(empty_bst)
    expected = f'BST: Root - Node: value - None'
    assert actual == expected


def test_bst_repr(empty_bst):
    """Test BST __repr__ magic method."""
    actual = repr(empty_bst)
    expected = f'<BST: - Node: value - None>'
    assert actual == expected


def test_bst_insertion(empty_bst):
    """Test BST insertion method."""
    empty_bst.insert(5, empty_bst.root)
    empty_bst.insert(3, empty_bst.root)
    assert empty_bst.root.val == 5
    assert empty_bst.root.left.val == 3


def test_bst_iterable():
    """Test BST instantiation with an iterable."""
    iterable = [5, 2, 10, 4, 8]
    bst = BST(iterable)
    assert bst.root.val == 5


def test_bst_bad_instantiation():
    """Test invalid BST instantiation."""
    with pytest.raises(TypeError):
        assert BST('j') == 'Iterable must be of type list'


def test_bst_in_order_traversal(small_bst):
    """Test in order BST traversal."""
    small_bst.traversal_list = []
    # Since traversal_list is stored in the BST object, nuke it before testing.
    expected = [1, 5, 9, 32, 40]
    actual = small_bst.in_order(small_bst.root, small_bst.enlist)
    assert actual == expected


def test_bst_pre_order_traversal(small_bst):
    """Test pre order BST traversal."""
    small_bst.traversal_list = []
    expected = [5, 1, 40, 32, 9]
    actual = small_bst.pre_order(small_bst.root, small_bst.enlist)
    assert actual == expected


def test_bst_post_order_traversal(small_bst):
    """Test post order BST traversal."""
    small_bst.traversal_list = []
    expected = [1, 9, 32, 40, 5]
    actual = small_bst.post_order(small_bst.root, small_bst.enlist)
    assert actual == expected


def test_bst_strings(string_bst):
    """Test whether a BST can be made up of strings."""
    assert string_bst.root.val == 'A'
    assert string_bst.root.right.val == 'B'
    assert string_bst.root.right.right.val == 'C'
    # The BST is created, but it always inserts to the right
    # without a proper string comparison


def test_bst_traversals_pre(test_bst):
    """Test BST pre order traversal with a specifically-formed BST."""
    test_bst.traversal_list = []
    expected = [10, 8, 5, 9, 20, 11]
    actual = test_bst.pre_order(test_bst.root, test_bst.enlist)
    assert actual == expected


def test_bst_traversals_in(test_bst):
    """Test BST in order traversal with a specifically-formed BST."""
    test_bst.traversal_list = []
    expected = [5, 8, 9, 10, 11, 20]
    actual = test_bst.in_order(test_bst.root, test_bst.enlist)
    assert actual == expected


def test_bst_traversals_post(test_bst):
    """Test BST post order traversal with a specifically-formed BST."""
    test_bst.traversal_list = []
    expected = [5, 9, 8, 11, 20, 10]
    actual = test_bst.post_order(test_bst.root, test_bst.enlist)
    assert actual == expected
