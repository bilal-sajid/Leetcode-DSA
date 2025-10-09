"""
Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element. 
The elements do not have to be consecutive in the original array.

You must write an algorithm that runs in O(n) time.
"""

"""
Input:
    - nums: List[int]
Output:
    - int

Considerations:
    - Length of nums: 0 <= nums.length <= 1000
    - Values that nums[i] can take: -10^9 <= nums[i] <= 10^9

Idea 1 (Set):
    - We dont care about multiple occurrances of a value, ONLY that it exists
        - Convert nums into a set
    
    - Traverse the set and if we reach a value where 'value+1' exists in the set then we can continue down that path
    Example: set(3,4)
        - We see that for 3, '3+1' exists so we then go to 4, and see that '4+1' doesnt exist so the length is 2
        - We do the same thing for 4

    Example 2: set(1,2,3,4,5)
        - In the example above, its as if we are using a nested loop

    Time Complexity: O(n^2)
    Space Complexity: O(n), for the set

Idea 2 (Optimized Set):
    - We want to find the 'LONGEST' sequence, and that will only be achieved if we start at the smallest of that sequence
    Example: set(1,2,3,4,10,11)
        - 1,2,3,4 is the longest sequence
        - 2,3,4 and 3,4 and 10,11 are also sequences, but much smaller
    
    - We can check for a condition where for a value if its 'value-1' doesnt exist, only then start traversing forward
        Example: set(1,2,3)
        - since (1-1) doesnt exist in the set, it must be the smallest value that makes up the sequence
        - (2-1) exists in the set and so does (3-1)
    
    Time Complexity: O(n)
    Space Complexity: O(n)
"""

def solution(nums):
    num_set = set(nums)
    max_sequence_len = 0

    for curr_num in num_set:
        seq_len = 1
        if (curr_num-1) not in num_set:
            # Start of a sequence
            while curr_num + 1 in num_set:
                seq_len += 1 
                curr_num += 1 
            
        max_sequence_len = max(max_sequence_len, seq_len)
    
    return max_sequence_len
    

nums = [10,20,30]
print(solution(nums))