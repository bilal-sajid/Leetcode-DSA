"""
You are given an array of integers nums and an integer k. 
There is a sliding window of size k that starts at the left edge of the array. 
The window slides one position to the right until it reaches the right edge of the array.

Return a list that contains the maximum element in the window at each step.
"""

"""
Input:
    - nums: int
    - k: int

Output:
    List[int]

Considerations:
    - Length of nums: 1 <= nums.length <= 1000
    - Possible range of values that nums[i] can take: -10,000 <= nums[i] <= 10,000
    - Values that k can take: 1 <= k <= nums.length

Idea 1 (Fixed Sliding Window):
    - Create windows of size k and find the max in that subarray

    Time Complexity: O(n * k), O(n) formaking the windows, and for each window we are finding max which needs to go over all the elements in that particular window
    Space Complexity: O(1), not inclusing output list

Idea 2 (Queue):
    - Add the elements to a queue and once they are out of the window we need to remove them

    - We are only concerned with the biggest value, therefore we can have a monotonically non-decreasing stack
        - This way, the largest number that we have seen will be at position 0 in the queue
    
    - Also need to remove from the queue once it is no longer in the window
        - Can store indices rather than the numbers so we can continuously check
    
    Time Complexity: O(n)
    Space Complexity: O(k)
"""

from collections import deque

def solution(nums, k):
    queue = deque() 
    ans = [] 

    for i in range(len(nums)):
        while queue and nums[i] > nums[queue[-1]]:
            queue.pop()

        queue.append(i)

        if i - k >= queue[0]:
            queue.popleft()
        
        if i >= k - 1:
            ans.append(nums[queue[0]])
    
    return ans 

nums = [1,2,1,0,4,2,6]
k = 3

print(solution(nums, k))
