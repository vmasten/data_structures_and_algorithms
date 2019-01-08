"""Module to implement an animal shelter queue using inherited classes."""
from .animal import Cat, Dog


class AnimalQueue(object):
    """A queue to hold animals."""

    def __init__(self):
        """Initialize the queue with front and back pointers."""
        self.front = None
        self.back = None
        self._size = 0


class AnimalShelter(object):
    """Holds the dog and cat queues and defines some functions."""

    """
    __init__ initializes the object with animal queues for dogs, cats
    enqueue(value) adds an item to dog or cat queue depending on value
    dequeue(val) removes the front item from dog or cat queue based on val

    """
    def __init__(self):
        """Initialize the shelter."""
        self.dog_queue = AnimalQueue()
        self.cat_queue = AnimalQueue()

    def enqueue(self, value):
        """Add an item to the designated queue(value)."""
        if value == 'dog':
            animal = Dog(value)
            if self.dog_queue._size == 0:
                # seems like the safest way to check for an empty queue
                self.dog_queue.front = animal
                self.dog_queue.back = animal
                self.dog_queue._size += 1
                return self

            self.dog_queue.back.next_node = animal
            self.dog_queue.back = animal
            self.dog_queue._size += 1
        if value == 'cat':
            animal = Cat(value)
            if self.cat_queue._size == 0:
                # seems like the safest way to check for an empty queue
                self.cat_queue.front = animal
                self.cat_queue.back = animal
                self.cat_queue._size += 1
                return self

            self.cat_queue.back.next_node = animal
            self.cat_queue.back = animal
            self.cat_queue._size += 1

        if value != 'dog' and value != 'cat':
            raise NameError('only dogs and cats are accepted at this shelter')

    def dequeue(self, val=None):
        """Remove the front node from designated queue(val) and return it."""
        if val == 'dog':
            if self.dog_queue.front:
                old_front = self.dog_queue.front
                self.dog_queue.front = old_front.next_node
                old_front.next_node = None

                return old_front

            if not self.dog_queue.front:
                return 'No dogs in the shelter (yay!)'

        if val == 'cat':
            if self.cat_queue.front:
                old_front = self.cat_queue.front
                self.cat_queue.front = old_front.next_node
                old_front.next_node = None

                return old_front

            if not self.cat_queue.front:
                return 'No cats in the shelter (yay!)'

        if val is None:
            return None
