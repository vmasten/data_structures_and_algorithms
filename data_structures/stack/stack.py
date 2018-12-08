"""Implement a stack data structure in Python."""

from ..node.node import Node


class Stack(object):
    """Class to implement a stack in Python."""

    """
    __init__ initializes an empty stack.
    __len__ returns the current size of the stack.
    __str__ returns a string with the top value in friendly format.
    __repr__ returns a string with the top node for debugging.
    push() adds a node to the top of the stack.
    pop() removes the top node from the stack and returns the node's value.
    peek() returns the top node itself for possible manipulation
    """
    def __init__(self, iterable=None):
        """Initialize the stack, optionally using a list for input."""
        self.top = None
        self._size = 0

        if iterable is None:
            iterable = []

        if type(iterable) is not list:
            raise TypeError('iterable must be of type list')

        for val in iterable:
            self.push(val)
            # copied from linked list implementation

    def __len__(self):
        """Return the size of the stack."""
        return self._size

    def __str__(self):
        """Return an fstring with the value of the top of the stack."""
        output = f'Stack: Top value - {self.top.val}'
        return output

    def __repr__(self):
        """Return the top node for debugging purposes."""
        return f'<STACK Top: {self.top}>'

    def push(self, value):
        """Push a node onto the top of the stack."""
        node = Node(value)
        node.next_node = self.top
        self.top = node
        self._size += 1
        return self

    def pop(self):
        """Pop a node off the top of the stack."""
        if self.top:
            old_top = self.top
            self.top = old_top.next_node
            old_top.next_node = None
            self._size -= 1

            return old_top.val

        if not self.top:
            return 'Stack is empty!'

    def peek(self):
        """Return the top node itself for evaluation/manipulation."""
        if self.top:
            return self.top
        if not self.top:
            return 'Stack is empty!'
