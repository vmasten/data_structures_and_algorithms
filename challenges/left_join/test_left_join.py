"""Tests for left join function."""
from .left_join import left_join


def test_traversal(hash_table):
    """Not really a test, just poking at how to traverse the hash table."""
    for i in range(len(hash_table)):
        if hash_table.hash_table[i]:
            print(hash_table.hash_table[i][0])


def test_left_join(hash_table, hash_table_two):
        """Basic test of the function."""
        actual = left_join(hash_table, hash_table_two)
        expected = 'averse'
        assert actual[0][2] == expected


def test_left_join_other_way(hash_table, hash_table_two):
    """Test joining the other way."""
    actual = left_join(hash_table_two, hash_table)
    expected = 'guide'
    assert actual[1][0] == expected


def test_empty_input(hash_table, empty_hash_table):
    """See what happens if the joining table is empty."""
    actual = left_join(hash_table, empty_hash_table)
    expected = 4
    # we get back the original inputs in lists
    assert len(actual) == expected


def test_empty_input_left(empty_hash_table, hash_table):
    """Test what happens when the table to join on is empty."""
    actual = left_join(empty_hash_table, hash_table)
    expected = 0
    # nothing to join!
    assert len(actual) == expected

