"""
Given an unsorted array of integers nums and an integer k, return the kth largest element in the array.

By kth largest element, we mean the kth largest element in the sorted order, not the kth distinct element.

Follow-up: Can you solve it without sorting?

"""

"""
Input:
    - nums: List[int]
    - k: int
Output:
    - int

Considerations:
    - Length of nums, k: 1 <= k <= nums.length <= 10000
    - Values of nums[i]: -1000 <= nums[i] <= 1000

Note:
    - k cannot be larger than the size of nums, therefore it is always valid (No need to check)

Idea 1 (Sorting):
    - Sort nums and the index using the k value

    Time Complexity: O(nlogn)
    Space Complexity: O(1) or O(n) depending on sort method

Idea 2 (Min Heap): - Best Case
    - Iterate over nums 1-by-1 and add them to a min heap
    - Whenever the size of the heap grows beyond k, remove from the heap
    - Since min heap prioritizes the 'smallest' element, that will be removed

    - In the end, we will have the minheap containing the k largest values

    Time Complexity: O(nlogk)
    Space Complexity: O(k)

Idea 3 (Heapify):
    - Heapify nums and keep popping from the minheap until there are k values left

    Time Complexity: O(nlog(n-k))
    Space Complexity: O(n)
"""

import heapq
def solution(nums, k):
    minheap = []
    
    for num in nums:
        heapq.heappush(minheap, num)
        if len(minheap) > k:
            heapq.heappop(minheap)
    
    return minheap[0]

nums = [1,7,6,9,8]
k=5
print(solution(nums,k))