"""Simple module that performs a binary search on a sorted list."""


def binary_search(list, key):
    """
    Find the desired key in a sorted list.

    Input is a sorted list and key.
    The function splits the list in half and checks to see if
    the key is in the upper or lower half of the split
    Returns the key if it's in the list, or -1 if it's not
    """
    left = 0
    right = len(list)
    print(right)
    while True:
        mid = (left + right) // 2
        print(mid)
        if list[mid] == key:
            return mid
        if key > list[mid]:
            left = mid
        if key < list[mid]:
            right = mid
        if right - left == 1:
            if list[left] == key:
                return left
            if list[right] == key:
                return right
            return -1
