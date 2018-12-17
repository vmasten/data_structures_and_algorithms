"""Function to traverse a binary tree and apply FizzBuzz algorithm."""


def FizzBuzzTree(tree):
    """Implement FizzBuzz algorithm on a binary tree."""
    if tree.left is not None:
        FizzBuzzTree(tree.left)

    if tree.val is not None:
        # if so, the tree is empty
        if tree.val % 15 == 0:
            tree.val = 'FizzBuzz'

        elif tree.val % 3 == 0 and tree.val % 5 != 0:
            tree.val = 'Fizz'

        elif tree.val % 5 == 0 and tree.val % 3 != 0:
            tree.val = 'Buzz'

    if tree.right is not None:
        FizzBuzzTree(tree.right)

    return tree
