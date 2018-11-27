def insert_shift_array(list_input, new):
  """Given a list and a new element to add, returns a new list with the element added to the middle (odd list) or middle + 1 (even list) index
  """
  middle = (len(list_input) + 1) // 2
  new_list = []
  for i in range(len(list_input)):
    if i == middle:
      new_list.append(new)
      # The if/append is executed first because of zero-indexing
    new_list.append(list_input[i])
  return new_list

def uninsert_shift_array(list_input, removed):
  """Given a list and an element to remove, returns a new list with the desired element removed
  """
  new_list = []
  for i in range(len(list_input)):
    if list_input[i] == removed:
      continue
      # If the element to be remove is detected, the append is skipped and the loop continues to the next element
    new_list.append(list_input[i])
  return new_list
