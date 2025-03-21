# LeetCode Progress Tracker 🚀

## 📊 Progress Overview
- **Total Problems**: 6
- **Total Solved**: 5
- **Progress:** [████████████████----] 5/6 solved

![Progress Chart](progress_chart.png)

## 📌 Problem List
| #  | Problem | Category | Difficulty | Time Taken | Attempts | Hints Used | Notes | Status |
|----|---------|----------|------------|------------|----------|------------|-------|--------|
| 1 | Counting Bits: https://leetcode.com/problems/isomorphic-strings/description/ | HashMaps | Easy | 20 min | 2 | Yes | Use a hashmap to store the mapping of characters from s to t. If a character in s is already in the hashmap, check if the mapping is the same as the current character in t. If not, return False. If the current character in t is already in the hashmap, return False. Otherwise, add the mapping to the hashmap. | Solved |
| 2 | Contains Duplicate II: https://leetcode.com/problems/contains-duplicate-ii/ | HashMaps | Easy | 20 min | 2 | No | Use a hashmap to implement the solution in O(n) time. Store the index of the last occurence of each number in the hashmap. If the difference between the current index and the last occurence is less than or equal to k, return True. Otherwise, update the last occurence of the number in the hashmap. | Solved |
| 3 | Valid Palindrome | Strings | Easy | 15 min | 2 | No | None | Solved |
| 4 | Problem 1 | Arrays | Easy | 15 min | 1 | No | Used a dictionary to store seen numbers. | Unsolved |
| 5 | Counting Bits: https://leetcode.com/problems/counting-bits/description/ | Bit Manipulation | Easy | 20 min | 1 | Yes | Used a helper function to count the number of 1 bits in a number. Use the operation n & (n - 1) to count the number of 1 bits in a number. | Solved |
| 6 | Single Number | Bit Manipulation | Easy | 5 min | 1 | No | Used XOR to solve the problem. It permits us to find the unique number in the list. Why ? Because XOR of a number with itself is 0. So, if we XOR all the numbers in the list, we will be left with the unique number. | Solved |
