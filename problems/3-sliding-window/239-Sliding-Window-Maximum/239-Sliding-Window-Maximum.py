'''
https://leetcode.com/problems/sliding-window-maximum/
'''

last_solved     = "2026-09-21"
revisit_in_days = 5
times_reviewed  = 5
difficulty      = "hard"
topic_tags      = ["array", "queue", "sliding-window", "heap-priority-queue", "monotonic-queue", "range-minimum-maximum-query"]

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        q = deque()
        output = []

        for i, num in enumerate(nums):
            while q and nums[q[-1]] < num:
                q.pop()

            q.append(i)

            if q[0] <= i - k:
                q.popleft()

            if i >= k - 1:
                output.append(nums[q[0]])

        return output
        # Time: O(N) — each element enqueued/dequeued at most once
        # Space: O(k) auxiliary (deque) + O(N) output
