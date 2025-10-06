"""
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can 
be different.

"""

"""
Input:
    str: List[string]
Output:
    List[List[string]]

Considerations:
    - Length of strs: 1 <= strs.length <= 1000.
    - Length os strs[i]: 0 <= strs[i].length <= 100
    - Characters that can be used for the string elements: strs[i] is made up of lowercase English letters.

Idea 1 (Sorting):
    - Sorted anagrams will always be the same
        - Example: cat and tac, sorted will be act
    
    - Use the sorted string as the 'identifier'
    - Can use the identifier as a key in a dictionary and add the element as a value into a list
        - Dictionary: { key: [str1, str2] }
    If m is the average length of strs[i], then sorting would cost O(mlogm)

    Time Complexity: O(n * mlogm)
    Space Complexity: O(n * m) - Worst case every element is different (No anagrams), so dictionary grows to size of strs

Idea 2:
    - Since we are limited to lowercase letters, we can use a list of size 26 as the identifier
        - [0,1,4..], b occurs once, c occurs 4 times
        - can find index by doing ord(char) - ord(a)
    
    - Whenever we go over an element, check the characters, and the character frequency list becomes to identifier

    {key:value} => {[0,0,0..] : ["abc","cba"]}
    Need to convert the identifier into a tuple since keys need to be immutable

    ["abc","de","gh"]

    Time Complexity: O(n*m), where m is the average length of each element
    Space Complexity: O(n * 26) => O(n)
"""

from collections import defaultdict

def solution(strs):
    anagram_dict = defaultdict(list)

    for word in strs:
        identifier = [0] * 26
        for char in word:
            identifier[ord(char) - ord('a')] += 1
        
        anagram_dict[tuple(identifier)].append(word)
    
    ans = [values for values in anagram_dict.values()]
    return ans

strs = ["act","pots","tops","cat","stop","hat"]
print(solution(strs))
            
