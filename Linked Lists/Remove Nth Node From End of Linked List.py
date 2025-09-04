"""
You are given the beginning of a linked list head, and an integer n.
Remove the nth node from the end of the list and return the beginning of the list.

Example 1:
Input: head = [1,2,3,4], n = 2
Output: [1,2,4]
"""

"""
Input:
    - head: Linked List / Node
    - n: int

Output:
    - Linked List (head/new head)

Considerations:
    - Possible size/length of the List: 1 <= sz <= 30
    - Values that n can take: 1 <= n <= sz
    - Values that each node can take: 0 <= Node.val <= 100

Important Notes:
    - There CAN be a case where there's one node and that is deleted (if n=1) so now the linked list is empty

Idea 1:
    - Iterate over the entire linked list and get the size/length of it
    - Iterate again to get up to the (size - n) node - This points to the previous node to the one that needs to be deleted
    - To delete we can simply do ptr.next.next

    Time Complexity: O(n + n) - Need to iterate over list twice
    Space Complexity: O(1)

Idea 2 (Slow and Fast Pointers):
    - Initially begin the two pointers together, and put the fast pointer n nodes ahead of the slow pointer
    - Move both forward by one node, until fast ptr reaches the end 
    - slow references the node to delete

    - We want a reference to the node BEFORE slow, so we can keep track of that using a prev ptr 
        OR
    - Can iterate until fast.next == None - Then slow would point one node before the one to delete

    - For the case where length of list is 1 and n=1, the prev node needs to be something, so we can create a 'sentinal head'
    - prev would just be a reference to the node behind the node to delete

    Time Complexity: O(n) - Single Pass
    Space Complexity: O(1)
"""

class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next

def solution(head, n):
    sentinal_head = ListNode(-1, head)
    slow = fast = sentinal_head
    
    # Step 1: Move fast n steps ahead of slow
    for _ in range(n):
        fast = fast.next
    
    # Step 2: Move pointers forward by one 
    while fast.next:
        slow = slow.next
        fast = fast.next
    
    # Step 3: Delete the Node
    slow.next = slow.next.next
    
    return sentinal_head.next
