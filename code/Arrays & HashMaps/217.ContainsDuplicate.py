# Problem: Contains Duplicate: https://leetcode.com/problems/contains-duplicate/
# Difficulty: Easy
# Time Taken: 5 min
# Attempts: 2
# Hints Used: No
# Notes: Use a set to get only unique letters. If the length is not the same it means there are duplicates. 
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)