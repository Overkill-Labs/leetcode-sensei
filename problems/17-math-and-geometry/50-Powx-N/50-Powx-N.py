'''
https://leetcode.com/problems/powx-n/
'''

last_solved     = "2026-10-01"
revisit_in_days = 1
times_reviewed  = 1
difficulty      = "medium"
topic_tags      = ["math", "recursion"]

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def c_pow(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x

            half = c_pow(x, n // 2)
            square = half * half

            if n % 2:
                return x * square

            return square

        return c_pow(x, n) if n > 0 else 1 / c_pow(x, -n)
