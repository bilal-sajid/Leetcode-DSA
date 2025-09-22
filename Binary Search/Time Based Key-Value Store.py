"""
Implement a time-based key-value data structure that supports:

Storing multiple values for the same key at specified time stamps
Retrieving the key's value at a specified timestamp

Implement the TimeMap class:
    TimeMap() 
        - Initializes the object.
    void set(String key, String value, int timestamp): 
        - Stores the key key with the value value at the given time timestamp.
    String get(String key, int timestamp): 
        - Returns the most recent value of key if set was previously called on it and the most recent timestamp for that key prev_timestamp is less than or equal to the given timestamp (prev_timestamp <= timestamp). 
        - If there are no values, it returns "".

Note: For all calls to set, the timestamps are in strictly increasing order.
"""

"""
Input:
    - None
    - key: string; value: string; timestamp: int
    - key: string; timestamp: int

Output:
    - None
    - None
    - string

Considerations:
    - Characters that key and value can take: key and value only include lowercase English letters and digits.
    - Legth of key and value: 1 <= key.length, value.length <= 100
    - Range of values that timestamp can take: 1 <= timestamp <= 1000

Note:
    - One key can have multiple values, which will each have their associated timestamps
    - For "get", we want the value at that timestamp OR if it does not exist then the most recent value associated with a timestamp <= the input timestamp

Idea 1:
    - Store the key-value pairing in a hashmap
        {"key":"value"}
    - One key can have multiple values, and each are associated with a specific timestamp, so sotre those in a list
        {"key":[(val1,t1), (val2,t2)]}
    
    - Whenever "get" is called, jsut go to that key and iterate over all elements and find the most recent one
        - Keep going until the value associated timestamp is <= timestamp and keep track
    
    Time Complexity: O(n) - Worst case is if all values are associated with one key so need to go over each one
    Space Complexity: O(n+k) - Space taken by the keys and values

Idea 2 (Binary Search):
    - Important Note is how the timestamps are ALWAYS in increasing order!
        - The elements are SORTED so we can use binary search

    - When we get to a particular key, perform binary search on the values

    Time Complexity: O(logn)
    Space Complexity: O(n+k)
"""

from collections import defaultdict

class TimeMap:
    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key, value, timestamp):
        self.hashmap[key].append((value, timestamp))
        # print(self.hashmap)

    def get(self, key, timestamp):
        answer = ""
        if not self.hashmap[key]:
            return answer
        
        associated_values = self.hashmap[key] # List of tuples (value, timestamp)
        
        left, right = 0, len(associated_values) - 1

        while left <= right:
            mid = (left + right) // 2
            curr_value, value_timestamp = associated_values[mid][0], associated_values[mid][1]
            
            if value_timestamp == timestamp:
                return curr_value
            elif value_timestamp > timestamp:
                # If the value if greater than the timestamp, we dont want to update our answer
                right = mid - 1
            elif value_timestamp < timestamp:
                # If the value if smaller than the timestamp, we want to update our answer
                answer = curr_value
                left = mid + 1

        return answer

test = TimeMap()
test.set("alice", "okay", 1)
test.set("alice", "wow", 2)
test.set("alice", "hello", 5)
test.set("alice", "there", 10)
test.set("alice", "nice", 11)
test.set("alice", "day", 20)

print(test.get("alice", 3))