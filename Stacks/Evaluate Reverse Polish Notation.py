"""
You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

Return the integer that represents the evaluation of the expression.

The operands may be integers or the results of other operations.
The operators include '+', '-', '*', and '/'.
Assume that division between integers always truncates toward zero.

Example:
Input: tokens = ["1","2","+","3","*","4","-"]
Output: 5
Explanation: ((1 + 2) * 3) - 4 = 5

"""

"""
Input:
    - tokens: List[string]
Output:
    - int

Considerations:
    - Length of tokens: 1 <= tokens.length <= 1000
    - Values of each element: tokens[i] is "+", "-", "*", or "/", or a string representing an integer in the range [-100, 100]

Idea 1:
    - Take the first and second elements and perform the operation on them
    - Delete the 3 elements at the start of the list and insert the new_value
    
    Problem: 
        - Adding to the start of the list is O(n)
        - So Time Complexity would be at least O(2^n)

Idea 2 (Stack):
    - Iterate over the elements and add them to the stack until an operator is reached
    - Perform calculation based on the operator and remove the old values
    - Add new value to stack

    Notes:
        - Convert the strings to integers
        - Pop from the stack because weno longer need the old values once a new one is calculated
        - Take care of special case where divisor or divident is negative

    Time Complexity: O(n)
    Space Complexity: O(n)
"""

# stack = [1,2]
# "1","2","+"
# 1+2
import math

def solution(tokens):
    stack = []
    operators = {"+" , "-" , "*" , "/"}

    for token in tokens:
        if token not in operators:
            stack.append(token)
        else:
            value2 = int(stack.pop())
            value1 = int(stack.pop())

            computed_val = 0
            if token == "+":
                computed_val = value1 + value2
            if token == "-":
                computed_val = value1 - value2
            if token == "*":
                computed_val = value1 * value2
            if token == "/":
                computed_val = value1 / value2
                # So that it always tends towards 0
                if computed_val > 0:
                    computed_val = math.floor(computed_val)
                else:
                    computed_val = math.ceil(computed_val)
            
            stack.append(str(computed_val))
    
    return int(stack[-1])

tokens1 = ["1","10","+","3","*","4","-"]
tokens2 = ["10","-3","/"]
print(solution(tokens2))





