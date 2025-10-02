"""
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.
"""

"""
Input:
    - nums: int
    - target: int

Output:
    - i, j: int, int (Indices)

Considerations:
    - Length of nums: 2 <= nums.length <= 1000
    - Values that nums[i] can take: -10,000,000 <= nums[i] <= 10,000,000
    - Values that target can take: -10,000,000 <= target <= 10,000,000

Idea 1 (Nested Loop):
    - Compare each element at an index with every other element at other indices
        - Add the 2 values together and see if they sum up to target
    
    Time Complexity: O(n^2), for the nested loop
    Space Complexity: O(1)

Idea 2 (Hashmap):
    - Whenever we reach a new element, for that to be an answer, we must have seen the 'target - ans' before it
        Example: target = 7 - If we come across a 3, then for that to be part of the answer, we must have seen a 4 before
    
    - Can store a dictionary with { element:index } pairs
    - Can check for the complement in O(1) time

    Time Complexity: O(n)
    Space Complexity: O(n)
"""

def solution(nums, target):
    hashmap = {}

    for i in range(len(nums)):
        complement = target - nums[i]

        if complement in hashmap:
            return [hashmap[complement], i]
    
        hashmap[nums[i]] = i

nums = [1,2,3,4,5,6,7,8,9,10]
target = 10
print(solution(nums, target))