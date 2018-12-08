"""Tests to ensure queue data structure works as expected."""
from .queue import Queue
import pytest


@pytest.fixture
def empty_queue():
    """Empty queue for testing."""
    return Queue()


@pytest.fixture
def small_queue():
    """Small queue for testing."""
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    return queue


def test_empty_queue_none_value(empty_queue):
    """Make sure empty queue is empty."""
    assert empty_queue.front is None
    assert empty_queue.back is None


def test_queue_empty_insertion(empty_queue):
    """Make sure a newly instantiated queue can handle insertion."""
    empty_queue.enqueue(1)
    expected = 1
    assert empty_queue.front.val == expected
    assert empty_queue.back.val == expected


def test_enqueue_in_existing_queue(small_queue):
    """Test enqueueing into an existing queue."""
    small_queue.enqueue(2)
    expected = 2
    assert small_queue.back.val == expected


def test_enqueue_iterable_and_insertion_order():
    """Instantiate a queue with an iterable and test its structure."""
    queue = Queue([1, 2, 3, 4])
    assert queue.front.val == 1
    assert queue.back.val == 4


def test_enqueue_dequeue_order(small_queue):
    """Test FIFO nature of queue."""
    expected = [1, 2, 3, 4]
    actual = []
    while small_queue.front:
        temp = small_queue.dequeue()
        actual.append(temp.val)
    assert actual == expected


def test_empty_queue_dequeue(empty_queue):
    """Test dequeueing empty queue."""
    expected = 'Queue is empty!'
    actual = empty_queue.dequeue()
    assert actual == expected


def test_queue_length(small_queue):
    """Test len magic method."""
    expected = 4
    actual = len(small_queue)
    assert actual == expected


def test_queue_str(small_queue):
    """Test str magic method."""
    expected = f'Queue: Front value: {small_queue.front.val}'
    actual = str(small_queue)
    assert expected == actual


def test_queue_repr(small_queue):
    """Test repr magic method."""
    expected = f'<QUEUE Front: {small_queue.front}>'
    actual = repr(small_queue)
    assert actual == expected


def test_queue_garbage_collection(small_queue):
    """Test whether dequeued queue is good and empty."""
    expected = None
    while small_queue.front:
        small_queue.dequeue()
    assert small_queue.front == expected
    assert small_queue.back.next_node == expected
    # back itself still returns a node, which may be a bug
