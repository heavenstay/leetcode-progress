# Problem: Two Sum II - Input Array Is Sorted: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
# Difficulty: Medium
# Time Taken: 10 min
# Attempts: 2
# Hints Used: Yes
# Notes: Use two pointers, one at the start and one at the end. Move the pointers left or right based on the sum, taking advantage of the sorted order of the array.
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 0 
        index2 = len(numbers) - 1

        while index1 < index2:
            twoSum = numbers[index1] + numbers[index2]
            if twoSum == target:
                return [index1 + 1, index2 + 1]

            if twoSum > target:
                index2 = index2 - 1
            elif twoSum < target: 
                index1 = index1 + 1

        return []