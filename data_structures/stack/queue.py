"""Implement a queue data structure in Python."""

from ..node.node import Node


class Queue(object):
    """Class to implement a queue in Python."""

    """
    __init__ initializes an empty queue.
    __len__ returns the current size of the queue.
    __str__ returns a string with the front value in friendly format.
    __repr__ returns a string with the front node for debugging.
    enqueue() adds a node to the back of the queue.
    dequeue() removes and returns the node at the front of the queue.
    """

    def __init__(self, iterable=None):
        """Initialize the queue."""
        self.front = None
        self.back = None
        self._size = 0

        if iterable is None:
            iterable = []

        if type(iterable) is not list:
            raise TypeError('iterable must be of type list')

        for val in iterable:
            self.enqueue(val)
            # copied from linked list implementation

    def __len__(self):
        """Return the length of the queue."""
        return self._size

    def __str__(self):
        """Return the value of the front node in the queue."""
        return f'Queue: Front value: {self.front.val}'

    def __repr__(self):
        """Return the top node for debugging purposes."""
        return f'<QUEUE Front: {self.front}>'

    def enqueue(self, value):
        """Add an item to the end (and/or front if necessary) of the queue."""
        node = Node(value)
        if self._size == 0:
            # seems like the safest way to check for an empty queue
            self.front = node
            self.back = node
            self._size += 1
            return self

        self.back.next_node = node
        self.back = node
        self._size += 1
        return self

    def dequeue(self):
        """Remove the front node from the queue and return it."""
        if self.front:
            old_front = self.front
            self.front = old_front.next_node
            old_front.next_node = None

            return old_front

        if not self.front:
            return 'Queue is empty!'
