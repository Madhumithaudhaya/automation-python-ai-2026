# Script:
# This program finds the index of the first non-repeating character in a string.
# It first counts the frequency of each character using a dictionary.
# Then, it iterates through the string by index to find the first character
# whose frequency is exactly one.
# If such a character is found, its index is returned.
# If no unique character exists, the function returns -1.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        mp = {}
        for a in s:
            mp[a] = mp.get(a, 0) + 1

        for i in range(len(s)):
            if mp[s[i]] == 1:
                return i

        return -1
