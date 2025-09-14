"""
You are given an array of integers heights where heights[i] represents the height of a bar. The width of each bar is 1.

Return the area of the largest rectangle that can be formed among the bars.

Note: This chart is known as a histogram.

"""

"""
Input:
    - heights: List[int]

Output:
    - max_area: int

Considerations:
    - Length of heights: 1 <= heights.length <= 1000
    - Range of values that heights[i] can take: 0 <= heights[i] <= 1000

    
Intuition:
    - The width of each rectangle is 1, so each rectangle is making AT LEAST the height of height[i]

Idea:
    - Example 1: heights = [1,2,3]
        - 1: can continue to the right but NOT the left (Larger value to its right - Smaller value to its left)
        - 2: CANNOT cotinue to the left, but CAN CONTINUE to the right (Larger Value to its right - Smaller Value to its left)
        - 3: CANNOT continue left or right (Smaller values on both sides)
    
    - Example 2: heights = [1,2,3,2]
        - On the last 2, the area can go towards the left UP UNTIL the previous 2 (At the second position)
        - So the maximum area taken by a rectangle would be from 2 -> 2
        - The 3 stops increasing from the left and the right

    Step 1:
        - Iterate over each element in heights and put the this into a stack - (heights[i], index)
        - We need index since we need to use it for the width
    
    Step 2:
        - If we come across a heights[i] that is smaller than the previous heights[i-1], that means that
            - 1) heights[i-1] can no longer be extended to the right, therefore the max area that IT can make would be either its own height, OR be extended towards the left
        - Keep popping from the stack WHILE the heights values are LARGER than the current one
        - On each pop, we want to find the max area that this specific rectangle can make (extended to left)
        
        Example: heights: [1,2,3,3]
        - If a height can be extended towards the left, we need the index of the previous height and we want to set this new one
        - Can set this new one by putting in the new height
        - Above, we dont know if there is a 3, AFTER the last one, so when we come across the second one, set the index to 2, so next time if we come across a 3, we would find the MAX area
    
    Step 3:
        - Exhaust the stack until its empty by using the stack length and the current index as the width

    Time Complexity: O(n)
    Space Complexity: O(n)

"""
# heights = [1,1,2,2,3]

#         # h,i  
# stack = [(1,0), (2,2), (3,4)]

def solution(heights):
    stack = []
    max_area = 0

    for index in range(len(heights)):
        prev_index = index # 4

        # Can extend towards the left
        while stack and stack[-1][0] >= heights[index]:
            prev_h, prev_index = stack.pop() # 2,2
        
        max_area = max(max_area, heights[index] * ((index - prev_index) + 1)) # 3 * 1 = 3
        stack.append((heights[index], prev_index))
    
    for height, index in stack:
        max_area = max(max_area,height * (len(heights) - index)) # 2 * (5 - 2)
    
    return max_area
    
heights = [1,1,1,4,3]
print(solution(heights))