'''
https://leetcode.com/problems/non-overlapping-intervals/
'''

last_solved     = "2026-09-19"
revisit_in_days = 1
times_reviewed  = 1
difficulty      = "medium"
topic_tags      = ["array", "dynamic-programming", "greedy", "sorting"]

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        g_end = intervals[0][1]
        cnt = -1

        for start, end in intervals:
            if start < g_end:
                cnt += 1
            else:
                g_end = end

        return cnt
