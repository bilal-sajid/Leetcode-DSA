"""
You are given an array of length n which was originally sorted in ascending order. 
It has now been rotated between 1 and n times. For example, the array nums = [1,2,3,4,5,6] might become:

[3,4,5,6,1,2] if it was rotated 4 times.
[1,2,3,4,5,6] if it was rotated 6 times.

Notice that rotating the array 4 times moves the last four elements of the array to the beginning. 
Rotating the array 6 times produces the original array.

Assuming all elements in the rotated sorted array nums are unique, return the minimum element of this array.

A solution that runs in O(n) time is trivial, can you write an algorithm that runs in O(log n) time?

"""

"""
Input:
    - arr: List[int] - Unique - Was initially sorted
Output:
    - int

Considerations:
    - Range of values that n can take: 1 <= nums.length <= 1000
    - Elements data type: integer
    - Valeus that nums[i] can take: -1000 <= nums[i] <= 1000

Note:
    - Rotating the array n times puts it back into sorted order

Idea 1 (Simple Search):
    - Linearly scan each element in the list and keep track fo the smallest one
    
    Time Complexity: O(n)
    Space Complexity: O(1)

    
[1,2,3,4,5,6]

[1,2,3,4,5,6], n=6
   
l.         r

[6,1,2,3,4,5], n=1
[5,6,1,2,3,4]
[4,5,6,1,2,3], n=3

     l     r
[3,4,5,6,1,2]
[2,3,4,5,6,1]


Idea 2 (Binary Search):
    - For the rotated array, we can divide it into 2 distinct portions: Left Portion and Right Portion
        - The Left portion contains the bigger elements
        - The Right portion contains the smaller elements
        Example: [4,5,6,1,2,3], rotations=3 - The Left portion contains all elements larger than  the Right portion
    
    - The larger portion will always be to the left of the smaller one (Except in the case of rotations = n)

    - For binary search, we first need to figure out if we are in the left or the right portion
        - Check the current element with the left-most element
            - if its smaller then we are in the right portion
            - if its larger, then we are in the left portion
    
    - Performing Binary Search
        - Step 1:
            - Already sorted, return array[0] - Check if nums[0] < nums[-1] then already sorted
        
        - Step 2:
            - Find out what portion we are in
                - If current value > left: In left portion
                - If current value < left: In right portion
        
        - Step 3:
            - If we are in right portion:
                - Smaller value can exist to the left side of it
                - right = mid - 1

            - If we are in left portion:
                - Smaller value would be on the right side of it
    
    - Time Complexity: O(logn)
    - Space Complexity: O(1)

"""

def solution(nums):
    left, right = 0, len(nums) - 1
    ans = float("inf")

    if nums[0] < nums[-1]:
        return nums[0]
    
    while left <= right:
        mid = (left + right) // 2
        ans = min(ans,nums[mid])

        if nums[mid] < nums[0]:  # In Right-Portion
            right = mid - 1
        else:  # In Left-Portion
            left = mid + 1
    
    return ans


# nums1 = [1,2,3,4,5,6]
# print(solution(nums1))

# nums2 = [4,5,6,1,2,3]
# print(solution(nums2))

# nums3 = [2,3,4,5,6,1]
# print(solution(nums3))

nums4 = [6,1,2,3,4,5]
print(solution(nums4))