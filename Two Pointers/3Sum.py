"""
Do this AGAIN!!
"""

"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, 
and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.
"""

"""
Input:
    - nums: List[int]
Output:
    - List[List[int,int,int]]

Considerations:
    - Length of nums: 3 <= nums.length <= 1000
    - Values that nums[i] can take: -10^5 <= nums[i] <= 10^5

Idea 1 (Nested Loops):
    - Have triple nested loops where each loop represents a certain index - i,j and k
    - Make sure that they arent the same at any point

    Time Complexity: O(n^3)
    Space Complexity: O(1)

Idea 2 (Sorting):
    - Instead of having to find 3 values, first focus on finding 2
    - Can sort and use same logic as used in 'Two Sum where input array is sorted'
        - Idea is that we intialise ptrs and move them based on if they are > or < than the target
    
    - The first value can be the appropriate index and the rest of the array can be considered to find the other 2

    Important:
        1) There could be multiple of the same values within our loop, so when we find an answer, we need to move the left ptr forward till the value is different
            - This prevents finding duplicate triplets
        2) For the first value, we dont want the same ones, so need to move that forward as well till its different from the previous one
    
    Time Complexity: O(nlogn) for sorting, O(n^2)
    Space Complexity: O(1)
"""
left, right = 1, 9
# nums = [-4,-4,2,2,2,2,2,2,2,2,5,6]
# [-4,2,2]

# -4 + 2= -2
def solution(nums):
    nums.sort()
    ans = []

    i = 0
    while i < len(nums):
        while nums[i] == nums[i-1] and i != 0:
            i += 1
        
        a = nums[i]

        left, right = i+1, len(nums) - 1
        while left < right:
            b, c = nums[left], nums[right]
            
            if b + c > a:
                right = right - 1
            elif b + c < a:
                left = left + 1
            else:
                ans.append([a,b,c])
                left, right = left + 1, right - 1

                while nums[left] == nums[left - 1] and left < right:
                    left += 1
        
        a = left

    return ans

nums = [-4,-4,2,2,2,2,2,2,2,2,5,6]
print(solution(nums))

            