"""
Design a stack class that supports the push, pop, top, and getMin operations.

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.

Each function should run in O(1) time.

"""

"""
Input:
- None
- val: int
- None
- None
- None

Output:
- None (Initialization)
- None
- None
- int
- int

Considerations:
    - Values that val can take: -2^31 <= val <= 2^31 - 1
    - Can we do pop() or top() on an empty stack: pop, top and getMin will always be called on non-empty stacks.

Idea:
    - If we use a simple stack data structure, we can perform all operations in O(1) EXCEPT getMin(), which requires O(n)

    - Can create another stack that increases/decreases in size along with the main stack
        - At it's top, it would have the minimum value seen up until that point
        - Then every time a val is popped, we pop from the other stack as well
    
    Example:
    main_stack =  [6,7,5,3,4]
    other_stack = [6,6,5,3,3]

    This way, at every point, we know the minimum value we have seen till then

    Time complexity: O(1) for each function
    Space Complexity: O(2n) => O(n)

"""

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self, val):
        self.stack.append(val)

        if not self.min_stack:
            self.min_stack.append(val)
        else:
            min_value = min(val, self.min_stack[-1])
            self.min_stack.append(min_value)

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]
    


