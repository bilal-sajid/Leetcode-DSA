"""
The median is the middle value in a sorted list of integers. 
For lists of even length, there is no middle value, so the median is the mean of the two middle values.

For example:
    For arr = [1,2,3], the median is 2.
    For arr = [1,2], the median is (1 + 2) / 2 = 1.5

Implement the MedianFinder class:
    MedianFinder() initializes the MedianFinder object.
    void addNum(int num) adds the integer num from the data stream to the data structure.
    double findMedian() returns the median of all elements so far.
"""

"""
Input:
    - None
    - num: int
    - None

Output:
    - None
    - None
    - int/float

Considerations:
    - Can findMedian be called on an empty list: findMedian will only be called after adding at least one integer to the data structure.
    - Range of values that num can take: -100,000 <= num <= 100,000
    - Length of nums (Potential Size): N/A

Idea 1 (Sorting):
    - Each time an element is added, sort the entire thing
    - Then when findmedian() is called we just need to reference the middle value(s)
    
    Time Complexity: O(nlogn), each time a new num is added
    Space Complexity: O(n), if we use a list, where n is the total number of num values added to the stream

Idea 2 (Min and Max Heaps):
    - Visualise the num stream as 2 separate 'sectors'
    - The smaller sector is the max heap and the larger one is the min heap
        - This way, max heap[0] would hold the largest value in the smaller range and minheap[0] would hold the smallest in the alrger range
    
    - Need to maintain all the smaller numbers in the maxheap to maintain the proerty

    Step 1:
        - Add num to max heap
    Step 2:
        - Remove from the maxheap and put into minheap
    Step 3:
        - If the length of minheap > length of maxheap, pop from minheap and add back to minheap
    
    For even length:
        - Take the two values at minheap[0] and maxheap[0]
    For odd length:
        - maxheap[0] would be the median
    
    Time Complexity: O(logn)
    Space Complexity: O(n), for the heaps
"""

import heapq

class MedianFinder:

    def __init__(self):
        self.maxheap = []
        self.minheap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxheap, -num)
        heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))

        if len(self.minheap) > len(self.maxheap):
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))
        

    def findMedian(self) -> float:
        if len(self.minheap) == len(self.maxheap):
            return ((-self.maxheap[0]) + self.minheap[0]) / 2
        
        return -self.maxheap[0]

medianfinder = MedianFinder()
medianfinder.addNum(10)
print(medianfinder.findMedian())
medianfinder.addNum(20)
print(medianfinder.findMedian())