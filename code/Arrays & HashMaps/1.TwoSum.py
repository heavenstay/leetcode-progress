# Problem: Two Sum: https://leetcode.com/problems/two-sum
# Difficulty: Easy
# Time Taken: 10 min
# Attempts: 1
# Hints Used: No
# Notes: We use a hash_map to store the difference between the target and the current number as a key and the index as a value. We have to check if the current num is not already in the hash_map because if it's the case it means we have a sum of two elements that gives the target (hash_map[nums[i]] and i).
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(0, len(nums)):
            diff = target - nums[i]
            if nums[i] in hash_map:
                return [hash_map[nums[i]], i]
            hash_map[diff] = i