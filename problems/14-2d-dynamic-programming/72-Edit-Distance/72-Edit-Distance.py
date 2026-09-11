'''
https://leetcode.com/problems/edit-distance/
'''

last_solved     = "2026-09-11"
revisit_in_days = 3
times_reviewed  = 2
difficulty      = "medium"
topic_tags      = ["string", "dynamic-programming"]

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dp(i, j):
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i

            if word1[i] == word2[j]:
                return dp(i + 1, j + 1)

            return 1 + min(
                dp(i + 1, j),    # delete
                dp(i, j + 1),    # insert
                dp(i + 1, j + 1) # replace
            )

        return dp(0, 0)
        # Time:  O(M * N)
        # Space: O(M * N)
