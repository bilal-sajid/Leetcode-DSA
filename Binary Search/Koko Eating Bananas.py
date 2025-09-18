"""
You are given an integer array piles where piles[i] is the number of bananas in the ith pile. You are also given an integer h, which represents the number of hours you have to eat all the bananas.

You may decide your bananas-per-hour eating rate of k. Each hour, you may choose a pile of bananas and eats k bananas from that pile. 
If the pile has less than k bananas, you may finish eating the pile but you can not eat from another pile in the same hour.

Return the minimum integer k such that you can eat all the bananas within h hours.

"""

"""
Input:
    - piles: List[int]
    - h: int

Output:
    - k (Banana Eating Speed)

Considerations:
    - Range of values that piles[i] can take: piles.length <= h <= 1,000,000
    - Length of piles: 1 <= piles.length <= 1,000
    - Range of values of h:piles.length <= h <= 1,000,000
    - Will a viable solution ALWAYS exist (Think of case where len(piles) > h):

Idea (Binary Search - Solution Space):
    - There is a point at which the eating speed k allows all the bananas to be eaten in h hours
        - Example: if speed is 2 it cannot finish, but at speed 3 it can
            - Meaning that at speeds lower than 2, it STILL wont be able to finish and at speeds greater than 3 it WOULD be
    
    - We want to find that threshold
    - To find bananas eaten per hour: piles[i]/speed

    Step 1
        - Set high and low boundaries
        - low = 1, since eating speed must be > 0 (otherwise no bananas eaten per pile)
        - high = max(piles), eating speed greater doesn;t effect since each pile would take AT LEAST 1 hour
    
    Step 2
        - Binary search where the 'mid' value represents the eating speed
    
    Step 3
        - Helper function that checks if its possible/not possible to eat all the piles within h

        If possible:
            - There potentially exists a SMALLER value of k so reduce search range (right = mid-1)
        If impossible:
            - There should exist a LARGER value of k so increase search range (left = mid+1)
    
    Time Complexity: O(nlogk), where n is the length of piles and k is the search space
    Space Complexity: O(1)
"""

import math

def solution(piles, h):

    def canFinishPiles(speed):
        hours_taken = 0
        for pile in piles:
            hours_taken += math.ceil(pile / speed)
        return hours_taken <= h

    left, right = 1, max(piles)
    while left <= right:
        mid = (left + right) // 2

        if canFinishPiles(mid):
            right = mid - 1
        else:
            left = mid + 1
    
    return left

piles = [10,20,30]
h = 6
print(solution(piles, h))
