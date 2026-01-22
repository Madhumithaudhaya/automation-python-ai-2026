# Script:
# This program generates the FizzBuzz sequence from 1 to n.
# For multiples of 3, it adds "Fizz" to the result list.
# For multiples of 5, it adds "Buzz" to the result list.
# For numbers that are multiples of both 3 and 5, it adds "FizzBuzz".
# For all other numbers, it adds the number itself as a string.
# The final list containing the FizzBuzz sequence is returned.

from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []

        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                ans.append("FizzBuzz")
            elif i % 3 == 0:
                ans.append("Fizz")
            elif i % 5 == 0:
                ans.append("Buzz")
            else:
                ans.append(str(i))

        return ans
