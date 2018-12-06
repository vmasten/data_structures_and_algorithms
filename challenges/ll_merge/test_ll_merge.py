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


@pytest.fixture
def bigger_linked_list():
    """Slightly larger linked list for testing."""
    ll = LinkedList()
    ll.insert(10)
    ll.insert(9)
    ll.insert(8)
    ll.insert(7)
    ll.insert(6)
    ll.insert(5)
    ll.insert(4)
    ll.insert(3)
    ll.insert(2)
    ll.insert(1)
    return ll

def test_linked_list_merge_head(small_linked_list, bigger_linked_list):
    actual = merge_lists(small_linked_list, bigger_linked_list)
    expected = 4
    assert actual.val == expected

def test_linked_list_merge_list_values(small_linked_list, bigger_linked_list):
    actual = merge_lists(small_linked_list, bigger_linked_list)
    while actual._next:
        # print(actual.val)
        actual = actual._next
