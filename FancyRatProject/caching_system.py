'''
**High Level*: Algorithms and Data Structures

Category:
Hashing

Topic:
Linear Probing

Operation for 1st prompt (you only need to follow this for your 1st prompt):

Other: Any code related task that you think is interesting or useful to programmers.
-----------------------------------------------------------------------------------------------

1. what is the purpose of linear probing in general ?

The purpose of linear probing is to resolve collisions that occur in hashing algorithms or 
data structures. It is a process used in a hash table to find the position of a key in the table. 
The process starts by comparing the key against the first entry in the table. If the key and the first 
entry are the same, the process is successful. If the key and the first entry are not the same, 
the process continues to the next entry in the table until a match is found. If there is no match 
found after searching the entire table, the key is considered to be absent from the table.

The aim is to minimise collisions and store elements in the hash table efficiently by using 
linear probing. It allows for open addressing. All elements are stored directly in the table 
itself, without the need for additional data structures to handle collisions. Memory efficiency 
and cache performance can be improved as a result.

Here’s an example of implementing linear probing for a hash table in Python:

class HashTable:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    def hash_function(self, key):
        # A simple hash function example
        return key % self.size

    def insert(self, key, value):
        hash_index = self.hash_function(key)

        while self.keys[hash_index] is not None:
            # Linear probing: move to the next slot
            hash_index = (hash_index + 1) % self.size

        # Store the key and value in the found slot
        self.keys[hash_index] = key
        self.values[hash_index] = value

    def search(self, key):
        hash_index = self.hash_function(key)

        while self.keys[hash_index] is not None:
            if self.keys[hash_index] == key:
                # Return the value if key is found
                return self.values[hash_index]

            # Linear probing: move to the next slot
            hash_index = (hash_index + 1) % self.size

        # Key not found
        return None
A HashTable class that uses linear probing for collision resolution is defined in this example. 
The size of the hash table is determined by the size parameter in the constructor.

This method computes a hash index based on key and table size.

A key-value pair is inserted into the hash table by the insert method. Using the hash function, 
it starts by calculating the initial hash index. It probes linearly by moving to the next slot until 
an empty slot is found if the slot at that index is already occupied. At that point it will store the 
key and the value in that slot.

The searching method searches the hashed table for a key. Using the hash function, it starts by 
calculating the initial hash index. It checks whether the key matches if the slot is occupied by 
that index. If this is the case, it returns the corresponding value. If it does not, it continues 
with a linear search until the key is found or an empty slot is found.

Note that this is a simplified example for the purposes of illustration only. You may need to deal 
with resizing, deletion and other considerations based on your specific requirements in a practical 
implementation.

2. can you adapt the code for caching systems ?

The following is a modified version of the previous implementation for a caching system example 
that incorporates the key features of linear probing:
'''
class CachingSystem:
    def __init__(self, initial_size):
        self.size = initial_size
        self.keys = [None] * self.size
        self.values = [None] * self.size
        self.load_factor = 0  # Tracks the current load factor

    def hash_function(self, key):
        # A simple hash function example
        return hash(key) % self.size

    def resize(self, new_size):
        # Resize the hash table and rehash all key-value pairs
        old_keys = self.keys.copy()
        old_values = self.values.copy()

        self.size = new_size
        self.keys = [None] * self.size
        self.values = [None] * self.size
        self.load_factor = 0

        for i in range(len(old_keys)):
            if old_keys[i] is not None:
                self.insert(old_keys[i], old_values[i])

    def insert(self, key, value):
        if self.load_factor >= 0.7:
            # Resize the hash table if the load factor exceeds 0.7
            new_size = self.size * 2
            self.resize(new_size)

        hash_index = self.hash_function(key)

        while self.keys[hash_index] is not None:
            # Linear probing: move to the next slot
            hash_index = (hash_index + 1) % self.size

        # Store the key and value in the found slot
        self.keys[hash_index] = key
        self.values[hash_index] = value
        self.load_factor = sum(1 for k in self.keys if k is not None) / self.size

    def delete(self, key):
        hash_index = self.hash_function(key)

        while self.keys[hash_index] is not None:
            if self.keys[hash_index] == key:
                # Delete the key-value pair
                self.keys[hash_index] = None
                self.values[hash_index] = None
                self.load_factor = sum(1 for k in self.keys if k is not None) / self.size
                return

            # Linear probing: move to the next slot
            hash_index = (hash_index + 1) % self.size

    def get(self, key):
        hash_index = self.hash_function(key)

        while self.keys[hash_index] is not None:
            if self.keys[hash_index] == key:
                # Return the value if key is found
                return self.values[hash_index]

            # Linear probing: move to the next slot
            hash_index = (hash_index + 1) % self.size

        # Key not found
        return None
'''
The CachingSystem class represents a caching system that uses linear probing as its collision 
resolution technique in this adapted code. Its main features include
- **Resizing** — When the load factor exceeds 0.7, the Resize method is called. In order to maintain 
an efficient load factor, it resizes the hash table by doubling its size and rehashes all key-value pairs.
- **Insertion** — Insertion checks the load factor and resizes if necessary. It then uses linear probing 
to find the next free slot in the table and stores the key-value pair in it.
- **Deletion** — Using linear probing, the delete method searches for the specified key. If it is found, 
it deletes the key-value pair by marking the slots as 'None' and updates the load factor as appropriate.
- **Retrieval** — The get method scans for the specified key using linear scanning and returns the 
corresponding value if found.

Through the inclusion of resize, delete and load factor tracking.


3. How does the hash_function method work in this system?

The hash_function method in this caching system is responsible for determining the slot or index 
where a key-value pair will be stored in the hash table. The hash_function method uses the hash() 
function to map the key to an index in the hash table. The hash function uses the key and the size 
of the table to calculate the index.

The supplied code uses a simple hash function example that calculates the hash code by modulo the 
key's hash value with the hash table size (hash(key) % self.size). Hashing transforms a key into a 
whole number and applies a modulo operation to limit its result to a range of size of a hashed table.

In determining the initial location for storing key-value pairs, the role of the hash_function 
method is critical. It allows efficient retrieval of the corresponding value by mapping the key 
to a specific index in the hash table. By using the same hash function for both insertion and 
retrieval, the cache system guarantees consistent key mapping to the same place, which allows 
for successful retrieval of key and value pairs during lookups.

It's important to note, however, that hash functions are not perfect and can lead to collisions, 
where two different keys will produce the same hash code. In such cases, linear probing, as 
implemented in the code, is used to handle collisions. It finds the next available slot by 
sequentially probing the successive indices until an empty slot is found.



4. How does the caching system in this code handle collisions?


The caching system in this code uses linear probing to handle collisions. If the load factor 
exceeds 0.7, the resize method is called, which resizes the hash table by doubling its size 
and rehashes all key-value pairs. When a key is inserted, the hash_function method is used 
to calculate the hash index where the key and value should be stored. If the hash index is 
already taken, the key and value are stored in the next available slot by using linear probing. 
This process is repeated until an empty slot is found.

Here's a breakdown of the process:

1. A key and value are inserted into the cache system via the insert method. The code will 
first try to insert the key and value pair at the hashed index. It enters a loop to handle 
the collision if the index is already occupied.
2. The hash_function method calculates the hash index where the key and value should be 
stored. Within the loop, the code sequentially moves to the next slot by incrementing the 
hash index using the formula (hash_index + 1) % self.size. This ensures that the probing 
wraps around to the beginning of the hash table if the end is reached.
3. If the hash index is already taken, the key and value are stored in the next available 
slot by using linear probing. This is repeated until an empty slot is found. The code continues 
to probe the subsequent indices until an empty slot is found (i.e., self.keys[hash_index] is None).
4. Once an empty slot is found, the key and value are stored in it, and the load factor is updated.

This process is repeated until all keys and values have been inserted into the cache system. Through 
the use of linear probing, the caching system ensures that even in the presence of collisions, keys 
are stored in the hash table without data loss. However, it's important to note that linear probing 
can lead to clustering, where successive occupied slots are formed, potentially affecting the efficiency 
of insertion and retrieval operations. In order to mitigate this, the code includes a resizing function 
to accommodate more entries and maintain a lower load factor, thereby reducing the likelihood of collisions 
and clustering.


5.  How is the load factor calculated and why is it important in a caching system?

The load factor is a measure of the efficiency of a hash table in a caching system. It is the 
number of keys divided by the size of the hash table. In the provided code, the load factor is 
calculated using the formula load_factor = count / size.

The load factor is important because it helps to determine if the hash table is full or 
nearly full. If the load factor exceeds 0.7, the resize method is called, which resizes the 
hash table by doubling its size and rehashes all key-value pairs. This is done to prevent collisions 
and improve the efficiency of the caching system.

A high load factor indicates that the hash table is holding a large number of keys and may be 
approaching its maximum capacity. If the load factor is close to 1.0, the table is effectively 
full and new insertions will fail.

The load factor is used as a heuristic to determine the appropriate time to resize the table to 
avoid collisions and ensure the efficient use of resources.

Here's a step-by-step explanation of the load factor calculation and resizing process in the 
provided caching system:
1. Calculating the load factor:
- Load factor is calculated as the ratio of number of keys (self.count) to hash table size (self.size).
- The formula used to calculate the load factor is as follows: load_factor = self.count / self.size.
2. The insert operation:
- The load factor is checked before inserting a new key-value pair using the insert method.
- It indicates that the hash table is becoming overcrowded if the load factor exceeds the 
threshold (0.7 in this case), and resizing is required.
3. Operation resize:
- The resize method is called to increase the size of the hash table when resizing is triggered.
- The new hash size is typically twice the current size (new_size = self.size * 2).
- The following steps are performed by the resize method:
- Create temporary arrays for the storage of the old keys and values (old_keys and old_values) 
from the original hash table.
- Updates the size of the hash table (self.size) to the new size.
- Using the updated size, create new arrays for keys and values.
- Use the insert method to rewrite all key-value pairs from the temporary arrays into the new arrays.
- Dividing the current number of keys (self.count) by the new size of the hash table, recalculate 
the load factor (self.load_factor).
- The hashed table is now re-sized and ready to use.
4. Continuing operations:
- Since the hash table has been resized to accommodate more entries after the resizing operation, 
insertion of the new key-value pair continues.
- The load factor will be checked again for future insertions, and if the load factor exceeds the 
threshold value, the resizing operation may be triggered again.

This allows the cache system to adapt to the number of key and value pairs, ensuring optimal performance.

'''