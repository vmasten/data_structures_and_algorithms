"""Implement a singly linked list in Python."""

from .node import Node


class LinkedList(object):
    """Class to implement a singly linked list in Python."""

    """__init__ initializes an empty list.
    __str__ return a string with current head value in friendly format
    __repr__ return a string with head and length for debugging
    __len__ Return length of linked list

    insert() adds a node to the linked list
    includes() checks for a specific value"""

    def __init__(self, iterable=None):
        """Initialize the linked list."""
        self.head = None
        self._size = 0

        if iterable is None:
            iterable = []

        if type(iterable) is not list:
            raise TypeError('iterable must be of type list')

        for val in iterable:
            self.insert(val)

    def __str__(self):
        """Return an fstring with the head of the linked list."""
        output = f'Linked List: Head val - {self.head}'
        return output

    def __repr__(self):
        """Return an fstring with the head and length of the linked list."""
        output = f'<LinkedList: head - {self.head} size - {self._size}>'
        return output

    def __len__(self):
        """Return the length of the linked list."""
        return self._size

    def insert(self, value):
        """Insert and links a new node at the head of the list."""
        self.head = Node(value, self.head)
        self._size += 1

    def includes(self, value):
        """Check whether a specific value is in the list."""
        result = False
        if self.head:
            while self.head:
                if self.head.val == value:
                    result = True
                self.head = self.head._next

        return result
