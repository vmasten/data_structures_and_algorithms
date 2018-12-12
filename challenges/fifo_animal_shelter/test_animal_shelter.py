"""Test animal shelter implementation."""
from .fifo_animal_shelter import AnimalShelter
import pytest


@pytest.fixture
def empty_animal_shelter():
    """Empty shelter for testing."""
    return AnimalShelter()


@pytest.fixture
def small_animal_shelter():
    """Small shelter for testing."""
    shelter = AnimalShelter()
    shelter.enqueue('dog')
    shelter.enqueue('cat')
    shelter.enqueue('dog')
    shelter.enqueue('dog')
    return shelter


def test_enqueue():
    """Test the enqueue function."""
    test = AnimalShelter()
    test.enqueue('dog')
    test.enqueue('dog')
    assert test.dog_queue.front.val == 'dog'


def test_enqueue_multiple_animal_types():
    """Test the enqueue function with both dogs and cats."""
    test = AnimalShelter()
    test.enqueue('dog')
    test.enqueue('cat')
    assert test.cat_queue.back.val == 'cat'


def test_dequeue(small_animal_shelter):
    """Test the dequeue function."""
    actual = small_animal_shelter.dequeue('dog')
    expected = 'dog'
    assert actual.val == expected


def test_dequeue_no_pref(small_animal_shelter):
    """Test dequeue with no preference."""
    assert small_animal_shelter.dequeue() is None


def test_multiple_to_empty_dequeue_cats(small_animal_shelter):
    """Test dequeueing both dogs and cats, ending with an empty cat queue."""
    small_animal_shelter.dequeue('dog')
    small_animal_shelter.dequeue('dog')
    small_animal_shelter.dequeue('cat')
    actual = small_animal_shelter.dequeue('cat')
    expected = 'No cats in the shelter (yay!)'
    assert small_animal_shelter.dog_queue.front.val == 'dog'
    assert actual == expected


def test_multiple_to_empty_dequeue_dogs(small_animal_shelter):
    """Empty out the dog queue to test the empty conditional."""
    small_animal_shelter.dequeue('dog')
    small_animal_shelter.dequeue('dog')
    small_animal_shelter.dequeue('dog')
    actual = small_animal_shelter.dequeue('dog')
    expected = 'No dogs in the shelter (yay!)'
    assert actual == expected


def test_bad_input(empty_animal_shelter):
    """Try to enqueue another animal."""
    with pytest.raises(NameError):
        empty_animal_shelter.enqueue('rabbit')
