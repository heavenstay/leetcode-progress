# Problem: Counting Bits: https://leetcode.com/problems/isomorphic-strings/description/
# Difficulty: Easy
# Time Taken: 20 min
# Attempts: 2
# Hints Used: Yes
# Notes: Used two dictionaries to map the characters in the two strings. If the mapping is not the same, return False.
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s = {}
        map_t = {}

        for i in range(0, len(s)):
            if s[i] not in map_s: 
                map_s[s[i]] = i
            
            if t[i] not in map_t: 
                map_t[t[i]] = i

            if map_s[s[i]] != map_t[t[i]]:
                return False
        
        return True