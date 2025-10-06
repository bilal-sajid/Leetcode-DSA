"""
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.
"""

"""
Input:
    - nums: List[int]
    - k: int

Output:
    List[int]

Considerations:
    - Length of nums: 1 <= nums.length <= 10^4
    - Values that nums[i] can take: -1000 <= nums[i] <= 1000
    - Can k ever be > unique valuesin nums: 1 <= k <= number of distinct elements in nums

Idea 1 (Dictionary):
    - Count frequencies of each number in a hashmap - O(n)
    - Sort the hashmap - O(nlogn)
    - Create array that has the k most frequent values

    Time Complexity: O(nlogn), sorting hashmap takes most time
    Space Complexity: O(n), each element is distinct

Idea 2 (Heap):
    - Create a minheap that would store the dictionary of { number: frequency } pairs
    - Whenever the size of the minheap grows > k, pop from the heap

    Time Complexity: O(nlogk)
    Space Complexity: O(n + k), for the hashmap and the heap

Idea 3 (Bucket Sort Variation):
    - Create an array of size == len of nums
    - Count frequencies using hashmap -> add the frequencies 
    - This is because the MOST times a number can repeat == length of nums i.e all numbers are the same

    - The indices of the array represent the frequencies and the elements would be List[int]
    - Iterate backwards to get the k most frequent elements

    Iterating would be O(n) -> Since we would MAX iterate over all the elements just ONCE

    Time Complexity: O(n), iterating over each element
    Space Complexity: O(n), for hashmap
"""
from collections import defaultdict

def solution(nums, k):
    number_freq = defaultdict(int)

    for num in nums:
        number_freq[num] += 1
    
    freq_numbers = [[] for i in range(len(nums) + 1)] 

    for number, frequency in number_freq.items():
        freq_numbers[frequency].append(number)
    
    ans = []
    for element in freq_numbers[::-1]:
        for value in element:
            ans.append(value)
            if len(ans) == k:
                return ans

import heapq
def solution2(nums, k):
    number_freq = defaultdict(int)
    for num in nums:
        number_freq[num] += 1
    
    minheap = []
    for number, frequency in number_freq.items():
        heapq.heappush(minheap, [frequency, number])
        if len(minheap) > k:
            heapq.heappop(minheap)
    
    return [num for freq, num in minheap]


nums = [1,2,2,3,3,3]
k = 2

print(solution2(nums, k))
