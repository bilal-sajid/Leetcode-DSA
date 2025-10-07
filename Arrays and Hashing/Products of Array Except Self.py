"""
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in O(n) time without using the division operation?

Example:
    Input: nums = [1,2,4,6]
    Output: [48,24,12,8]
"""

"""
Input:
    - nums: List[int]
Output:
    - List[int]

Considerations:
    - Length of nums: 2 <= nums.length <= 1000
    - Values that nums[i] can take: -20 <= nums[i] <= 20

Idea 1 (Simple Division):
    - Multiply all numbers together to get a total product
    Example: nums = [1,2,4,6], total_product = 1*2*4*6 = 48

    - For each num, divice total_product by that num to get the answer at that index
    Example: [48/1, 48/2,48/4,48/6]

    Time Complexity: O(n)
    Space Complexity: O(1)

Idea 2 (Prefix and Postfix Product):
    - The answer at each index is dependent on the products before and after it (not including itself)

    - Can create two lists
        - One for prefix: Move forward in nums and get the current product
        - One for postfix: MOve backwards in nums and get the product

    Then for each index, we get the answer by doing, prefix[index-1] * postfix[index+1]

    Time Complexity: O(n + n + n) => O(n)
    Space Complexity: O(n)

Idea 3 (Reduced Space):
    - Single pass where each indexs' prefix product is calculated (NOT INCLUDING ITESELF!). - Start with 1
    - Another pass (backword) where the postfix product is calculated (NOT INCLUDING ITSELF!) - Start with 1

    Example:
        nums = [1,2,4,6]
        First Pass = [1,1,2,8]
        Second Pass(Backward) = [1*48,1*24,2*6,8*1]
    
    Time Complexity: O(n + n) => O(n)
    Space Complexity: O(1), not including our answer array
"""

def solution(nums):
    answer = []
    prefix_prod = 1
    for i in range(len(nums)):
        answer.append(prefix_prod)
        prefix_prod *= nums[i]
    
    postfix_prod = 1
    for i in range(len(nums)-1, -1, -1):
        answer[i] = answer[i] * postfix_prod
        postfix_prod *= nums[i]
    
    return answer

nums = [1,2,4,6]
print(solution(nums))