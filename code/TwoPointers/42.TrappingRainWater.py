# Problem: Trapping Rain Water: https://leetcode.com/problems/trapping-rain-water
# Difficulty: Hard
# Time Taken: 22 min
# Attempts: 1
# Hints Used: No
# Notes:  
# - Two-pointer approach: simulate trapping from both ends.
# - When the left height is smaller or equal, scan forward and trap water until hitting a wall >= left.
# - When the right height is smaller, scan backward and trap water until hitting a wall >= right.
# - Even though a loop exists inside another loop, each index is visited at most once.
# - So, overall time complexity is still O(n) with constant space.
class Solution:
    def trap(self, height: List[int]) -> int:
        trapped_water = 0 
        left, right = 0, len(height) - 1 

        while left < right:
            if height[left] <= height[right]:
                cursor = left + 1
                water_amount = 0
                while cursor < right and height[cursor] < height[left]: 
                    water_amount += (height[left] - height[cursor])
                    cursor += 1
                trapped_water += water_amount
                left = cursor
            else: 
                cursor = right - 1
                water_amount = 0 
                while cursor > left and height[cursor] < height[right]:
                    water_amount += (height[right] - height[cursor])
                    cursor -= 1
                trapped_water += water_amount 
                right = cursor

        return trapped_water