"""Tests for the repeated_word module."""
from .repeated_word import repeated_word


def test_repeated_word(example_string):
    """Test the function with an example string."""
    expected = 'it'
    actual = repeated_word(example_string)
    assert expected == actual


def test_repeated_word_again(example_two):
    """Test the function with a different string."""
    expected = 'a'
    actual = repeated_word(example_two)
    assert actual == expected


def test_empty_string(empty_string):
    """Test that empty string conditional is working properly."""
    expected = 'empty string!'
    actual = repeated_word(empty_string)
    assert actual == expected


def test_singleton(singleton):
    """Test single-word string conditional."""
    expected = 'string is too short!'
    actual = repeated_word(singleton)
    assert expected == actual


def test_example_three(example_three):
    """Test third example from challenge documentation."""
    expected = 'summer'
    actual = repeated_word(example_three)
    assert expected == actual


def test_bad_input(bad_data):
    """Test non-string conditional."""
    expected = 'wrong input type (must be string)!'
    actual = repeated_word(bad_data)
    assert expected == actual

def test_no_repeats_in_string(no_repeats):
    """Test the return at the bottom of the function."""
    expected = 'no match!'
    actual = repeated_word(no_repeats)
    assert expected == actual
