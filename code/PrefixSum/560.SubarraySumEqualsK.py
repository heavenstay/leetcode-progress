# Problem: Subarray Sum Equals K
# Link: https://leetcode.com/problems/subarray-sum-equals-k
# Difficulty: Medium
# Time Taken: 1h+
# Attempts: 4
# Hints Used: Yes
# Notes:
#   - To avoid a brute-force approach, we use a hash map to store the places we've "been" (prefix sums).
#   - Think of it like walking along a trail: at each step, you stop and check if the distance from a previous stop equals k.
#   - If the difference between your current position and a previous one is k, you've found a valid subarray.
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:        
        res = 0
        curPlace = 0
        alreadyBeenPlace = {0: 1}  # Base place is at 0 (before starting the walk)

        for num in nums:
            curPlace += num
            
            diff = curPlace - k
            if diff in alreadyBeenPlace: 
                res += alreadyBeenPlace[diff]

            if curPlace in alreadyBeenPlace:
                alreadyBeenPlace[curPlace] += 1
            else: 
                alreadyBeenPlace[curPlace] = 1
                
        return res