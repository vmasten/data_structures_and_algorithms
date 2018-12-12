"""Define inherited animal classes for use in an animal shelter."""
from ...data_structures.node.node import Node


class Animal(Node):
    """Base class for inheritance."""

    def __init__(self, val):
        """Initialize the Animal object."""
        Node.__init__(self, val, next_node=None)
        self.counter = 0

    def __str__(self):
        """Return the value of the object for debugging."""
        return self.val


class Dog(Animal):
    """Inherits from Animal and increments an (unused) counter."""

    def __init__(self, val):
        """Initialize the Dog object."""
        Animal.__init__(self, val)
        self.counter += 1


class Cat(Animal):
    """Inherits from Animal and increments an (unused) counter."""

    def __init__(self, val):
        """Initialize the Cat object."""
        Animal.__init__(self, val)
        self.counter += 1
