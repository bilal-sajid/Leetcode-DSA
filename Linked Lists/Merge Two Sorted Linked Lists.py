"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted linked list and return the head of the new sorted linked list.
The new list should be made up of nodes from list1 and list2.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,5]
Output: [1,1,2,3,4,5]
"""

"""
Considerations:
    - The possible length/size of each linked list? 0 <= The length of the each list <= 100
    - The values that each node can have? -100 <= Node.val <= 100


Idea 1 (Push onto array, sort and create new Linked List) - Not viable since it creates NEW nodes:
    1) Iterate over each linked list and add value to a dynamic array
    2) Sort the array
    3) Create new linked List

    Time Complexity: O((m+n)log(m+n)) - This is due to sorting step, where m represents number of nodes in list 1, and n represents nodes in list 2
    Space Complexity: O(m+n) - Space taken by the array and new created linked list

Idea 2 (Take advantage of sorted lists):
    - Have pointers at each linked list (These are already the heads of each linked list), compare the 2 values and choose the node with the smaller value of the two
    - Then move the pointer forward based on the linked list from where we chose the node
    
    Example:
        list_1 = 4 -> 5 -> 6, list_2 = 1 -> 3 -> 10
                 p1                    p2
    
    - Since we always choose the smaller value, we create a new list in sorted order

    Important Point:
        - The length of the linked lists may not be equal, so we can go up until the smaller list is finished
        - Then append the rest of the remaining linked list
    
    Creating new Linked List:
        - Create sentinal head and make a tail pointer that points to it
        - Whenever node is added, reference the tail and move it forward by doing tail.next

    Time Complexity: O(m+n), where m represents nodes in list1, and n represents nodes in list 2
    Space Complexity: O(1), Using the nodes in list1 and list 2 - Not creating own nodes
"""

class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next

def solution(list1, list2):
    sentinal_head = ListNode(-200, None)
    tail = sentinal_head

    while list1 and list2:
        if list1.val <= list2.val:
            # Add List 1 node to new linked list
            tail.next = list1
            list1 = list1.next
        else:
            # Add list 2 node to new linked list
            tail.next = list2
            list2 = list2.next
        
        tail = tail.next
    
    # Exhaust Remaining Linked List
    if list1:
        tail.next = list1
    else:
        tail.next = list2
    
    return sentinal_head.next