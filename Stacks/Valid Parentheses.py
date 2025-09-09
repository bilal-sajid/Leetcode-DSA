"""
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:
    Every open bracket is closed by the same type of close bracket.
    Open brackets are closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

Return true if s is a valid string, and false otherwise.
"""

"""
Input:
    - s: string (Limited characters)
Output:
    - Boolean

Idea:
    - Need a mapping of every open and close bracket in order to determine if a current character is open/close
        - Hashmap where we map {open_bracket: close_bracket}
    
    - The most recent bracket needs to be closed first, then the second and so on, in order for it to be closed in the correct order
        - Example: ({()}) - The inner ( must be closed first
        - This shows a LIFO pattern which indicates use of a Stack Data Structure
    
    Main Steps:
        - Continue adding opening brackets to a stack
        - When we comes across a closing bracket, check if it corresponds to the most recent opening bracket
        - If it corresponds then pop the opening bracket since it founds it corresponding closing bracket

        - At the end the stack needs to be empty, showing that the opening brackets are all closed
        - Special Case:
            - If a closing bracket is reached when there are no opening brackets in the stack, that is also not valid
    
    Time Complexity: O(n), where n is the length of s - Going over each character once
    Space Complexity: O(n) - For the Stack
"""

def solution(s):
    stack = []
    bracket_mapping = {'(':')', '{':'}', '[':']'}

    for bracket in s:
        if bracket in bracket_mapping:
            stack.append(bracket)
        else:
            if not stack or bracket_mapping[stack[-1]] != bracket:
                return False
            else:
                stack.pop()
    
    return (len(stack) == 0)

s = "()[][][]"
print(solution(s))