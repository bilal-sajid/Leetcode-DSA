"""
You are given two non-empty linked lists, l1 and l2, where each represents a non-negative integer.
The digits are stored in reverse order, e.g. the number 123 is represented as 3 -> 2 -> 1 -> in the linked list.

Each of the nodes contains a single digit. You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Return the sum of the two numbers as a linked list.

Example
Input: l1 = [1,2,3], l2 = [4,5,6]
Output: [5,7,9]

Explanation: 321 + 654 = 975.
"""

"""
Input:
    - l1, l2: Linked Lists

Output:
    - new_head: Linked List

Considerations:
    - Values of the nodes: 0 <= Node.val <= 9
    - Length of the linked lists: 1 <= l1.length, l2.length <= 100

Important Notes:
    - 923, in this question format would be 3->2->9
    - For normal addition we take the units, then tenths and so on ..
    - Since l1 and l2 are already in that format, we can just add the values at those positions

Idea:
    - Iterate over the lists and add the values of the nodes at the same positions
    
    - The added number can be single ofr double digit
        - Single Digit: Create a new node and put the val in that
        - Double Digit: Carry the 'tenth' position and the curr position would be th unit
    
    - Length of l1 and l2 may not necessarily be equal
        - Keep going until they're both exhausted. If one gets exhausted first, then give it the value of 0
    
    Even at the end there may be a carry left (i.e when we exhause BOTH lists), so we need to keeo going until that is exhausted as well

    - To create the new linked list, just create a sentinal head, make a tail pointer and whenever a new node is added, use the tail ptr to add and move onto the next

    Time Complexity: O(n)
    Space Complexity: O(1)

"""

class ListNode:
    def _init__(self, val, next = None):
        self.val = val
        self.next = next

def solution(l1, l2):
    sentinal_head = ListNode(10)
    tail = sentinal_head

    carry = 0

    while l1 or l2 or carry:
        first_value, second_value = 0, 0
        if l1:
            first_value = l1.val
        if l2:
            second_value = l2.next

        summed_value = first_value + second_value + carry
        unit, carry = summed_value % 10, summed_value // 10

        new_node = ListNode(unit)
        
        tail.next = new_node
        tail = tail.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    
    return sentinal_head.next
    

