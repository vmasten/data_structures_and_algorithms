"""Implement a node object for use in a singly linked list data structure."""


class Node(object):
    """Create a node object."""

    """ __init__ instantiates the node
        __str__ returns the value at the node"""

    def __init__(self, val, next_node=None):
        """Initialize the node with a value and a null pointer."""
        self.val = val
        self.next_node = next_node

    def __str__(self):
        """Return an fstring with the value of the node."""
        output = f'{self.val}'
        return output
