"""
Design an algorithm to encode a list of strings to a single string. 
The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example:
Input: ["neet","code","love","you"]
Output:["neet","code","love","you"]

"""

"""
Input:
    - List[string]
    - string


Output:
    - string
    - List[string]

Considerations:
    - Length of strs: 0 <= strs.length < 100
    - Length of strs[i]: 0 <= strs[i].length < 200
    - Values that strs[i] can take: strs[i] contains only UTF-8 characters.

Idea 1 (Using a non-UTF-8 character):
    - When joining the string, join the characters with a special character between the words
    - This character is what spearates the words from each other and will be the signal that will be used for the decoding step

    Time Complexity: 
        Encode: O(n), where n is the length of strs
        Decode: O(n*m), where m is the average length of the words in strs

    Space Complexity:
        Encode: O(1)
        Decode: O(1)

Idea 2:
    - When encoding, have a special character, AND ALSO the length of the upcoming word
    - ["neet","code","love","you"] => 4#neet4#code4#love3#you
    - We need to use both because the word length can be greater than 9, so it requires complex slicing

    - The first number represents the number of letters that make up the word
        - The problem with this is, that the word length > 9, in which case we dont know when the number starts and ends

    - We use the special character in order to find out the length of the word
        - Can then use the word_length to get the word we are looking for

    Time Complexity: O(n), where n is the total number of characters
    Space Complexity: O(n)
"""

def encode(strs):
    encoded_string = []
    special_char = "#"
    for word in strs:
        num_character = len(word)
        encoded_string.append(str(num_character))
        encoded_string.append(special_char)
        for char in word:
            encoded_string.append(char)
        
    return "".join(encoded_string)


# print(encode(["we","say",":","yes","!@#$%^&*()"]))

def decode(s):
    decoded_strings = []
    i = 0
    while i < len(s):
        j=i
        while s[j] != "#":
            j += 1

        word_length = int(s[i:j])
        curr_word = s[j+1: j+1+word_length]
        decoded_strings.append(curr_word)
        i=j+1+word_length
    
    return decoded_strings

print(decode("2#we3#say1#:3#yes10#!@#$%^&*()"))
        


