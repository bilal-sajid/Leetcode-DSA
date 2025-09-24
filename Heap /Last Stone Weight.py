"""
You are given an array of integers stones where stones[i] represents the weight of the ith stone.

We want to run a simulation on the stones as follows:
    At each step we choose the two heaviest stones, with weight x and y and smash them togethers
    If x == y, both stones are destroyed
    If x < y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.

Continue the simulation until there is no more than one stone remaining.

Return the weight of the last remaining stone or return 0 if none remain.

"""

"""
Input:
    - stones: List[int]
Output:
    - int

Considerations:
    - Length of stones: 1 <= stones.length <= 20
    - Range of values that stones[i] can take: 1 <= stones[i] <= 100

Idea 1 (Sorting):
    - Sort 'stones' in descending order
    - Pick up the two heaviest stones at position 0 and 1
    - Insert the difference back into stones (Using Binary Search)

    Main probloem is that inserting into the array would cost O(n)

    Time Complexity: 
        - O(nlogn) - For Sorting
        - O(logn) - For Binary Search
        - O(n) - For Insertion



Idea (Max Heap):
    - At each point we want to get the two 'heaviest' stones, which we can get in O(logn) time if we use a maxheap
    - Converting into a maxheap would be in O(n) time

    - Take the two values and insert the difference back intot he heap (O(logn) for insertion)
    - Keep the simulation going until the length of the heap <= 1

    Time Complexity: O(nlogn)
    Space Complexity: O(n)
"""

import heapq

def solution(stones):
    maxheap = [-stone for stone in stones]
    heapq.heapify(maxheap)

    while len(maxheap) > 1:
        stone1, stone2 = -heapq.heappop(maxheap), -heapq.heappop(maxheap)
        # Note: stone1 >= stone2
        difference = stone1 - stone2
        if difference != 0:
            heapq.heappush(maxheap, -difference)
    
    return 0 if len(maxheap) == 0 else -maxheap[0]

stones = [2,1]
print(solution(stones))