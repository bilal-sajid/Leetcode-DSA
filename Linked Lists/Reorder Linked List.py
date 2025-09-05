"""
You are given the head of a singly linked-list.

The positions of a linked list of length = 7 for example, can intially be represented as:
[0, 1, 2, 3, 4, 5, 6]

Reorder the nodes of the linked list to be in the following order:
[0, 6, 1, 5, 2, 4, 3]

Notice that in the general case for a list of length = n the nodes are reordered to be in the following order:
[0, n-1, 1, n-2, 2, n-3, ...]

You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.

Example 1:
Input: head = [2,4,6,8]
Output: [2,8,4,6]

Example 2:
Input: head = [2,4,6,8,10]
Output: [2,10,4,8,6]
"""

"""
Input: 
    - head: Linked List
Output:
    - head: Linked List

Considerations:
    - Size of Linked List: 1 <= Length of the list <= 1000
    - Values of Nodes: 1 <= Node.val <= 1000

Idea:
    - Main Idea: We are matching the first with the last, then second with second last and so on

    Step 1)
        - Find the Middle of the linked list and start reversing from there
        Even: 1 -> 2 -> 3 -> 4     =>      1 -> 2   4->3
        Odd: 1 -> 2 -> 3 -> 4 -> 5 =>    1 -> 2 -> 3  5->4
        - We would now have 2 separate linked lists
        - For odd cases one of the lists would be larger
    
    Step 2)
        - Create the new reordered list
        2 -> 4 -> 20 -> None     8 -> 6 -> None
             l1    l1nn                     l2.   l2nn

        - l1.next = l2
        Lost reference to original so we need to store l1_next_node
        - l2.next = l1_next_node
        Lost reference so we need to store l2_next_node
        - Set l2 to l2_next_node
        - Set l1 to l1_next_node

        As long as the first linked list is larger than the second linked list, we keep going UNTIL l2 is None
    
        Time Complexity: O(n), where n is the length of the linked list
        Space Complexity: O(1)
"""


def solution(head):
    # if not head or not head.next:
    #     return head

    # Find middle of linked list
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Reverse second half of Linked List
    prev, curr = None, slow.next
    slow.next = None # Sever connection of first half to second

    while curr:
        nextNode = curr.next
        curr.next = prev
        prev = curr
        curr = nextNode
    
    # Reorder the Linked List
    l1, l2 = head, prev

    while l2:
        l1_next_node, l2_next_node = l1.next, l2.next
        l1.next = l2
        l2.next = l1_next_node
        l1, l2 = l1_next_node, l2_next_node
