"""
You are given an array of integers nums containing n + 1 integers. Each integer in nums is in the range [1, n] inclusive.
Every integer appears exactly once, except for one integer which appears two or more times. Return the integer that appears more than once.

Example 1:
Input: nums = [1,2,3,2,2]
Output: 2

Example 2:
Input: nums = [1,2,3,4,4]
Output: 4

"""

"""
Input:
    - nums: List[int]
Output:
    - int

Considerations:
    - Length of nums: nums.length == n + 1
    - Values of nums: 1 <= nums[i] <= n
    - Values of n: 1 <= n <= 10000

Idea 1 (Set):
    - Iterate over each of the values in nums and add them to a set
    - If we reach a value that is already in the set, then it appeared multiple times

    Time Complexity: O(1)
    Space Complexity: O(n)

Idea 2 (Floyd's Tortoise and Hare Algorithm):
    - For a 0 indexed array, the first index starts from 0 and will go on till n
    Example: [1,2,3,4,5], indices would be 0,1,2,3,4

    - We can structure this as a linked list probloem, where we want to find a cycle in the linked list
    - The cycle is determined by using the indices i.e the value of the current array index indicates the next index position to go to

    Example: [1,2,3,4,1], n = 4
        - index 0 -> index 1 -> index 2 -> index 3 -> index 4 -> index 1
    
    We are guaranteed to find a cycle in the linked list, we jsut need to figure out where it starts

    Step 1 (Slow and Fast Pointer):
        - Move fast at twice the speed until the two 'ptrs' meets
        - The idea is to move toi the next index position using the value of the current one
    
    Step 2 (Two Slow Pointers):
        - The distance between the start of the linked list and the point where the slow and fast pointers met would be equal
        - Move the two ptrs by one until they meet each other
        - Wherever they meet is the value which occurred multiple times
    
    Important: 
        - We can use the value at index 0 as the start of the linked list (and asssume its not part of the cycle) is because the range would be [0,n] inclusive
        - So theres no way that anything would point back the the 0-th index

    Time Complexity: O(1)
    Space Complexity: O(1)
"""

def solution(nums):
    slow = fast = nums[0]

    while True:
        slow = slow[nums]
        fast = fast[fast[nums]]
        # Both the indices are the same
        if slow == fast:
            break
    
    slow2 = nums[0]
    while slow != slow2:
        slow = slow[nums]
        slow2 = slow2[nums]
    
    return slow[nums]
    


