"""Tests for the PseudoQueue class."""
from ..queue_with_stacks.queue_with_stacks import PseudoQueue
import pytest


@pytest.fixture
def empty_queue():
    """Empty queue for testing."""
    return PseudoQueue()


@pytest.fixture
def small_queue():
    """Small queue for testing."""
    small_queue = PseudoQueue()
    small_queue.enqueue(1)
    small_queue.enqueue(2)
    small_queue.enqueue(3)
    small_queue.enqueue(4)
    return small_queue


def test_queue_instance():
    """Test that instantiated queue is well-formed."""
    test_queue = PseudoQueue()
    assert test_queue.front.top is None
    assert test_queue.rear.top is None


def test_empty_queue_enqueue(empty_queue):
    """Test an initial enqueue."""
    empty_queue.enqueue(1)
    assert empty_queue.rear.top.val == 1


def test_empty_queue_dequeue(empty_queue):
    """Make sure dequeue on empty queue doesn't error out."""
    empty_queue.dequeue()


def test_queue_instance_iterable():
    """Test instantiation with an iterable."""
    iterable_queue = PseudoQueue([1, 2, 3])
    expected = 3
    assert iterable_queue.rear.top.val == expected


def test_small_queue_enqueue(small_queue):
    """Test enqueueing on an existent queue."""
    small_queue.enqueue(5)
    assert small_queue.rear.top.val == 5


def test_dequeue(small_queue):
    """Test dequeueing."""
    actual = small_queue.dequeue()
    expected = 1
    assert expected == actual


def test_multiple_dequeue(small_queue):
    """Test order after multiple dequeues."""
    assert small_queue.dequeue() == 1
    assert small_queue.dequeue() == 2
    assert small_queue.rear.top.val == 4


def test_enqueue_dequeue(small_queue):
    """Test enqueueing and dequeueing in same queue."""
    small_queue.enqueue(5)
    small_queue.enqueue(6)
    small_queue.enqueue(7)
    small_queue.dequeue()
    small_queue.dequeue()
    assert small_queue.rear.top.val == 7
    # check of the rear item in the queue
    assert small_queue.dequeue() == 3
    # check of the front item in the queue
