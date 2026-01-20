# Script:
# This program reverses a list of characters in-place.
# It uses Python slicing to reverse the list efficiently.
# The expression s[::-1] returns the reversed list.
# Assigning it to s[:] updates the original list instead of creating a new one.
# This satisfies the problem constraint of modifying the input list in-place.

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[:] = s[::-1]
