"""
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. 
It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).
"""

"""
Input:
    - s: string
Output:
    - Boolean

Considerations:
    - Length of s: 1 <= s.length <= 1000
    - Values that s[i] can take: s is made up of only printable ASCII characters.

Idea 1:
    - Store the reverse of s in another variable
    - Iterate over both and see if the reversed characters == s characters
    
    - Case insensitive:
        - Convert all characters to lowercase
    
    - Non-Alphanumeric Character Ignore:
        - Separate function to check
    
    Time Complexity: O(n)
    Space Complexity: O(n), for the reversed s

Idea 2 (Two Pointers):
    - Intiialize left and right pointers at the start and end of s
    - Use same logic as above

    - Keep iterating the left and right pointers (forward and back respectively) until both reach a valid character
    
    Time Complexity: O(n)
    Space Complexity: O(1)
"""



def isAlpha(char):
    if ord('a') <= ord(char) <= ord('z') or ord('A') <= ord(char) <= ord('Z') or ord('0') <= ord(char) <= ord('9'):
        return True
    else:
        return False

def solution(s):
    left, right = 0, len(s) - 1

    while left < right:
        # Increment left
        while not isAlpha(s[left]) and left < right:
            left += 1
        # Decrement right
        while not isAlpha(s[right]) and left < right:
            right -= 1
        
        if s[left].lower() != s[right].lower():
            return False
        
        left, right = left + 1, right - 1

    return True

s = "Was it a car or a cat I saw?"
print(solution(s))