"""
You are given an array of non-negative integers height which represent an elevation map. 
Each value height[i] represents the height of a bar, which has a width of 1.

Return the maximum area of water that can be trapped between the bars.
"""

"""
Input:
    - height: int

Output:
    - int

Considerations:
    - Length of height: 1 <= height.length <= 1000
    - Values that height can take: 0 <= height[i] <= 1000

Idea 1:
    - Need to know how much water can be trapped at each position
        - This is dependent on the bars to the right and left of it
    
    - The maximum amount of water that can be stored at a particular position would be the minimum of the largest heights to its left and right
        - Example: height = [2,0,10], at position 1, it can store 2 units of water
    
    - Can have two lists that store these values for each position
        - left_largest, right_largest

        - Then it is a manner of just taking the minimum of the two
    
    - Also need to subtract the current height so it is not included

    Time Complexity: O(n)
    Space Complexity: O(n)
"""

def solution1(height):
    left_largest = []
    right_largest = [0] * len(height)

    left_largest_height = 0
    for h in height:
        left_largest.append(left_largest_height)
        left_largest_height = max(h, left_largest_height)
    
    right_largest_height = 0
    for i in range(len(height) - 1, -1 , -1):
        right_largest[i] = right_largest_height
        right_largest_height = max(height[i], right_largest_height)
    
    ans = 0
    for i in range(len(left_largest)):
        water_stored = min(left_largest[i], right_largest[i]) - height[i]
        if water_stored > 0:
            ans += water_stored
    
    return ans


height = [0,2,0,3,1,0,1,3,2,1]
print(solution1(height))