# Script:
# This program reverses the digits of a given number.
# The number is first converted to a string to allow easy digit manipulation.
# All zero digits are skipped while iterating through the string.
# The remaining digits are collected into a list.
# The list is then joined back into a string.
# Finally, the resulting string is reversed and returned.

# User function Template for python3

class Solution:
    def reverseDigits(self, n):
        n = str(n)
        l = []
        for i in n:
            if i == '0':
                continue
            else:
                l.append(i)
        k = "".join(l)
        return k[::-1]
