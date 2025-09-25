"""
You are given an 2-D array points where points[i] = [xi, yi] represents the coordinates of a point on an X-Y axis plane. 
You are also given an integer k.

Return the k closest points to the origin (0, 0).

The distance between two points is defined as the Euclidean distance (sqrt((x1 - x2)^2 + (y1 - y2)^2)).

You may return the answer in any order.

"""

"""
Input:
    - points: List[List[int]]
    - k: int

Output:
    - [List[List[int]]] => [[x1,y2],[x2,y2]..]

Idea 1:
    - Find the distances of all the points from the origin - Time Complexity: O(n)
    - Sort based on distance - O(nlogn)
    - Select the k closest points - O(k)

    Time Complexity: O(n) + O(nlogn) + O(k)
    Space Complexity: O(1) or O(n), depending on if we create a new array

Idea 2 (Max Heap):
    - As we caluclate the distance, we add the distances (along with the x,y points) into a max heap
    - Once the size of the heaop grows beyond k, we need to start popping from it

    - We are concerned with the K Closest elements therefore we want to remove the larger distances
        - Since max heap prioritizes larger values, those would be popped off first
    
    - At the end we would have the K closest points in our maxheap

    Time Complexity: O(nlogk)
    Space Complexity: O(logk)
""" 

import heapq
def solution(points, k):
    maxheap = []

    for x, y in points:
        distance = (((x)**2) + ((y)**2))**0.5
        heapq.heappush(maxheap, (-distance, (x, y))) # (-distance, (x1, y1))

        if len(maxheap) > k:
            heapq.heappop(maxheap)
    
    return [[items[1][0], items[1][1]]for items in maxheap]