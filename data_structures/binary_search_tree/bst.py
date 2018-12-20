"""Module to implement a binary search tree."""
from ..stack.queue import Queue


class Node(object):
    """Building block to create binary search trees."""

    def __init__(self, val=None, left=None, right=None):
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

    def __init__(self, iterable=None, traversal_list=[], max=None):
        """Initialize BST."""
        self.root = Node()
        self.traversal_list = traversal_list
        self.max = max

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

    def enlist(self, node):
        """Helper method for building lists during BST traversals."""
        self.traversal_list.append(node.val)
        return self.traversal_list

    def pre_order(self, node, operation):
        """Traverse the BST in pre order."""
        result = operation(node)
        # Read the node itself first

        if node.left is not None:
            self.pre_order(node.left, operation)
        if node.right is not None:
            self.pre_order(node.right, operation)
            # Read the left child, and then the right child
        # print(result)
        return result

    def in_order(self, node, operation):
        """Traverse the BST in order."""
        if node.left is not None:
            self.in_order(node.left, operation)
            # Read the left child

        result = operation(node)
        # Read the node itself

        if node.right is not None:
            self.in_order(node.right, operation)
            # Read the right child

        return result

    def post_order(self, node, operation):
        """Traverse the BST in post order."""
        if node.left is not None:
            self.post_order(node.left, operation)
            # Read the left child

        if node.right is not None:
            self.post_order(node.right, operation)
            # Read the right child

        result = operation(node)
        # Read the node itself
        return result

    def breadth_first_search(self, node, operation):
        """Breadth-first traversal for the BST."""
        queue = Queue()
        queue.enqueue(node)

        while queue.front:
            front = queue.dequeue()

            result = operation(front.val)

            if front.val.left is not None:
                queue.enqueue(front.val.left)
            if front.val.right is not None:
                queue.enqueue(front.val.right)

        return result

    def find_maximum_value_binary_tree(self, node):
        if not node.val:
            return None

        if not self.max:
            self.max = node.val

        if self.max < node.val:
            self.max = node.val

        return self.max
