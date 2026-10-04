'''
https://leetcode.com/problems/partition-labels/
'''

last_solved     = "2026-10-04"
revisit_in_days = 5
times_reviewed  = 4
difficulty      = "medium"
topic_tags      = ["hash-table", "two-pointers", "string", "greedy"]

class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last_occur = defaultdict(int)
        for idx, c in enumerate(s): last_occur[c] = idx

        output = []

        max_occur, left = 0, 0
        for right, c in enumerate(s):
            max_occur = max(max_occur, last_occur[c])

            if right == max_occur:
                output.append(right - left + 1)
                left = right + 1

        return output
        # Time:  O(N)
        # Space: O(1) — last_occur holds at most 26 keys (lowercase letters only)
