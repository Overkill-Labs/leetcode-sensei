'''
https://leetcode.com/problems/factorial-trailing-zeroes/
'''

last_solved     = "2026-09-17"
revisit_in_days = 1
difficulty      = "medium"
topic_tags      = ["math"]
times_reviewed  = 0

class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0

        while n > 0:
            count += n // 5
            n //= 5
            
        return count
