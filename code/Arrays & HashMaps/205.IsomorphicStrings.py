# Problem: Counting Bits: https://leetcode.com/problems/isomorphic-strings/description/
# Difficulty: Easy
# Time Taken: 20 min
# Attempts: 2
# Hints Used: Yes
# Notes: Use a hashmap to store the mapping of characters from s to t. If a character in s is already in the hashmap, check if the mapping is the same as the current character in t. If not, return False. If the current character in t is already in the hashmap, return False. Otherwise, add the mapping to the hashmap.
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash_map = {}

        for i in range(0, len(s)):
            if s[i] in hash_map: 
                if t[i] != hash_map[s[i]]:
                    return False
            elif t[i] in hash_map.values():
                return False 
            
            hash_map[s[i]] = t[i]

        return True 