# LeetCode Progress Tracker 🚀

## 📊 Progress Overview
- **Total Problems**: 13
- **Total Solved**: 12
- **Progress:** [██████████████████--] 12/13 solved

![Progress Chart](progress_chart.png)

## 📌 Problem List
| #  | Problem | Category | Difficulty | Time Taken | Attempts | Hints Used | Notes | Status |
|----|---------|----------|------------|------------|----------|------------|-------|--------|
| 1 | Counting Bits: https://leetcode.com/problems/isomorphic-strings/description/ | HashMaps | Easy | 20 min | 2 | Yes | Use a hashmap to store the mapping of characters from s to t. If a character in s is already in the hashmap, check if the mapping is the same as the current character in t. If not, return False. If the current character in t is already in the hashmap, return False. Otherwise, add the mapping to the hashmap. | Solved |
| 2 | Group Anagrams: https://leetcode.com/problems/group-anagrams/ | HashMaps | Medium | 40 min | 5 | Yes | Store in the hash_map all anagram by using the word sorted as key. | Solved |
| 3 | Contains Duplicate II: https://leetcode.com/problems/contains-duplicate-ii/ | HashMaps | Easy | 20 min | 2 | No | Use a hashmap to implement the solution in O(n) time. Store the index of the last occurence of each number in the hashmap. If the difference between the current index and the last occurence is less than or equal to k, return True. Otherwise, update the last occurence of the number in the hashmap. | Solved |
| 4 | Encode And Decode Tiny URL: https://leetcode.com/problems/encode-and-decode-tinyurl/ | HashMaps | Medium | 8 min | 1 | No | Use a dictionnary to store the correspondance between the encoded key and the long url. This code can be improve by adding an other hash_map to verify if the url hasn't already encoded, and by verifying if the key wasn't already used even tough the probability is very low. | Solved |
| 5 | Longest Consecutive Sequence: https://leetcode.com/problems/longest-consecutive-sequence | HashMaps | Medium | 15 min | 1 | No | Use a set to store unique values from the input list for O(1) lookups. Iterate through the set and only start counting sequences from numbers that have no predecessor (num - 1 not in set). Expand the sequence by counting consecutive numbers (num + 1) in the set. | Solved |
| 6 | Valid Palindrome | Strings | Easy | 15 min | 2 | No | None | Solved |
| 7 | 3Sum: https://leetcode.com/problems/3sum | TwoPointers | Medium | 34 min | 2 | Yes |  | Solved |
| 8 | Two Sum II - Input Array Is Sorted: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted | TwoPointers | Medium | 10 min | 2 | Yes | Use two pointers, one at the start and one at the end. Move the pointers left or right based on the sum, taking advantage of the sorted order of the array. | Solved |
| 9 | Range Sum Query - Immutable: https://leetcode.com/problems/range-sum-query-immutable/ | PrefixSum | Easy | 20 min | 1 | No |  | Solved |
| 10 | Subarray Sum Equals K | PrefixSum | Medium | 1h+ | 4 | Yes |  | Solved |
| 11 | Problem 1 | Arrays | Easy | 15 min | 1 | No | Used a dictionary to store seen numbers. | Unsolved |
| 12 | Counting Bits: https://leetcode.com/problems/counting-bits/description/ | Bit Manipulation | Easy | 20 min | 1 | Yes | Used a helper function to count the number of 1 bits in a number. Use the operation n & (n - 1) to count the number of 1 bits in a number. | Solved |
| 13 | Single Number | Bit Manipulation | Easy | 5 min | 1 | No | Used XOR to solve the problem. It permits us to find the unique number in the list. Why ? Because XOR of a number with itself is 0. So, if we XOR all the numbers in the list, we will be left with the unique number. | Solved |
