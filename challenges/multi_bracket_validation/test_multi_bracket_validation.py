"""Test bracket validation function."""
from .multi_bracket_validation import validate


def test_initial_condition():
    """Test return if very first character is a closing bracket."""
    test_string = ']jerk'
    test = validate(test_string)
    assert test is False


def test_simple_input():
    """Test simple opening/closing brackets."""
    test_string = '{}'
    test = validate(test_string)
    assert test is True


def test_multiple_brackets():
    """Test multiple sets of brackets."""
    test_string = '{}(){}'
    test = validate(test_string)
    assert test is True


def test_brackets_and_characters():
    """Test brackets and characters."""
    test_string = '()[[Extra Characters]]'
    test = validate(test_string)
    assert test is True


def test_again():
    """Test another complicated set of brackets."""
    test_string = '(){}[[]]'
    test = validate(test_string)
    assert test is True


def test_false():
    """Test false condition with multiple brackets."""
    test_string = '[({}]'
    test = validate(test_string)
    assert test is False


def test_singleton():
    """Test false condition on single opening bracket."""
    test_string = '{'
    test = validate(test_string)
    assert test is False


def test_mismatched_brackets():
    """Test mismatched brackets."""
    test_string = '[}'
    test = validate(test_string)
    assert test is False


def test_complex_valid_input():
    """Test complex input from code challenge examples."""
    test_string = '{}{Code}[Fellows](())'
    test = validate(test_string)
    assert test is True


def test_no_bracket_input():
    """Test for validity with no brackets at all."""
    test_string = 'you awake in the dark, disoriented.'
    test = validate(test_string)
    assert test is True
