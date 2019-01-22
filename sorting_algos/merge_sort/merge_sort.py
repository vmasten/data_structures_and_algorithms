def merge_sort(input_list):
    if len(input_list) > 1:
        middle = len(input_list) // 2
        left = input_list[:middle]
        right = input_list[middle:]
        #slice the list into halves (repeatedly)

        merge_sort(left)
        merge_sort(right)
        # call the function recursively on each half

        i = j = k = 0

        while i < len(left) and j < len(right):
            # walk each half of each slice with its own index
            # sorting the slices in place
            if left[i] < right[j]:
                input_list[k] = left[i]
                i += 1
                # increment the left index
            else:
                input_list[k] = right[j]
                j += 1
                # increment the right index
            k += 1
            # regardless, increment the index of the original list

        while i < len(left):
            input_list[k] = left[i]
            i += 1
            k += 1
            # recombine the left

        while j < len(right):
            input_list[k] = right[j]
            j += 1
            k += 1
            # recombine the right

    return input_list
    # profit
