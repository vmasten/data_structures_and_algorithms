"""Tests for animal/cat/dog inherited classes."""
from .animal import Animal, Cat, Dog


def test_animal_instantiation_str():
    """Use str method to make sure Animal instantiation is correct."""
    test = Animal('Muffins')
    assert str(test) == 'Muffins'


def test_dog_instantiation_counter():
    """Test the (unused) counter on the Dog class."""
    test = Dog('Fluffy')
    assert test.counter == 1
    assert str(test) == 'Fluffy'


def test_cat_instantiation_counter():
    """Test the (unused) counter on the Cat class."""
    test = Cat('Mittens')
    assert test.counter == 1
    assert str(test) == 'Mittens'
