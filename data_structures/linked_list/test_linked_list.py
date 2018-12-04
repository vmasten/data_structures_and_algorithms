"""Tests for a singly linked list."""

from .linked_list import LinkedList
import pytest


@pytest.fixture
def empty_linked_list():
    """Empty linked list for testing."""
    return LinkedList()


@pytest.fixture
def small_linked_list():
    """Small linked list for testing."""
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    return ll


@pytest.fixture
def random_ll():
    """Large linked list full of randomly generated numbers for testing."""
    from random import randint
    ll = LinkedList()
    for num in range(100):
        ll.insert(randint(0, 100))
    return ll


def test_linked_list_module_exists():
    """Proof of life."""
    assert LinkedList


def test_linked_list_instance_has_none_value_head(empty_linked_list):
    """Make sure empty list is empty."""
    assert empty_linked_list.head is None


def test_linked_list_str_method(empty_linked_list):
    """Check for well-formed output from __str__."""
    assert str(empty_linked_list) == (f'Linked List: Head val - '
                                      f'{empty_linked_list.head}')
    # For the record, the formatting above is very silly.


def test_size_of_empty_linked_list(empty_linked_list):
    """Make sure the empty list has a length of 0."""
    assert len(empty_linked_list) == 0


def test_small_linked_list_has_size_of_4(small_linked_list):
    """Make sure the calculated length of linked list matches the fixture."""
    assert len(small_linked_list) == 4


def test_insert_new_node_into_empty_list(empty_linked_list):
    """Test initial node insertion."""
    assert empty_linked_list.head is None
    empty_linked_list.insert(1)
    assert empty_linked_list.head.val == 1


def test_random_ll(random_ll):
    """Test the length calculation in a longer list."""
    assert len(random_ll) == 100


def test_iterable_as_argument():
    """Test passing in an iterable to instantiate the linked list."""
    ll = LinkedList([1, 2, 3, 4])
    assert ll.head.val == 4
    assert len(ll) == 4


def test_includes(small_linked_list):
    """Test the includes function."""
    expected = True
    assert small_linked_list.includes(4) == expected


def test_includes_edge(small_linked_list):
    """Test the edge case of finding the last node."""
    expected = True
    assert small_linked_list.includes(1) == expected


def test_includes_not_in_list(small_linked_list):
    """Test includes when the search value is not in list."""
    expected = False
    assert small_linked_list.includes(5) == expected


def test_includes_empty_list(empty_linked_list):
    """Test includes on an empty list."""
    expected = False
    assert empty_linked_list.includes(1) == expected


def test_invalid_instantiation():
    """Test for invalid list instantiation."""
    with pytest.raises(TypeError):
        LinkedList('j')


def test_repr_output(small_linked_list):
    """Test for well-formed output of __repr__."""
    assert repr(small_linked_list) == (f'<LinkedList: head - 4 size - 4>')


def test_insertion_order(small_linked_list):
    """Test the insertion order of the linked list."""
    expected = [4, 3, 2, 1]
    actual = []
    while small_linked_list.head:
        actual.append(small_linked_list.head.val)
        small_linked_list.head = small_linked_list.head._next
    assert expected == actual


def test_append(small_linked_list):
    """Tests that the append method adds nodes at end of list."""
    small_linked_list.append(5)
    expected = [4, 3, 2, 1, 5]
    actual = []
    while small_linked_list.head:
        actual.append(small_linked_list.head.val)
        small_linked_list.head = small_linked_list.head._next
    assert expected == actual


def test_append_empty(empty_linked_list):
    """Tests that append works with an empty list."""
    empty_linked_list.append(4)
    expected = [4]
    actual = []
    while empty_linked_list.head:
        actual.append(empty_linked_list.head.val)
        empty_linked_list.head = empty_linked_list.head._next
    assert expected == actual


def test_appended_size(small_linked_list):
    """Test that size is incrementing correctly on append."""
    small_linked_list.append(5)
    expected = 5
    actual = small_linked_list.__len__()
    assert expected == actual


def test_insert_after(small_linked_list):
    """Test insertion after present element."""
    small_linked_list.insert_after(3, 5)
    expected = [4, 3, 5, 2, 1]
    actual = []
    while small_linked_list.head:
        actual.append(small_linked_list.head.val)
        small_linked_list.head = small_linked_list.head._next
    assert expected == actual


def test_insert_after_end_of_list(small_linked_list):
    """Test insertion at end of list."""
    small_linked_list.insert_after(1, 5)

    expected = [4, 3, 2, 1, 5]
    actual = []
    while small_linked_list.head:
        actual.append(small_linked_list.head.val)
        small_linked_list.head = small_linked_list.head._next
    assert expected == actual


def test_insert_after_front_of_list(small_linked_list):
    """Test insertion at front of list."""
    small_linked_list.insert_after(4, 5)
    expected = [4, 5, 3, 2, 1]
    actual = []
    while small_linked_list.head:
        actual.append(small_linked_list.head.val)
        small_linked_list.head = small_linked_list.head._next
    assert expected == actual


def test_insert_after_wrong_element(small_linked_list):
    """Tests insertion after a nonexistent element."""
    actual = small_linked_list.insert_after(5, 6)
    expected = False
    assert expected == actual


def test_insert_before(small_linked_list):
    """Test insertion before present element."""
    small_linked_list.insert_before(3, 5)
    expected = [4, 5, 3, 2, 1]
    actual = []
    while small_linked_list.head:
        actual.append(small_linked_list.head.val)
        small_linked_list.head = small_linked_list.head._next
    assert expected == actual


def test_insert_before_end_of_list(small_linked_list):
    """Test insertion before end of list."""
    small_linked_list.insert_before(1, 5)

    expected = [4, 3, 2, 5, 1]
    actual = []
    while small_linked_list.head:
        actual.append(small_linked_list.head.val)
        small_linked_list.head = small_linked_list.head._next
    assert expected == actual


def test_insert_before_front_of_list(small_linked_list):
    """Test insertion before at front of list."""
    small_linked_list.insert_before(4, 5)
    expected = [5, 4, 3, 2, 1]
    actual = []
    while small_linked_list.head:
        actual.append(small_linked_list.head.val)
        small_linked_list.head = small_linked_list.head._next
    assert expected == actual


def test_insert_before_wrong_element(small_linked_list):
    """Tests insertion before a nonexistent element."""
    actual = small_linked_list.insert_before(5, 6)
    expected = False
    assert expected == actual
