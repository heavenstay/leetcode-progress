# Problem: Product Of Array Except Self: https://leetcode.com/problems/product-of-array-except-self/
# Difficulty: Medium
# Time Taken: 40 min
# Attempts: 5
# Hints Used: Yes
# Notes: Use a prefix and postfix to calculate the product. 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for i in range(0, len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix 
            postfix *= nums[i]            

        return res