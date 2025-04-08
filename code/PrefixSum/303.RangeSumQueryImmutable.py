# Problem: Range Sum Query - Immutable: https://leetcode.com/problems/range-sum-query-immutable/
# Difficulty: Easy
# Time Taken: 20 min
# Attempts: 1
# Hints Used: No
# Notes: 
# - Learned and implemented the prefix sum technique to optimize multiple range sum queries.
# - The trick of adding an initial 0 in the prefix_sum list simplifies the math.
# - Important to remember the offset: prefix_sum[i] holds sum up to nums[i - 1].
# - Efficient solution with O(1) time complexity for each sumRange call and O(n) preprocessing.
# - Very useful pattern for similar problems involving repeated range queries.
class NumArray:
    def __init__(self, nums):
        # We create a prefix_sum list to store cumulative sums.
        # We start with a 0 to make the math easier when calculating ranges.
        # This way, prefix_sum[i] represents the sum of nums[0] to nums[i - 1].
        self.prefix_sum = [0]
        for i in range(len(nums)):
            # Add the current number to the last value in prefix_sum to build the next sum
            self.prefix_sum.append(self.prefix_sum[i] + nums[i])

    def sumRange(self, i, j):
        # To get the sum from index i to j (inclusive), 
        # we subtract the sum up to index i - 1 from the sum up to index j.
        # That's why we return prefix_sum[j + 1] - prefix_sum[i].
        return self.prefix_sum[j + 1] - self.prefix_sum[i]