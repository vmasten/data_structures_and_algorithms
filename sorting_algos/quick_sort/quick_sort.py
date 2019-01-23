"""
Module to implement quick sort in Python.
Lightly adapted from GeeksforGeeks' implementation.
"""
def quick_sort(input_list, left, right):

    def partition(input_list, left, right):
        # helper function to accomplish quick sort
        i = (left - 1)
        pivot = input_list[right]
        # set left and right indices of pivot for comparison

        for j in range(left, right):
            if input_list[j] <= pivot:
                i = i + 1
                input_list[i], input_list[j] = input_list[j], input_list[i]
                # if an item is less than or equal to the pivot, increment
                # the index to prepare for a swap and then swap

        input_list[i + 1], input_list[right] = input_list[right], input_list[i + 1]
        # once the loop is complete, swap the item after the current index and
        # the far right item <-- I have to admit, I don't really understand this part
        return (i + 1)

    if left < right:
        # there's still work to do

        part = partition(input_list, left, right)
        # partition the list

        quick_sort(input_list, left, part - 1)
        # quick sort the left half

        quick_sort(input_list, part + 1, right)
        # quick sort the right half

    return input_list



