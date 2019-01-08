"""Implement a queue using two stacks."""

from ...data_structures.stack.stack import Stack


class PseudoQueue(object):
    """Implement a queue data structure using two stacks."""

    def __init__(self, iterable=None):
        """Initialize the queue."""
        self.front = Stack()
        self.rear = Stack()

        if iterable is None:
            iterable = []

        if type(iterable) is not list:
            raise TypeError('iterable must be of type list')

        for val in iterable:
            self.enqueue(val)

    def enqueue(self, val):
        """Add an item to the rear of the queue."""
        self.rear.push(val)
        return self

    def dequeue(self):
        """Flip the stack on its head to dequeue the first item added."""
        while self.rear.top:
            temp = self.rear.pop()
            self.front.push(temp)
            # flip and reverse the stack like a slinky (thanks, JB!)

        result = self.front.pop()
        # extract the node to be dequeued

        while self.front.top:
            temp = self.front.pop()
            self.rear.push(temp)
            # reflow the remaining stack into its original order

        return result

