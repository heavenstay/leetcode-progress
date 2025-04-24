# Problem: Min Stack: https://leetcode.com/problems/min-stack/
# Difficulty: Medium
# Time Taken: 20 min
# Attempts: 1
# Hints Used: No
# Notes: 
# - Use a second stack to store min values to get the current min value of the stack with O(1) complexity 
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_values = []

    def push(self, val: int) -> None:
        min_val = val
        if len(self.min_values) != 0:
            min_val = min(self.min_values[-1], min_val)
        
        self.min_values.append(min_val)
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_values.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_values[-1]