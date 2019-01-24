"""Module to implement radix sort on a list of positive integers."""


def counting_sort(input, curr_exponent):
    """Helper function to sort each digit."""
    length = len(input)
    count = [0] * 10
    output = [0] * length
    # find the length of the input and
    # initialize the number of storage buckets needed
    # for sorting and output

    for i in range(length):
        index = (input[i]//curr_exponent)
        count[(index) % 10] += 1
        # single out the current digit
        # and put it into the appropriate bucket

    for i in range(1, 10):
        count[i] += count[i - 1]
        # shift the position to reflect base 10 indexing
        # rather than computer/Python list indexing

    i = length - 1
    while i >= 0:
        index = (input[i]//curr_exponent)
        output[count[(index) % 10] - 1] = input[i]
        count[(index) % 10] -= 1
        i -= 1
        # build the output list for the current digit

    i = 0
    for i in range(0, len(input)):
        input[i] = output[i]
        # copy the output list back to the input list


def radix_sort(input):
    """Use helper function to perform radix sort."""
    if not input:
        return 'empty list!'
        # if input list is empty, yell at the user

    maximum = max(input)
    # feels like a bit of a cheat, but this way we know
    # how many times to call the sort

    exponent = 1
    # start at the 1s as the least significant digit
    while maximum // exponent > 0:
        counting_sort(input, exponent)
        exponent *= 10
        # call counting sort for each digit (to the maximum)
        # and then multiply by 10 to get to the next

    return input
