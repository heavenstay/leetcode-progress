# Problem: Longest Consecutive Sequence: https://leetcode.com/problems/longest-consecutive-sequence
# Difficulty: Medium
# Time Taken: 15 min
# Attempts: 1
# Hints Used: No
# Notes: Use a set to store unique values from the input list for O(1) lookups. Iterate through the set and only start counting sequences from numbers that have no predecessor (num - 1 not in set). Expand the sequence by counting consecutive numbers (num + 1) in the set.
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longestConsecutive: int = 0
        currentConsecutive: int = 0

        nums_set = set(nums)

        for num in nums_set: 
            if (num - 1) not in nums_set: 
                currentConsecutive = 1

                while (num + 1) in nums_set:
                    currentConsecutive = currentConsecutive + 1
                    num = num + 1 

                longestConsecutive = max(longestConsecutive, currentConsecutive)

        return longestConsecutive