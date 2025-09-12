"""
You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.
Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day. 
If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.

Example 1:
Input: temperatures = [30,38,30,36,35,40,28]
Output: [1,4,1,2,1,0,0]
"""


"""
Input:
    - temperatures: List[int]
Output:
    - result: List[int]

Considerations:
    - Length of temperatures: 1 <= temperatures.length <= 1000
    - Value of temperatures[i]: 1 <= temperatures[i] <= 100

Idea (2 For Loops):
    - For each day/temperature, we look for the next highest temperature
    - One loop to iterate over the daily temperatures
    - Another loop to find the next highest temperature

    - The difference in indices is the number of days before a warmer temperate appears

    Time Complexity: O(n^2)
    Space Complexity: O(1)

Idea ():
    - We are concerned with finding the 'next' warmer temperature
        - This is indicative of a monotonic data structure (Either stack or queue)
    
    Example: [40, 35, 38]
    - Until we find a temperature warmer than 35, there is NO WAY we can find a temperature warmer than 40 (Transitive property)

    For this case, we can use a MONOTONICALLY decreasing stack
    - We pop from the stack whenever we find a warmer temperature. Then push that temperature onto the stack
    - We care about indices because we want to find their difference, so we can push the indices instead of the actual temperatures

    Time Complexity: O(n)
    Space Complexity: O(n)
"""

def solution(temperatures):
    stack = []
    result = [0] * len(temperatures)

    for i in range(len(temperatures)):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            j = stack.pop()
            result[j] = i-j

        stack.append(i)
    
    return result


print(solution(temperatures = [30,38,30,36,35,40,28]))