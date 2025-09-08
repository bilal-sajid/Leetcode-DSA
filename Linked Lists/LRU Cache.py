"""
Implement the Least Recently Used (LRU) cache class LRUCache. The class should support the following operations

LRUCache(int capacity): Initialize the LRU cache of size capacity.

int get(int key): Return the value to the key if the key exists, otherwise return -1.

void put(int key, int value): Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. 
If the introduction of the new pair causes the cache to exceed its capacity, remove the least recently used key.

A key is considered used if a get or a put operation is called on it.

Ensure that get and put each run in O(1) average time complexity.

"""

"""
Inputs:
    - capacity: int
    - key: int
    - key, value: int, int

Outputs:
    - None (Initializing the class with capacity)
    - value: int
    - None (Updating the value, adding the key:value pair or removing the LRU)

Considerations:
    - What values can the key/value pairs take: 0 <= key, value <= 1000
    - Values for capacity: 1 <= capacity <= 100

Idea 1 (Hashmap):
    - Can add and update key:value pairs in O(1) time - Will take O(n) space

    - We can even put a new key in O(1) time BUT we would need an O(n) time operation to find the LRU key
        - Example is we can add a 'time' value to each key:value pair then go over the entire hashmap and look for the time that is least
        - Whenever we get a value, we would update this time
    
    get: O(1) time
    put: O(n) time

    
Idea 2 (Hashmap + Linked List Hybrid):
    - Keep the hashmap approach but instead of mapping keys with values, we map keys to Node objects
    - Each node would have the value of the key:value pairing

    We can create a doubly linked list (since we need to add and remove from that node) with a sentinal head and sentinal tail

    LRU -> MRU
        <-
    
    Every time a key, value is put OR a get is done on it we add/update it to the MRU side
    When length of hashmap exceeds capacity, we remove from LRU side

    Main idea:
        - Use hashmap to find the Node that is associated with the current key in O(1)
        - Use linked list to get LRU and remove from the linked list and hashmap
    
    get: O(1) time
    put: O(1) time

"""

class Node:
    def __init__(self, key=-1, val=-1, next = None, prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.hashmap = {}

        self.LRU = Node()
        self.MRU = Node()

        self.LRU.next = self.MRU
        self.MRU.prev = self.LRU
    
    def add_to_mru(self, node):
        prev_node, next_node = self.MRU.prev, self.MRU
        prev_node.next, next_node.prev = node, node
        node.prev, node.next = prev_node, next_node
    
    def remove_node(self, curr_node):
        prev_node, next_node = curr_node.prev, curr_node.next
        prev_node.next, next_node.prev = next_node, prev_node

    def get(self, key):
        if key not in self.hashmap:
            return -1
        else:   
            self.remove_node(self.hashmap[key])
            self.add_to_mru(self.hashmap[key])
            return self.hashmap[key].val

    def put(self, key, value):
        # If the key already exists
        if key in self.hashmap:
            self.remove_node(self.hashmap[key])
        
        self.hashmap[key] = Node(key, val = value)
        self.add_to_mru(self.hashmap[key])
        
        if len(self.hashmap) > self.capacity:
            lru_node = self.LRU.next
            self.remove_node(self.LRU.next)
            del self.hashmap[lru_node.key]





        



