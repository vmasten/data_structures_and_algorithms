"""Tests to ensure that the stack data structure is implemented correctly."""
from .stack import Stack
import pytest


@pytest.fixture
def empty_stack():
    """Empty stack for testing."""
    return Stack()


@pytest.fixture
def small_stack():
    """Small stack for testing."""
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    return stack


def test_empty_stack_none_value(empty_stack):
    """Make sure empty stack is empty."""
    assert empty_stack.top is None


def test_stack_empty_insertion(empty_stack):
    """Make sure a newly instantiated stack can handle insertion."""
    empty_stack.push(1)


def test_empty_stack_size(empty_stack):
    """Make sure empty stack has size of 0."""
    expected = 0
    assert len(empty_stack) == expected


def test_stack_push_order(small_stack):
    """Make sure insertion is happening correctly."""
    expected = 4
    assert small_stack.top.val == expected


def test_small_stack_size(small_stack):
    """Make sure size is incrementing properly."""
    expected = 4
    assert len(small_stack) == expected


def test_stack_size_increment_push(small_stack):
    """Make sure size is increased after a push."""
    expected = 5
    small_stack.push(5)
    assert len(small_stack) == expected


def test_stack_size_decrement_pop(small_stack):
    """Make sure size is decrementing properly."""
    expected = 3
    small_stack.pop()
    assert len(small_stack) == expected


def test_instantiation_iterable_as_argument():
    """Test for instantiating the stack with a list."""
    stack = Stack([1, 2, 3, 4])
    assert stack.top.val == 4
    assert len(stack) == 4


def test_str_output(small_stack):
    """Test for well-formed output from str magic method."""
    assert str(small_stack) == (f'Stack: Top value - {small_stack.top.val}')


def test_repr_output(empty_stack):
    """Test for well-formed repr output on an empty stack."""
    assert repr(empty_stack) == f'<STACK Top: {empty_stack.top}>'


def test_pop_empty_stack(empty_stack):
    """Test output when an empty stack can be popped."""
    actual = empty_stack.pop()
    expected = 'Stack is empty!'
    assert actual == expected


def test_pop_conditional(small_stack):
    """Test that a valid pop doesn't trigger empty stack conditional."""
    small_stack.pop()
    expected = 3
    assert len(small_stack) == expected


def test_peek_valid_stack(small_stack):
    """Test that peek works as expected."""
    expected = 4
    actual = small_stack.peek()
    assert actual.val == expected
    # have to use .val on actual due to implementation


def test_peek_empty_stack(empty_stack):
    """Test that peek yells at the user when the stack is empty."""
    expected = 'Stack is empty!'
    actual = empty_stack.peek()
    assert actual == expected


def test_multimodal_input_and_output(small_stack):
    """Test a bunch of different stuff at once."""
    small_stack.push(5)
    small_stack.push(6)
    small_stack.pop()
    small_stack.pop()
    small_stack.push(8)
    assert small_stack.top.val == 8
    assert len(small_stack) == 5
