"""Module to find the intersection of two trees."""


def tree_intersection(tree1, tree2):
    """Find intersecting nodes in two trees."""

    if type(tree1.root.val) is not int or type(tree2.root.val) is not int:
        return 'Input nodes must be integers!'

    result = set()

    def in_order(node):
        """Helper function to traverse the tree and check for intersection."""
        if node.left is not None:
            in_order(node.left)

        if node.val in traversal:
            result.add(node.val)

        if node.right is not None:
            in_order(node.right)

    traversal = tree1.in_order(tree1.root, tree1.enlist)
    in_order(tree2.root)

    return result
