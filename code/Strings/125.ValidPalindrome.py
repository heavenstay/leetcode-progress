# Problem: Valid Palindrome: https://leetcode.com/problems/valid-palindrome/
# Difficulty: Easy
# Time Taken: 7 min
# Attempts: 1
# Hints Used: No
# Notes: Use a set for valid_letters. Compare left letter and right letter to chech if it's a palindrome. 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid_letters = set({'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9'})

        s = s.lower()
        left = 0
        right = len(s) - 1
        while left < right: 
            if s[left] not in valid_letters:
                left += 1
                continue
            if s[right] not in valid_letters:
                right -= 1
                continue 
            if s[left] != s[right]:
                return False
            
            left += 1
            right -= 1

        return True