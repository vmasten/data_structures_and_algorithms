"""Tests for zip merging two lists."""

from .linked_list import LinkedList
from .ll_merge import merge_lists
import pytest


@pytest.fixture
def empty_linked_list():
    """Empty linked list for testing."""
    return LinkedList()


@pytest.fixture
def small_linked_list():
    """Small linked list for testing."""
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    return ll


@pytest.fixture
def random_ll():
    """Large linked list full of randomly generated numbers for testing."""
    from random import randint
    ll = LinkedList()
    for num in range(100):
        ll.append(randint(0, 100))
    return ll


@pytest.fixture
def bigger_linked_list():
    """Slightly larger linked list for testing."""
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.append(7)
    ll.append(8)
    ll.append(9)
    ll.append(10)
    return ll


@pytest.fixture
def challenge_sample_1():
    """Linked list from the challenge description."""
    ll = LinkedList()
    ll.append(1)
    ll.append(3)
    ll.append(2)
    return ll


@pytest.fixture
def challenge_sample_2():
    """Linked list from the challenge description."""
    ll = LinkedList()
    ll.append(5)
    ll.append(9)
    ll.append(4)
    return ll


def test_linked_list_merge_head(small_linked_list, bigger_linked_list):
    """Tests whether the head of the output linked list is returned correctly."""
    actual = merge_lists(small_linked_list, bigger_linked_list)
    expected = 1
    assert actual.val == expected


def test_linked_list_merge_list_values(small_linked_list, bigger_linked_list):
    """Tests whether the output list contains the correct values."""
    test = merge_lists(small_linked_list, bigger_linked_list)
    actual = []
    expected = [1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 8, 9, 10]
    while test:
        actual.append(test.val)
        test = test._next
    assert expected == actual


def test_linked_list_merge_list_values_flipped(bigger_linked_list, small_linked_list):
    """Tests whether a larger list as first input still contains correct values."""
    test = merge_lists(bigger_linked_list, small_linked_list)
    actual = []
    expected = [1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 8, 9, 10]
    while test:
        actual.append(test.val)
        test = test._next
    assert expected == actual


def test_merge_samples(challenge_sample_1, challenge_sample_2):
    """Tests for valid output based on code challenge examples."""
    test = merge_lists(challenge_sample_1, challenge_sample_2)
    actual = []
    expected = [1, 5, 3, 9, 2, 4]
    while test:
        actual.append(test.val)
        test = test._next
    assert expected == actual


def test_merge_second_list_empty(small_linked_list, empty_linked_list):
    """Tests malformed input (one list is empty)."""
    test = merge_lists(small_linked_list, empty_linked_list)
    actual = []
    expected = [1, 2, 3, 4]
    while test:
        actual.append(test.val)
        test = test._next
    assert expected == actual


def test_merge_first_list_empty(empty_linked_list, small_linked_list):
    """Tests malformed input on the other list."""
    test = merge_lists(empty_linked_list, small_linked_list)
    actual = []
    expected = [1, 2, 3, 4]
    while test:
        actual.append(test.val)
        test = test._next
    assert expected == actual
