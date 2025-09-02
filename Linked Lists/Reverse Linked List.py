"""
Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

Example 1:

Input: head = [0,1,2,3]
Output: [3,2,1,0]

Example 2:

Input: head = []
Output: []
"""

"""
Considerations:
- Possible Length/Size of the List? 0 <= The length of the list <= 1000
- What values can the linked list have? -1000 <= Node.val <= 1000

Note:
- We don't want to send back a copy of the list, but change the linked list IN-PLACE

Example:
0 -> 1 -> 2 -> 3 -----> 3 -> 2 -> 1 -> 0

Idea 1 (Push onto array) - (Not viable since we create a COPY of the list):
1) Go over each node in the linked list and add the values into a dynamic array
2) Reverse the array
3) Create a new Linked List based on those values

Time Complexity: O(n + n + n) -> O(n)
Space Complexity: O(n + n) -> O(n)


Idea 2 (Reverse in Place):
Important:
    - Each node is pointing to the one right before it

Main Issue(s):
    - If we make each ndoe point towards the previous one it would lose its .next reference
    - How to change the head

To maintain the next reference, store it before changing its value
We also need a previous node to reference - Can initialize to None
Then move each node/pointer 'forward' i.e to the next set of nodes

Time Complexity: O(n)
Space Complexity: O(1) - Reversed in-place
where n is the number of nodes in the linked list
"""

class LinkedList:
    def __init__(self, val, next):
        self.val = val
        self.next = next

def solution(head):
    prev = None

    while head:
        nextNode = head.next
        head.next = prev
        prev = head
        head = nextNode
    
    return prev

