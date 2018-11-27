def insert_shift_array(list_input, new):
  middle = (len(list_input) + 1) // 2
  print(middle)
  new_list = []
  for i in range(len(list_input)):
    if i == middle:
      new_list.append(new)
    new_list.append(list_input[i])
  return new_list

def uninsert_shift_array(list_input, removed):
  new_list = []
  for i in range(len(list_input)):
    if list_input[i] == removed:
      continue
    new_list.append(list_input[i])
  return new_list
