# Problem: Valid Anagram: https://leetcode.com/problems/valid-anagram/
# Difficulty: Easy
# Time Taken: 20 min
# Attempts: 1
# Hints Used: No
# Notes: Use hash_map to store distinct letters with the number of time they're appearing in the string. If equals it means it's an anagram. 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map_s = {}
        hash_map_t = {}

        for letter in s:
            if letter in hash_map_s:
                hash_map_s[letter] += 1
            else: 
                hash_map_s[letter] = 1

        for letter in t:
            if letter in hash_map_t:
                hash_map_t[letter] += 1
            else: 
                hash_map_t[letter] = 1

        return hash_map_s == hash_map_t