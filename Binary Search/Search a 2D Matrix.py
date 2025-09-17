"""
You are given an m x n 2-D integer array matrix and an integer target.

Each row in matrix is sorted in non-decreasing order.
The first integer of every row is greater than the last integer of the previous row.
Return true if target exists within matrix or false otherwise.

Can you write a solution that runs in O(log(m * n)) time?
"""

"""
Input:
    - matrix: List[List[int]]
    - target: int
Output:
    - Boolean

Considerations:
    - Length of matrix, matrix[0]: 1 <= m, n <= 100
    - Range of values that target and matrix[i][j] can take: -10000 <= matrix[i][j], target <= 10000

Idea 1 (Simple Search):
    - Iterate over each row 1-by-1, and check all of their elements

    Time Complexity: O(m*n) - Need to go over all the elements
    Space Complexity: O(1)

Idea 2 (Binary Search):
    - Each row is sorted and is SMALLER than ALL the elements in the next row
        - Therefore there is a sorted property across rows as well
    - We can essentially 'flatten' the 2D matrix and consider it as a single, sorted array
    - Perform Binary search from the 2 ends

    - The mid value corresponds to which element we want to access
        - Need to convert it into (i,j) indices
            - row = 3 // n
            - col = 5 % m

    - Keep checking until the left pointer goes beyond right - we only need to check for existence

    Time Complexity: O(log(m*n))
    Space Complexity: O(1)
"""

def solution(matrix, target):
    m, n = len(matrix), len(matrix[0])
    left, right = 0, (m * n) - 1

    while left <= right:
        mid = (left + right) // 2
        row = mid // n
        col = mid % n

        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            right = mid -1
        elif matrix[row][col] < target:
            left = mid + 1
    
    return False

matrix = [[1]]
target = 1
print(solution(matrix, target))
        