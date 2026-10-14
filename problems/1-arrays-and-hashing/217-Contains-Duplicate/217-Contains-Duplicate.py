'''
https://leetcode.com/problems/contains-duplicate/description/
'''

last_solved     = "2026-10-14"
revisit_in_days = 39
times_reviewed  = 8
difficulty      = "easy"
topic_tags      = ["arrays", "hashing"]

# REVISIT 2026-10-14: set approach instant; the gap is the trade-off discussion.
#   - Say unprompted: brute O(N^2)/O(1), sort O(N log N), set O(N)/O(N).
#   - Sort space is NOT O(1) in Python (Timsort up to O(N)); heapsort is the true O(1).
#   - When to sort over set: memory-constrained / O(1) extra space required.
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return not len(set(nums)) == len(nums)
