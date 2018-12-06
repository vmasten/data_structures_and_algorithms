from .linked_list import LinkedList

def merge_lists(first_list, second_list):
    output = LinkedList()
    if first_list.head and not second_list.head:
        output.head = first_list.head
        while first_list.head._next:
            output.head._next = first_list.head._next
            return output.head

    if second_list.head and not first_list.head:
        output.head = first_list.head
        while second_list.head._next:
            output.head._next = second_list.head._next
            return output.head

    output.head = first_list.head
    while first_list.head._next and second_list.head._next:
        output.head._next = first_list.head._next
        output.head._next = second_list.head._next
        first_list.head._next = first_list.head._next
        print(first_list.head)
        second_list.head._next = second_list.head._next
        print(second_list.head)

        if first_list.head._next is None and second_list.head._next is not None:
            while second_list.head._next:
                output.head._next = second_list.head._next
                second_list.head = second_list.head._next
        if second_list.head._next is None and first_list.head._next is not None:
            while first_list.head._next:
                output.head._next = first_list.head._next
                first_list.head = first_list.head._next
        return output.head
