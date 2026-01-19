# Problem: Count Digits that Evenly Divide a Number
# Platform: GeeksforGeeks
# Approach:
# 1. Extract each digit from the number
# 2. Ignore digit 0 (cannot divide)
# 3. Check if original number is divisible by the digit
# 4. Count such digits
# Time Complexity: O(d) where d = number of digits
# Space Complexity: O(1)

class Solution:
    def evenlyDivides(self, n):
        digits_count = 0
        store_num = n

        while n > 0:
            digit = n % 10

            if digit != 0 and store_num % digit == 0:
                digits_count += 1

            n //= 10

        return digits_count


# ---- Test case (for local testing only) ----
if __name__ == "__main__":
    sol = Solution()
    print(sol.evenlyDivides(12))   # Expected output: 2
    print(sol.evenlyDivides(2446)) # Expected output: 1
