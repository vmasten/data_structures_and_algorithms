"""Implementation of selection sort."""


def selection_sort(list_to_sort):
    """Take in a list and sort it in place using selection sort algorithm."""
    if not list_to_sort:
        return 'empty list!'
        # nothing to sort

    for i in range(len(list_to_sort)):
        lowest_index = i
        # assumes the first index in the list contains the smallest item

        for j in range(i+1, len(list_to_sort)):

            if list_to_sort[j] < list_to_sort[lowest_index]:
                # if another item is smaller, re-set the index accordingly
                lowest_index = j

        list_to_sort[i], list_to_sort[lowest_index] = list_to_sort[lowest_index], list_to_sort[i]
        # once the smallest remaining item has been determined, swap it
        # with the current index of the outer loop (the original list index)

    return list_to_sort
