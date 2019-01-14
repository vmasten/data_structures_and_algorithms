"""Uses a predefined hash table to find the first repeated word in a string."""
from ...data_structures.hash_table.hash_table import HashTable


def repeated_word(string):
    """Look in a string for the first repeated word."""
    if type(string) is not str:
        return 'wrong input type (must be string)!'

    if string == '':
        return 'empty string!'

    split_string = ''.join(
                          (char if char.isalpha() else " ")
                          for char in string).split()
    # I originally wrote the function using just string.split(),
    # but found this on Stack Overflow when I realized
    # that I was capturing punctuation, throwing off the comparisons.

    if len(split_string) == 1:
        return 'string is too short!'

    h = HashTable()
    for i in range(len(split_string)):
        if h.getter(split_string[i]):
            return split_string[i]
        else:
            h.setter(split_string[i])

    return 'no match!'
