# Problem: Valid Parentheses: https://leetcode.com/problems/valid-parentheses/
# Difficulty: Easy
# Time Taken: 20 min
# Attempts: 1
# Hints Used: No
# Notes: 
# - Use a hashmap to store close to open brackets and a stack to detect if there are valid 
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s: 
            if c in closeToOpen:
                if len(stack) > 0 and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(c)

        return len(stack) == 0