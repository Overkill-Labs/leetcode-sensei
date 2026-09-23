'''
https://leetcode.com/problems/merge-triplets-to-form-target-triplet/
'''

last_solved     = "2026-09-23"
revisit_in_days = 3
times_reviewed  = 2
difficulty      = "medium"
topic_tags      = ["array", "greedy"]

class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        a, b, c = 0, 0, 0

        for x, y, z in triplets:
            if x <= target[0] and y <= target[1] and z <= target[2]:
                a, b, c = max(a, x), max(b, y), max(c, z)
            if [a, b, c] == target:
                return True

        return False
