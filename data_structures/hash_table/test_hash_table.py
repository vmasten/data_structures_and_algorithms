"""Module to test hash table functionality."""
import pytest


def test_empty_hash_table_length(empty_hash_table):
    """Proof of life."""
    assert len(empty_hash_table) == 8192


def test_empty_hash_table_add(empty_hash_table):
    """Test adding a value to the empty table."""
    empty_hash_table.setter('abc', '1')
    actual = empty_hash_table.getter('abc')
    expected = '1'
    assert expected == actual


def test_setter_method(very_simple_hash_table):
    """Test that the table was instantiated correctly."""
    assert very_simple_hash_table.getter('blue') == '2'


def test_collision(very_simple_hash_table):
    """Test a collision on the hash table."""
    very_simple_hash_table.setter('bleu', '8')
    # 'bleu' should hash the same as 'blue'
    result1 = very_simple_hash_table.getter('blue')
    result2 = very_simple_hash_table.getter('bleu')
    assert result1 != result2


def test_overwrite(very_simple_hash_table):
    """Test that passing in the same key and a new value will overwrite."""
    very_simple_hash_table.setter('blue', '8')
    expected = '8'
    actual = very_simple_hash_table.getter('blue')
    assert expected == actual


def test_getter(very_simple_hash_table):
    """Test the getter method."""
    expected = 5
    actual = very_simple_hash_table.getter('red')
    assert expected == actual


def test_getter_bad_input(very_simple_hash_table):
    """Test the getter method with bad input."""
    with pytest.raises(KeyError):
        very_simple_hash_table.getter('black')


def test_getter_chain(very_simple_hash_table):
    """Test both setting and getting in the same function."""
    very_simple_hash_table.setter('black', '666')
    expected = '666'
    actual = very_simple_hash_table.getter('black')
    assert expected == actual


def test_str_hash_table(str_hash_table):
    """Test string setting/getting."""
    expected = 'bad'
    actual = str_hash_table.getter('cat')
    assert expected == actual


def test_str_setter(str_hash_table):
    """Test adding and getting a new string value."""
    str_hash_table.setter('wolf', 'best')
    expected = 'best'
    actual = str_hash_table.getter('wolf')
    assert expected == actual
