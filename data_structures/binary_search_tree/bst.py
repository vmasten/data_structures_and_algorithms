"""Module to implement a binary search tree."""


class Node(object):
    """Building block to create binary search trees."""

    def __init__(self, val, left=None, right=None):
        """Initialize node object."""
        self.left = left
        self.right = right
        self.val = val

    def __str__(self):
        """Display value of the node."""
        output = f'Node: value - {self.val}'
        return output

    def __repr__(self):
        """Display debugging-friendly node information."""
        output = f'<Node: value - {self.val} left - {self.left} right - {self.right}>'
        return output


class BST(object):
    """Binary search tree data structure."""

    def __init__(self, iterable=None, traversal_list=[]):
        """Initialize BST."""
        self.root = Node(val=None)
        self.traversal_list = traversal_list

        if iterable is None:
            iterable = []

        if type(iterable) is not list:
            raise TypeError('iterable must be of type list')

        for val in iterable:
            self.insert(val, self.root)

    def __str__(self):
        """Return BST root info."""
        output = f'BST: Root - {self.root}'
        return output

    def __repr__(self):
        """Return BST info for debugging."""
        output = f'<BST: - {self.root}>'
        return output

    def insert(self, val, node):
        """Insert new node into BST based on BST properties (see comments)."""
        if node.val is None:
            node.val = val
            return
            # Root was empty

        if val < node.val:
            # left insertion
            if node.left is None:
                node.left = Node(val)
                # Create a child node
            else:
                self.insert(val, node.left)
                # Try again with the child's left node

        elif val > node.val:
            # right insertion
            if node.right is None:
                node.right = Node(val)
                # Create a child node
            else:
                self.insert(val, node.right)
                # Try again with the child's left node

    def enlist(self, node, traversal_list):
        """Helper method for building lists during BST traversals."""
        self.traversal_list.append(node.val)

    def pre_order(self, node, enlist):
        """Traverse the BST in pre order."""
        self.enlist(node, self.traversal_list)
        # Read the node itself first

        if node.left is not None:
            self.pre_order(node.left, self.traversal_list)
        if node.right is not None:
            self.pre_order(node.right, self.traversal_list)
            # Read the left child, and then the right child

        return self.traversal_list

    def in_order(self, node, enlist):
        """Traverse the BST in order."""
        if node.left is not None:
            self.in_order(node.left, self.traversal_list)
            # Read the left child

        self.enlist(node, self.traversal_list)
        # Read the node itself

        if node.right is not None:
            self.in_order(node.right, self.traversal_list)
            # Read the right child

        return self.traversal_list

    def post_order(self, node, enlist):
        """Traverse the BST in post order."""
        if node.left is not None:
            self.post_order(node.left, self.traversal_list)
            # Read the left child

        if node.right is not None:
            self.post_order(node.right, self.traversal_list)
            # Read the right child

        self.enlist(node, self.traversal_list)
        # Read the node itself

        return self.traversal_list
