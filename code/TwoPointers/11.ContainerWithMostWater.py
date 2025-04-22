# Problem: Container with most water: https://leetcode.com/problems/container-with-most-water
# Difficulty: Medium
# Time Taken: 10 min
# Attempts: 1
# Hints Used: No
# Notes:  
# - Use the two-pointer approach to find the maximum water container.
# - Start with pointers at both ends of the array.
# - At each step, calculate the area using the shorter height between the two pointers.
# - Move the pointer pointing to the shorter line inward, since moving the taller one won't help increase area.
# - Repeat until both pointers meet.
# - This gives an optimal solution in O(n) time.
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxAmount = 0 
        left, right = 0, len(height) - 1 

        while left < right:
            maxAmount = max(min(height[left], height[right]) * (right - left), maxAmount)

            if height[left] <= height[right]:
                left += 1 
                continue 

            if height[left] > height[right]:
                right -= 1
                continue

        return maxAmount