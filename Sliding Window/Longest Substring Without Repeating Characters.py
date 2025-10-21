"""
Given a string s, find the length of the longest substring without duplicate characters.
A substring is a contiguous sequence of characters within a string.
"""

"""
Input:
    - s: string
Output:
    - int

Considerations:
    - Length of s: 0 <= s.length <= 1000
    - Characters that s[i] can take: s may consist of printable ASCII characters.

Idea 1:
    - Consider all possible substrings and see if it is valid
    - For all the substrings that are VALID, keep track of the one that is the longest length

    Time Complexity: O(n^2)
    Space Complexity: O(1)

Idea 2 (Sliding Window):
    - 'Substrings' hints at using this technique
    
    - Keep moving the right ptr forward at every iteration
    - When the 'window' becomes invalid, shrink the window by moving the left ptr

    What makes the window valid?
        - No duplicate characters
            - Can check that by using a set
            - If the current character already exists in the set then that would make it invalid so remove UNTIL that character is removed then add he current one
    
    Time Complexity: O(n)
    Space Complexity: O(n), for the set
"""

def solution(s):
    left = 0
    char_set = set()
    ans = 0

    for right in range(len(s)):
        curr_char = s[right]
        
        while curr_char in char_set:
            char_set.remove(s[left])
            left += 1
        
        char_set.add(s[right])
        ans = max(ans, right - left + 1)
    
    return ans

s="abcde"
print(solution(s))
        
