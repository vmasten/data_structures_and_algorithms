"""Module to implement a hash table data structure."""


class HashTable(object):
    """Implements a basic hash table that can take in strings and integers."""
    entries = 0

    def __init__(self):
        """Instantiate the hash table."""
        self.hash_table = [[] for i in range(8192)]

    def __len__(self):
        """Get the length of the hash table."""
        return len(self.hash_table)

    def __repr__(self):
        """Return dev-friendly detail about the hash table."""
        return "<HashTable: {}>".format(self.hash_table)

    def hash(self, val):
        """Helper to hash a value before it is added to the table."""
        if type(val) == int:
            return val % len(self.hash_table)
        if type(val) == str:
            sum = 0
            for i in range(len(val)):
                sum += ord(val[i])
            return sum % len(self.hash_table)

    def setter(self, key, val):
        """Use the hash helper function to add a key/value to the table."""
        hashed = self.hash(key)
        for i, item in enumerate(self.hash_table[hashed]):
            if item[0] == key:
                del self.hash_table[hashed][i]
                self.entries -= 1
        self.hash_table[hashed].append((key, val))
        self.entries += 1

    def getter(self, key):
        """Get a value if it exists in the table."""
        hashed = self.hash(key)
        for i, item in enumerate(self.hash_table[hashed]):
            if item[0] == key:
                return item[1]
        raise KeyError('Key not in hash table.')
