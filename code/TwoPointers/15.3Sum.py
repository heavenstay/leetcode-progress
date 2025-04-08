# Problem: 3Sum: https://leetcode.com/problems/3sum
# Difficulty: Medium
# Time Taken: 34 min
# Attempts: 2
# Hints Used: Yes
# Notes:  
# - Fix one number and solve the rest as a Two Sum problem with two pointers.  
# - Improve performance by skipping duplicate values to avoid redundant calculations.  
# - Adjust left and right pointers efficiently to find unique triplets.  
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        threeSum = []
        sorted_nums = sorted(nums)

        for x in range(0, len(sorted_nums) - 2): 
            # If the fixed pointer is the same than before we go to the next one 
            if x > 0 and sorted_nums[x] == sorted_nums[x - 1]: 
                continue

            l = x + 1
            r = len(sorted_nums) - 1

            while l < r: 
                sum_result = sorted_nums[x] + sorted_nums[l] + sorted_nums[r]
                if sum_result < 0: 
                    l += 1
                elif sum_result > 0:
                    r -= 1 
                else: 
                    threeSum.append([sorted_nums[x], sorted_nums[l], sorted_nums[r]])
                    # Move left pointer past duplicates to avoid duplicate triplets
                    l += 1
                    while l < r and sorted_nums[l] == sorted_nums[l - 1]:
                        l += 1
                    # Move right pointer past duplicates to avoid duplicate triplets
                    r -= 1
                    while l < r and sorted_nums[r] == sorted_nums[r + 1]:
                        r -= 1

        return threeSum