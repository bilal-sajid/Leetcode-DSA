"""
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
"""

"""
Input:
    - nums: List[int]
Output:
    - Boolean

Considerations:
    - Length of nums: N/A
    - Values that nums[i] can take: N/A

Idea 1:
    - Nested Loop, where one loops over the elements, and the other loops over all the other elements to see if there is a match

    Time Complexity: O(n^2)
    Space Complexity: O(1)

Idea 2 (Set):
    - Iterate over the nums, one-by-one and add them to a set
    - If we come across a number that is already in the set, we have seen it before so return True

    Time Complexity: O(n)
    Space Complexity: O(n)
"""

def solution(nums):
    num_set = set()

    for num in nums:
        if num in num_set:
            return True
        num_set.add(num)
    
    return False

nums = [1,2,3,4,5,1,7,8,9,10]
print(solution(nums))