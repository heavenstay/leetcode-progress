# Problem: Contains Duplicate II: https://leetcode.com/problems/contains-duplicate-ii/
# Difficulty: Easy
# Time Taken: 20 min
# Attempts: 2
# Hints Used: No
# Notes: Use a hashmap to implement the solution in O(n) time. Store the index of the last occurence of each number in the hashmap. If the difference between the current index and the last occurence is less than or equal to k, return True. Otherwise, update the last occurence of the number in the hashmap.
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_map = {}

        for i in range(0, len(nums)):
            if nums[i] in hash_map.keys():
                if abs(hash_map[nums[i]] - i) <= k:
                    return True
            
            hash_map[nums[i]] = i

        return False 