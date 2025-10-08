"""
You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

Each row must contain the digits 1-9 without duplicates.
Each column must contain the digits 1-9 without duplicates.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.

Return true if the Sudoku board is valid, otherwise return false

Note: A board does not need to be full or be solvable to be valid.
"""

"""
Input:
    - board: List[List[string]] - Size = 9x9
Output:
    - Boolean

Considerations:
    - Length of board, board[i]: 9
    - Values that board[row][col] can take: 1-9 OR '.'

Idea (Multiple Sets):
    - We need to make sure there are NO DUPLICATES, which indicates the use of set(s)

    - Rows:
        - Whenever iterating across a row, use a set to make sure that there are no duplicates

    - Columns:
        - Whenever we move from one column to another, we need a set
    
    - Important: We need to know the digits that have already been mapped that that particular row/column
        - Mapping indicates the use of a hashmap
            - {row_number:set(5,4,1..)}
            - {col_number:set(5,4,1..)}
        - So the hashmap grows to a size of 9 keys (Indicating the row and column numbers)
    
    - Sub-Boxes:
        - Using the same logic as above, we need to map the digits to their specific 'sub-box'
            - {subbox_number: set(1,2,3..)}
        
        - Mapping [row][col] to subbox
            - The key can be the specific subbox
                - Calculate using - row//3, col//3 -> store as tuple
            - {(row//3, col//3): set(1,2,3..)}
    
    Time Complexity: O(n^2)
    Space Complexity: O(n^2)

"""

from collections import defaultdict

def solution(board):
    row_map = defaultdict(set)
    col_map = defaultdict(set)
    subbox_map = defaultdict(set)

    for row in range(len(board)):
        for col in range(len(board[0])):
            value = board[row][col]
            subbox_identifier = (row//3, col//3)
    
            if value in row_map[row] or value in col_map[col] or value in subbox_map[subbox_identifier]:
                return False
            
            if value != ".":
                row_map[row].add(value)
                col_map[col].add(value)
                subbox_map[subbox_identifier].add(value)
    
    return True

board = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

print(solution(board))