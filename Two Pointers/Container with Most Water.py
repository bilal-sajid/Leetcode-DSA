"""
You are given an integer array heights where heights[i] represents the height of the ith bar.

You may choose any two bars to form a container. Return the maximum amount of water a container can store.
"""

"""
Input:
    - heights: List[int]

Output:
    - int

Considerations:
    - Length of heights: 2 <= height.length <= 1000
    - Values of heights: 0 <= height[i] <= 1000

Idea 1 (Nested Loop):
    - For each height position, find all the possible subarrays and find the amount of water that it can contain
        - Then select the maximum

    Time Complexity: O(n^2)
    Space Complexity: O(1)

Idea 2 (Two Pointers):
    - Have two ptrs that are initialized to the start and end of 'heights'

    - Calculate the amount of water:
        min(height[left], height[right]) * distance
    
    - Then whichever was the minimum height, move that ptr forward/backward since that is the limiting factor

    Time Complexity: O(n)
    Space Complexity: O(1)
"""


def solution(heights):
    left, right = 0, len(heights) - 1
    ans = 0

    while left < right:
        ans = max(ans, min(heights[left], heights[right]) * (right - left))

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    
    return ans

height = [2,2,2]
print(solution(height))