# Problem: Evaluate Reverse Polish Notation: https://leetcode.com/problems/evaluate-reverse-polish-notation
# Difficulty: Medium
# Time Taken: 30 min
# Attempts: 1
# Hints Used: No
# Notes: 
# - Use stack to append non operator tokens. When an operator is found, it calculate the result with the top two items from the stack and replace them. 
import math
import operator
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens: 
            if token == '+':
                stack[-2:] = [operator.add(stack[-2], stack[-1])]
            elif token == '-':
                stack[-2:] = [operator.sub(stack[-2], stack[-1])]
            elif token == '*':
                stack[-2:] = [operator.mul(stack[-2], stack[-1])]
            elif token == '/':
                stack[-2:] = [math.trunc(operator.truediv(stack[-2], stack[-1]))]
            else:
                stack.append(int(token))
        return stack[0]