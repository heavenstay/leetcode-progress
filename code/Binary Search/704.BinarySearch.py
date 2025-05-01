# Problem: Binary Search – https://leetcode.com/problems/binary-search/
# Difficulty: Easy
# Time Taken: 10 min
# Attempts: 1
# Hints Used: No
# Notes:
# - Implemented classic binary search algorithm to efficiently narrows down the search space by dividing the array in half each iteration.
# - Time complexity: O(log n), since the array is halved each time.
# - Space complexity: O(1), as the search is done in-place.
# - Binary search only works on sorted arrays.
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        
        return -1