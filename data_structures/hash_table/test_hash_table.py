"""Module to test hash table functionality."""


def test_empty_hash_table_length(empty_hash_table):
    """Proof of life."""
    assert len(empty_hash_table) == 11


def test_empty_hash_table_add(empty_hash_table):
    """Test adding a value to the empty table."""
    empty_hash_table.setter('abc')
    assert empty_hash_table.hash_table[8] == 'abc'


def test_setter_method(very_simple_hash_table):
    """Test that the table was instantiated correctly."""
    assert very_simple_hash_table.hash_table[2] == 2


def test_collision(very_simple_hash_table):
    """Test a collision on the hash table."""
    very_simple_hash_table.setter(13)
    assert very_simple_hash_table.hash_table[2] == [2, 13]


def test_multiple_collisions(very_simple_hash_table):
    """Test that multiple collisions add to the list at the hashed value."""
    very_simple_hash_table.setter(13)
    very_simple_hash_table.setter(24)
    very_simple_hash_table.setter(35)
    expected = 24
    actual = very_simple_hash_table.hash_table[2][2]
    assert expected == actual


def test_getter(very_simple_hash_table):
    """Test the getter method."""
    expected = True
    actual = very_simple_hash_table.getter(2)
    assert expected == actual


def test_getter_bad_input(very_simple_hash_table):
    """Test the getter method with bad input."""
    expected = False
    actual = very_simple_hash_table.getter(22)
    assert expected == actual


def test_getter_chain(very_simple_hash_table):
    """Test both setting and getting in the same function."""
    expected = True
    very_simple_hash_table.setter(13)
    actual = very_simple_hash_table.getter(13)
    assert expected == actual


def test_str_hash_table(str_hash_table):
    """Test string setting/getting."""
    expected = True
    actual = str_hash_table.getter('cat')
    assert expected == actual


def test_str_setter(str_hash_table):
    """Test adding and getting a new string value."""
    expected = True
    str_hash_table.setter('wolf')
    actual = str_hash_table.getter('wolf')
    assert expected == actual
