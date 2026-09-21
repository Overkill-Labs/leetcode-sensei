'''
https://leetcode.com/problems/meeting-rooms-ii/
'''

last_solved     = "2026-09-21"
revisit_in_days = 2
times_reviewed  = 3
difficulty      = "medium"
topic_tags      = ["array", "two-pointers", "greedy", "sorting", "heap-priority-queue", "prefix-sum"]

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        heap = []

        for start, end in sorted(intervals):
            if heap and start >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, end)

        return len(heap)
