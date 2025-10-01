"""
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

"""

"""
Input:
    - s: string
    - t: string

Output:
    - Boolean

Considerations:
    - Length of s and t: None
    - Valid characters that can make up s and t: s and t consist of lowercase English letters.


Important Note:
    - We are limited to lowercase letters as characters - 26 letters

Idea 1 (Hashmap):
    - Have a counter for the characters in one of the strings and count the occurances
    counter = {character: frequency}

    - Go over the other input string and start deleting from the hashmap
        - Remove the key if the frequency is == 0
        - If we try to remove a character that isnt in the hashmap OR encounter a char that isnt in the hashmap, they cannot be anagrams
    
    - If the length of the hashmap != 0, they are not anagrams

    Time Complexity: O(n+m), where n is the length of s and m is the length of t
    Space Complexity: O(26) => O(26), since the size of the hashmap is proportional the the unique characters

Idea 2 (List/Array):
    - Since we are limited to 26 characters, we can have a list initialized with 0's of size 26
        - Each index represents the frequency that character has occurred
            - Example: [0,4,2..], b occurred 4 times and c occurred twice
    
    - Populate the frequencies using one of the inputs
    - Iterate over the second input and start decreasing
    - iterate over the list and if we find a value that isnt =0, the strings are not anagrams of each other

    Time Complexity: O(n+m+26)
    Space Complexity: O(26) => O(k)

    Slight Optimization:
        - Check if the lengths are equal in the beginning - if they are not equal, there is no way they can be anagrams

Idea 3 (Sorting):
    - If the lrngths are equal, then if we sort all the characters should be at the same position (if anagrams)

    Time Complexity: O(nlogn + mlogm)
    Space Complexity: O(1), if sorting in place
"""

from collections import defaultdict
def solution1(s, t):
    counter = defaultdict(int)
    for char in s:
        counter[char] += 1
    
    for char in t:
        if char not in counter:
            return False
        counter[char] -= 1
        if counter[char] == 0:
            del counter[char]
        
    return False if len(counter) !=0 else True
    
print(solution1("hello", ""))

def solution2(s, t):
    if len(s) != len(t):
        return False
    
    character_freq = [0] * 26
    for i in range(len(s)):
        character_freq[ord('z') - ord(s[i])] += 1
        character_freq[ord('z') - ord(t[i])] -= 1
    
    for frequency in character_freq:
        if frequency != 0:
            return False
    
    return True

print(solution2("hello", ""))