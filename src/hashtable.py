# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        index = self._hash_mod(key)
        current_value = self.storage[index]

        # if there is a node that already exists with same key
        if current_value is not None:
            print("Warning", value, " Colliding ", current_value.value)

            # create new link pair
            newLinkPair = LinkedPair(key, value)
            newLinkPair.next = self.storage[index]
            self.storage[index] = newLinkPair
        # if node with same ke doesn't already exist, create link pair and add to storage
        else:
            self.storage[index] = LinkedPair(key, value)



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        # if the key can't be found
        if self.storage[index] is None:
            print("The Key has not been found")
        # set key in storage to None 
        else:
            self.storage[index] = None


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        current_key = self.storage[index]
        
        # if node is found, verify it matches
        while current_key:
            # if value does not match, move to next node and check again
            if current_key.key != key:
                current_key = current_key.next
            # if found, return value
            else:
                return current_key.value
        # return None if not found
        return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity *= 2
        previous_storage = self.storage
        self.storage = self.capacity * [None]

        # for each previous key in the storage
        for previous_keys in previous_storage:
            # set current key to previous key
            current_key = previous_keys
            # if key exists
            while current_key is not None:
                # insert node and move onto next key
                self.insert(current_key.key, current_key.value)
                current_key = current_key.next


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
