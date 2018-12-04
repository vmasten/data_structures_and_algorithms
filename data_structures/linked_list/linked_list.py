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

    def append(self, value):
        """Add a node to the end of the list."""
        if self.head:
            current = self.head
            while current._next:
                current = current._next

            current._next = Node(value)
            self._size += 1
        else:
            # linked list was empty
            self.insert(value)

    def insert_after(self, value, new_value):
        """Add a node after a given input value."""
        if self.head:
            current = self.head
            inserted = False
            while current._next:

                if current.val == value:
                    new_node = Node(new_value, current._next)
                    current._next = new_node
                    self._size += 1
                    inserted = True
                    return
                    # item was found in the loop
                current = current._next

            if current.val == value:
                    new_node = Node(new_value, current._next)
                    current._next = new_node
                    self._size += 1
                    inserted = True
                    # item is inserted at the end of the list

            if inserted is False:
                print('value to be inserted after is not in the list')
                return inserted

    def insert_before(self, value, new_value):
        """Add a node before a given input value."""
        if self.head:
            current = self.head
            inserted = False
            if current.val == value:
                new_node = Node(new_value, current)
                self.head = new_node
                self._size += 1
                inserted = True
                # item is inserted at the beginning of the list

            while current._next:
                if current._next.val == value:
                    new_node = Node(new_value, current._next)
                    current._next = new_node
                    self._size += 1
                    inserted = True
                    return
                    # item was found in the loop
                current = current._next

            if inserted is False:
                print('value to be inserted before is not in the list')
                return inserted

    def kth_from_end(self, k):
        """Find the kth node from the end of the linked list."""
        found = False
        find = self.head
        result = self.head
        if not self.head:
            return found
            # list is empty

        for i in range(k):
            if find._next is None:
                return found
                # k invoked the lookahead to traverse too far out
            find = find._next
            # sets the lookahead

        while find:
            find = find._next
            result = result._next
            # result and find move synchronously until the lookahead reaches
            # the end of the list
        return result.val
