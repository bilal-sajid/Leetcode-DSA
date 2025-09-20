"""
You are given an array of length n which was originally sorted in ascending order. 
It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.
Given the rotated sorted array nums and an integer target, return the index of target within nums, or -1 if it is not present.

You may assume all elements in the sorted rotated array nums are unique,

A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?
"""

"""
Input:
    - arr: List[int] - Initially sorted, now rotated between 1 and n times - Unique elements
    - target: int

Output:
    - int (index of target or -1)

Considerations:
    - Length of array: 1 <= nums.length <= 1000
    - Range of values that target, arr[i] can take: -1000 <= nums[i], target <= 1000

Idea 1 (Simple Search):
    - Go over each element and compare with target

    Time Complexity: O(n)
    Space Complexity: O(1)

[1,2,3,4,5,6]

[6,1,2,3,4,5], n=1
l.     c   r
[5,6,1,2,3,4], n=2
[4,5,6,1,2,3], n=3

L.   c
[3,4,5,6,1,2], n=4
[2,3,4,5,6,1], n=5
[1,2,3,4,5,6], n=6

Idea 2 (Binary Search):
    - The hint that suggests binary search is that the array was initially SORTED

    - We are limited to 1-n rotations, therefore we can divide the array into 2 Sections
        - Left section: All values are > Right Section
        - Right Section: All values are < Left Section
        Example: [4,5,6,1,2,3], n=3 - All values in left section are greater than right section
        - In each section the values are in increasing order
        Important: EXCEPT when rotations=n and the elements are all sorted
    
    - Step 1 - Figure out what section we are currently in
        - If the current value >= left value: We are in the left section
        - If the current value < left value: We are in the right section
    
    - Step 2:
        - If we are in the Left Section:
            - The target is smaller:
                - If the target is smaller than the left most element then go towards right
                - If the target is >= the left most element then go towards left

            - The target is larger:
                - Go towards the right: left = mid + 1

        - If we are in the Right Section:
            - The target is smaller:
                - Go towards the left: right = mid - 1
                
            - The target is larger:
                - If the target is >= the left most element then go towards left
                - If the target is smaller than the left most element then we go towards right
    
    Time Complexity: O(logn)
    Space Complexity: O(1) 
"""

# [1,2,3,4,5,6]

# [6,1,2,3,4,5], n=1

# l.     c   r
# [5,6,1,2,3,4], n=2

# [4,5,6,1,2,3], n=3

# L.   c
# [3,4,5,6,1,2], n=4

# [2,3,4,5,6,1], n=5
# [1,2,3,4,5,6], n=6

def solution(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        
        if nums[mid] >= nums[0]: # Left Section - nums[0] or nums[left]
            # Go towards right
            if target > nums[mid] or target < nums[0]:
                left = mid + 1
            else:
                right = mid - 1
        
        else: # Right Section
            # Go towards left
            if target < nums[mid] or target >= nums[0]:
                right = mid - 1
            else:
                left = mid + 1

    return -1

nums = [4,5,6,1,2,3]
target = 5

print(solution(nums, target))
            


