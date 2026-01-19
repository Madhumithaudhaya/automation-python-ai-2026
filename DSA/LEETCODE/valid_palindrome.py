# Problem: Valid Palindrome
# Platform: LeetCode
# Approach:
# 1. Convert string to lowercase
# 2. Remove non-alphanumeric characters
# 3. Compare string with its reverse
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s= [i for i in s.lower() if i.isalnum()]
        return s==s[::-1]
