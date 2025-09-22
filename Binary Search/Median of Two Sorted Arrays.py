"""
You are given two integer arrays nums1 and nums2 of size m and n respectively, where each is sorted in ascending order. 
Return the median value among all elements of the two arrays.

Your solution must run in O(log(m+n)) time.
"""

"""
Input:
    - num1, num2: List[int] - Each in ascending order
Output:
    - int/float

Considerations:
    - Length of nums1 and nums2: 0 <= m, n <= 1000
    - Rang of values that nums1[i] and nums2[i] can take: -10^6 <= nums1[i], nums2[i] <= 10^6

Idea 1:
    - Add all the values in both the arrays into a singly array
    - Sort the array
    - Get the middle value

    Time Complexity: O((n+m)log(n+m)) - Sorting the new array with the elements from both arrays
    Space Complexity: O(n+m) - The new array would be the length of both nums1 and nums2 combined

Idea 2 (Binary Search):

"""