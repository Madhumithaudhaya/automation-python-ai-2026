# Script:
# This program calculates the sum of digits of a given number.
# It repeatedly extracts the last digit using modulo (%) operator.
# Each extracted digit is added to a running total.
# The number is reduced by removing the last digit using integer division (//).
# The process continues until the number becomes zero.
# Finally, the sum of all digits is returned as an integer.

class Solution:
    def sumOfDigits(self, n):
        sum = 0
        while n > 0:
            num = n % 10
            sum += num
            n = n // 10
        return int(sum)
