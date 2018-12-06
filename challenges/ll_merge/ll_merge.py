"""Zip merges two linked lists.

input: two linked lists
output: the head of a new merged linked list
"""

from .linked_list import LinkedList


def merge_lists(first_list, second_list):
    """Merge the lists."""
    output = LinkedList()

    if first_list.head and not second_list.head:

        for i in range(first_list._size):
            output.append(first_list.head.val)
            first_list.head = first_list.head._next

        return output.head

    if second_list.head and not first_list.head:

        for i in range(second_list._size):
            output.append(second_list.head.val)
            second_list.head = second_list.head._next

        return output.head

    if first_list._size > second_list._size:

        for i in range(first_list._size):
            output.append(first_list.head.val)
            first_list.head = first_list.head._next

            if second_list.head:  # adds to output while true
                output.append(second_list.head.val)
                second_list.head = second_list.head._next

        return output.head

    if second_list._size > first_list._size:

        for i in range(second_list._size):

            if first_list.head:  # adds to output while true
                output.append(first_list.head.val)
                first_list.head = first_list.head._next
            output.append(second_list.head.val)
            second_list.head = second_list.head._next

        return output.head

    if first_list._size == second_list._size:

        for i in range(first_list._size):
            output.append(first_list.head.val)
            first_list.head = first_list.head._next
            output.append(second_list.head.val)
            second_list.head = second_list.head._next

        return output.head
