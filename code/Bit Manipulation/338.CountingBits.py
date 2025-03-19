# Problem: Counting Bits: https://leetcode.com/problems/counting-bits/description/
# Difficulty: Easy
# Time Taken: 20 min
# Attempts: 1
# Hints Used: Yes
# Notes: Used a helper function to count the number of 1 bits in a number. Use the operation n & (n - 1) to count the number of 1 bits in a number. 
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        years = []
        for i in range(0, n + 1):
            years.append(countBit1(i))
        return years

# This methods counts the number of 1 bits in a number. It uses the operation n & (n - 1) to count the number of 1 bits in a number.
# For example, if n = 5, then n = 101. n - 1 = 100. n & (n - 1) = 100. So, the rightmost 1 bit is removed.
# We do it until n becomes 0. The number of times we do this operation is the number of 1 bits in the number.
def countBit1(n):
    count = 0
    while n != 0:
        n = (n & (n - 1))
        count = count + 1
    return count