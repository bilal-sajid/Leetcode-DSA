"""
Given the beginning of a linked list head, return true if there is a cycle in the linked list. Otherwise, return false.
There is a cycle in a linked list if at least one node in the list can be visited again by following the next pointer.

Internally, index determines the index of the beginning of the cycle, if it exists. The tail node of the list will set it's next pointer to the index-th node. If index = -1, then the tail node points to null and no cycle exists.

Note: index is not given to you as a parameter.
"""

"""
Considerations:
    - Length of Linked List: 1 <= Length of the list <= 1000
    - Values of linked List Nodes: -1000 <= Node.val <= 1000

Idea 1 (Hashmap/Set):
    - Iterate over each node, and add each of the nodes onto a set
    - If we reach a node that is already in our set, that means we have been to this node before, so there is a cycle
    - If we reach the end of the linked list without a node reappearing in the set, then there's no cycle

    Time Complexity: O(n), where n represents the size of linked list
    Space Complexity: O(n)

Idea 2 (Floyd's Tortoise and Hare Algorithm):
    - Main idea is if 2 people are running on a circular racetrack and one is running twice as fast as the other, they will eventually meet again
    
    Slow and Fast Pointers, where fast moves twice as fast as slow
    
    Two Possibilities:
        1) Fast pointer reaches the end of linked list (No cycle)
        2) Fast and slow overlap (Cycle)
    
    This works because at each point the 'distance' between the two pointers is decreasing by 1 each time

    Time Complexity: O(n), where n is the number of nodes in the linked list
    Space Complexity: O(1)
"""

def solution(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    
    return False


