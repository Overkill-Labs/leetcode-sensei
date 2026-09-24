'''
https://leetcode.com/problems/valid-parenthesis-string/
'''

last_solved     = "2026-09-24"
revisit_in_days = 1
times_reviewed  = 1
difficulty      = "medium"
topic_tags      = ["string", "dynamic-programming", "stack", "greedy"]

# Greedy range tracking — [lo, hi] = range of possible open-bracket balances
# Intuition: each '*' branches the balance three ways; the reachable set is always
# contiguous, so min/max describe it. Clamp lo at 0 (negative paths are dead),
# fail if hi < 0 (even all-'(' choices can't recover), valid iff 0 reachable at end.
class Solution:
    def checkValidString(self, s: str) -> bool:
        lo, hi = 0, 0

        for b in s:
            if b == "(":
                lo, hi = lo + 1, hi + 1
            elif b == ")":
                lo, hi = max(lo - 1, 0), hi - 1
            else:
                lo, hi = max(lo - 1, 0), hi + 1

            if hi < 0:
                return False

        if lo > 0:
            return False

        return True
        # Time:  O(N) — single pass
        # Space: O(1) — two counters
