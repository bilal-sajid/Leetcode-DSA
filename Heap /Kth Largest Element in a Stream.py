"""
Design a class to find the kth largest integer in a stream of values, including duplicates. 
E.g. the 2nd largest from [1, 2, 3, 3] is 3. The stream is not necessarily sorted.

Implement the following methods:

constructor(int k, int[] nums):
    - Initializes the object given an integer k and the stream of integers nums.
int add(int val): 
    - Adds the integer val to the stream and returns the kth largest integer in the stream.

"""

"""
Input:
    - k: int, nums: List[int]
    - val: int

Output:
    - None
    - Int

Considerations:
    - Range of values that nums[i] can take: -1000 <= nums[i] <= 1000
    - Length of nums: 0 <= nums.length <= 1000
    - Range of values that k can take: 1 <= k <= 1000
    - Can k > length of nums? There will always be at least k integers in the stream when you search for the kth integer.

Idea 1 (Sorting):
    Every time a new value comes in, sort the entire list then do indexing t find the K-th largest elemnt

    Time Complexity: O(nlogn), where n represents the numbers in our streams
    Space Complexity: O(n), if new array is used to store all the values

Idea 2 (Sort + Binary Search):
    - Sort the initial nums
    - Every time new value is added, perform binary search to find its insert position
    
    Time Complexity: O(nlogn), insertion would cost O(n)
    Space Complexity: O(n)

Idea 3 (Heap):
    - We are only concerned with the Top K Elements

    - Initialize a min heap which is of length k
    - Every time the length of the heap exceeds k we pop from it, thereby removing the smallest value
    - if we keep doing this, our heap wil contain the K largest integer values
    - At the end, we can just take the first index in the heap as the answer

    Time Complexity: O(nlogk), where n represents all values in stream - Each pop costs O(logn)
    Space Complexity: O(k), heap doesn't exceed k length
"""

import heapq

class KthLargest:
    def __init__(self, nums, k):
        self.k = k
        self.min_heap = nums
        heapq.heapify(self.min_heap)

        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

    def add(self, val):
        heapq.heappush(self.min_heap, val)

        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        
        return self.min_heap[0]

