"""
Given an array of integers numbers that is sorted in non-decreasing order.

Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. 
Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

There will always be exactly one valid solution.

Your solution must use O(1) additional space.
"""

"""
Input:
    - numbers: List[int] - Sorted -> Smallest to Largest
    - target: int

Output
    - List[int, int]

Considerations:
    - Length of numbers: 2 <= numbers.length <= 1000
    - Values that number[i] can take: -1000 <= numbers[i] <= 1000
    - Target values: -1000 <= numbers[i] <= 1000

Idea 1 (Nested Loop):
    - For each number, we loop over all the other numbers and see if their summations == target

    - If its equal to the target, return the indices

    Time Complexity: O(n^2)
    Space Complexity: O(1)

Idea 2 (Two Pointer):
    - Initialize two ptrs at the start and the end

    [-1,1,5,10,20], target = 25
      ^        ^

    If summation > target:
        - Move right ptr backward
    If summation < target:
        - Move left ptr forward
    
    Time Complexity: O(n)
    Space Complexity: O(1)
"""

def solution(numbers, target):
    left, right = 0, len(numbers) - 1

    while left < right:
        summation = numbers[left] + numbers[right]

        if summation == target:
            return [left + 1, right + 1]
        elif summation > target:
            right = right - 1
        else:
            left = left + 1
    
    return [None, None]

numbers = [-1,1,5,10,20]
target = 21

print(solution(numbers, target))


