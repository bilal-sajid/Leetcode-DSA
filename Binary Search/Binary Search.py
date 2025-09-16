"""
You are given an array of distinct integers nums, sorted in ascending order, and an integer target.

Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.

Your solution must run in O(logn) time.
"""

"""
Input:
    - nums: List[int] - Sorted(Ascending)
    - target: int

Output:
    - int

Considerations:
    - Length of nums: 1 <= nums.length <= 10000.
    - Values that nums[i], target can take: -10000 < nums[i], target < 10000
    - Distinct = unique integers? Yes

Idea 1 (Simple Search):
    - Go over the entire list and if we reach a number thats equal to target return its index
    - If we rech the end without finding target, return -1

    Time Complexity: O(n)
    Space Complexity: O(1)

Idea 2 (Binary Search):
    - Take advantage that the array is already SORTED
    - Initialize left and right pointers to the ends of the list, find midpoint, then move pointers accordingly

    Time Complexity: O(logn) - Reducing search space in half at each point
    Space Complexity: O(1)
"""



def solution(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (right + left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    
    return -1

nums = [10,20,21,33,46,50]
target = 22
print(solution(nums,target))