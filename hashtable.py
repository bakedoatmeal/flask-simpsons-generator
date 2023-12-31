#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = []
        for i in range(init_size):
            self.buckets.append(LinkedList())

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = []
        for key, val in self.items():
            items.append('{!r}: {!r}'.format(key, val))
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all buckets
        # TODO: Collect all values in each bucket
        all_values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all buckets
        # TODO: Count number of key-value entries in each bucket
        length = 0
        for bucket in self.buckets: 
            length += bucket.length()
        return length

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        bucket_index = hash(key) % len(self.buckets)
        bucket = self.buckets[bucket_index]
        found = bucket.find_if_matches(lambda entry: entry[0] == key)
        if found is not None: 
            return True
        else: 
            return False


    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        bucket_index = hash(key) % len(self.buckets)
        # TODO: Check if key-value entry exists in bucket
        bucket = self.buckets[bucket_index]
        # TODO: If found, return value associated with given key
        entry = bucket.find_if_matches(lambda entry: entry[0] == key)
        if entry is not None: 
            value = entry[1]
            return value
        else: 
            raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        bucket_index = hash(key) % len(self.buckets)
        # TODO: Check if key-value entry exists in bucket
        bucket = self.buckets[bucket_index]
        node = bucket.head
        while node: 
            if node.data[0] == key:
                node.data = (key, value)
                return
            node = node.next
        bucket.append((key, value))
        # TODO: If found, update value associated with given key
        # TODO: Otherwise, insert given key-value entry into bucket
            
    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        bucket_index = hash(key) % len(self.buckets)
        bucket = self.buckets[bucket_index]
        found = bucket.find_if_matches(lambda entry: entry[0] == key)
        if found is None:
            raise KeyError('Key not found: {}'.format(key))
        else: 
            bucket.delete((found))
        # TODO: If found, delete entry associated with given key
        # TODO: Otherwise, raise error to tell user delete failed
        # Hint: raise KeyError('Key not found: {}'.format(key))

if __name__ == '__main__':
    ht = HashTable()
    print('hash table: {}'.format(ht))
    print(hash("HELLOOOO") % 8)
    print(hash("HELLOOOO") % 8)
    print(hash("jane") % 8)

