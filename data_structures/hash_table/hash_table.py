"""Module to implement a hash table data structure."""


class HashTable(object):
    """Implements a basic hash table that can take in strings and integers."""

    def __init__(self):
        """Instantiate the hash table."""
        self.hash_table = [None]*11

    def __len__(self):
        """Get the length of the hash table."""
        return len(self.hash_table)

    def hash(self, val):
        """Helper to hash a value before it is added to the table."""
        if type(val) == int:
            return val % len(self.hash_table)
        if type(val) == str:
            sum = 0
            for i in range(len(val)):
                sum += ord(val[i])
            return sum % len(self.hash_table)

    def setter(self, val):
        """Use the hash helper function to add a value to the table."""
        hashed = self.hash(val)
        if self.hash_table[hashed] is None:
            self.hash_table[hashed] = val
        elif type(self.hash_table[hashed]) != list:
            chain = []
            chain.append(self.hash_table[hashed])
            chain.append(val)
            self.hash_table[hashed] = chain
        else:
            self.hash_table[hashed].append(val)

    def getter(self, val):
        """Get a value if it exists in the table. Returns True if found."""
        hashed = self.hash(val)
        if self.hash_table[hashed] == val:
            return True
        elif type(self.hash_table[hashed]) == list:
            for i in range(len(self.hash_table[hashed])):
                if self.hash_table[hashed][i] == val:
                    return True
        return False
