"""
You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.
"""

"""
Input:
    - prices: List[int]

Output:
    - int

Considerations:
    - Length of prices: 1 <= prices.length <= 100
    - Values that prices[i] can take: 0 <= prices[i] <= 100

Idea 1 (Nested Loop):
    - For each price, look at all the future prices and find their difference
    - Keep track of the largest one

    Time Complexity: O(n^2)
    Space Complexity: O(1)

Idea 2 (Sliding Window):
    - The main idea is that we want to but at the lowest and sell at the highest

    - Can create a window using left and right pointers where the right always moves forward
        - The left stays at the smallest price we have seen thus far
    Every time the right ptr moves froward, calculate the difference

    Time Complexity: O(n)
    Space Complexity: O(1)

"""

def solution(prices):
    left = 0
    ans = 0

    for right in range(len(prices)):
        if prices[right] < prices[left]:
            left = right
        ans = max(ans, prices[right] - prices[left])
    
    return ans

prices = [10,8,7,5,2]
print(solution(prices))


        
