"""
You are given the head of a linked list of length n. Unlike a singly linked list, each node contains an additional pointer random, which may point to any node in the list, or null.
Create a deep copy of the list.

The deep copy should consist of exactly n new nodes, each including:

The original value val of the copied node
A next pointer to the new node corresponding to the next pointer of the original node
A random pointer to the new node corresponding to the random pointer of the original node
Note: None of the pointers in the new list should point to nodes in the original list.

Return the head of the copied linked list.

In the examples, the linked list is represented as a list of n nodes. Each node is represented as a pair of [val, random_index] where random_index is the index of the node (0-indexed) that the random pointer points to, or null if it does not point to any node.

"""

"""
Input:
    - head: Linked List
Output:
    - head: Linked List

Considerations:
    - The length of the linked list:
    - Values that each node can take:

Idea (2 Pass):
    Main problem is that the random pointer can be pointing to a node that is NOT YET created

    First Pass:
        - Create a hashmap that maps the original node to a NEW copy node
        - copy_node = Node(values, ptrs of the original node)
    
    Second Pass:
        - Build up the new linked list
    
    We need a way to reference the new nodes, so we can keep track using the hashmap
        - {old_node_1: copy_node_1, old_node_2: copy_node_2 ...}
    
    Time Complexity: O(n + n) => O(n), where n is the number of nodes in the linked list
    Space Complexity: O(n) - For the hashmap

"""

class Node:
    def __init__(self, val, next = None, random = None):
        self.val = val
        self.next = next
        self.random = random
    

def solution(head):
    hash_map = {None: None}

    curr = head
    while curr:
        copy_node = Node(curr.val)
        hash_map[curr] = copy_node
        curr = curr.next
    
    curr = head
    while curr:
        copy_node = hash_map[curr]
        copy_node.next = hash_map[curr.next]
        copy_node.random = hash_map[curr.random]
        curr = curr.next
    
    return hash_map[head]
