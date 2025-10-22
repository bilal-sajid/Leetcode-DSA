"""
You are given two strings s1 and s2.

Return true if s2 contains a permutation of s1, or false otherwise. 
That means if a permutation of s1 exists as a substring of s2, then return true.

Both strings only contain lowercase letters.
"""

"""
Input:
    - s1: string
    - s2: string

Output:
    - Boolean

Considerations:
    - Length of s1 and s2: 1 <= s1.length, s2.length <= 1000

Idea 1 (Fixed Window):
    Main Idea: DOES S1 EXIST IN S2?

    - If s1 length > s2 length, we can immediately return False since there is no way that it could be present (in any form) within s2

    - Can create a fixed size window of length of s1 and track the characetr in that window
    - Need a left pointer to remove from the back of the window

    - 2 Options:
        1) Hashmap: Have two hashmaps and compare them every time a character is added/removed from the window
        2) List: Each index represent the characters and their frequencies
    
    Time Complexity: O(n * k), where n represents size of s2 and where k is the allowable character range
    Space Complexity: O(k)
"""

def solution(s1, s2):
    if len(s1) > len(s2):
        return False
    
    s1_char_freq = [0] * 26
    s2_char_freq = [0] * 26

    for i in range(len(s1)):
        s1_char_freq[ord(s1[i]) - ord('a')] += 1
        s2_char_freq[ord(s2[i]) - ord('a')] += 1
    
    left = 0
    for right in range(len(s1), len(s2)):
        if s1_char_freq == s2_char_freq: # This is running in O(k) -> O(26)
            return True
        
        s2_char_freq[ord(s2[right]) - ord('a')] += 1
        s2_char_freq[ord(s2[left]) - ord('a')] -= 1
        left += 1
    
    return False if s1_char_freq != s2_char_freq else True


s1 = "aba"
s2 = "lecaabee"
print(solution(s1, s2))