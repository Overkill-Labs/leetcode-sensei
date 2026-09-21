'''
https://leetcode.com/problems/find-median-from-data-stream/
'''

last_solved     = "2026-09-21"
revisit_in_days = 2
times_reviewed  = 2
difficulty      = "hard"
topic_tags      = ["heap"]

class MedianFinder:

    def __init__(self):
        self.min_heap = [] # Upper Half
        self.max_heap = [] # Lower Half

    def addNum(self, num: int) -> None:
        if not self.min_heap or num >= self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)
        
        while len(self.min_heap) - len(self.max_heap) > 1:
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        while len(self.max_heap) > len(self.min_heap):
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

    def findMedian(self) -> float:
        if len(self.min_heap) != len(self.max_heap):
            return self.min_heap[0]
        else:
            return (self.min_heap[0] - self.max_heap[0]) / 2
