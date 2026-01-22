# Script:
# This program generates a specific numeric pattern based on the input n.
# For each row, numbers start from n and decrease step by step.
# Each number is repeated a fixed number of times in the row.
# After completing a row, -1 is added as a separator.
# The pattern continues until all rows are generated.
# The final pattern is stored in a list and returned.

class Solution:
    def printPat(self, n):
        result = []
        N = n
        count = 0

        for i in range(n):
            x = n
            m = n - count
            counter = 0

            for j in range(n * N):
                result.append(x)
                counter += 1

                if counter == m:
                    x = x - 1
                    counter = 0

            N = N - 1
            result.append(-1)
            count += 1

        return result
