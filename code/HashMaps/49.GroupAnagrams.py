# Problem: Group Anagrams: https://leetcode.com/problems/group-anagrams/
# Difficulty: Medium
# Time Taken: 40 min
# Attempts: 5
# Hints Used: Yes
# Notes: Store in the hash_map all anagram by using the word sorted as key. 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}

        for i in range(0, len(strs)):
            sorted_word = ''.join(sorted(strs[i]))

            if sorted_word in hash_map:
                hash_map[sorted_word].append(strs[i])
            else:
                hash_map[sorted_word] = [strs[i]]

        return list(hash_map.values())