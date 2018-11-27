from .array_shift import insert_shift_array
from .array_shift import uninsert_shift_array

def test_assert_true():
  """A quick proof of life to make sure the configuration is correct
  """
  assert True is True

def test_insert_shift_array_even():
  """tests the shift with an even number of list elements
  """
  initial = [1, 2, 3, 4]
  new = 5
  expected = [1, 2, 5, 3, 4]
  assert insert_shift_array(initial, new) == expected

def test_insert_shift_array_odd():
  """tests the shift with an odd number of elements
  """
  initial = [1, 2, 3, 4, 5]
  new = 6
  expected = [1, 2, 3, 6, 4, 5]
  assert insert_shift_array(initial, new) == expected

def test_insert_shift_array_large():
  """tests the shift with a large number of elements
  """
  initial = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
  new = 99
  expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 99, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
  assert insert_shift_array(initial, new) == expected

def test_uninsert_shift_array():
  """tests the stretch goal
  """
  initial = [1, 2, 3, 4, 5]
  removed = 4
  expected = [1, 2, 3, 5]
  assert uninsert_shift_array(initial, removed) == expected

def test_uninsert_shift_array_even():
  """a second test for the stretch goal given even elements just in case
  """
  initial = [1, 2, 3, 4, 5, 6]
  removed = 2
  expected = [1, 3, 4, 5, 6]
  assert uninsert_shift_array(initial, removed) == expected

  
