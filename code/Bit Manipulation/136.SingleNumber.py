# Problem: Single Number
# Difficulty: Easy
# Time Taken: 5 min
# Attempts: 1
# Hints Used: No
# Notes: Used XOR to solve the problem. It permits us to find the unique number in the list. Why ? Because XOR of a number with itself is 0. So, if we XOR all the numbers in the list, we will be left with the unique number.
class Solution(object):
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result = result ^ num
        return result