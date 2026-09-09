'''
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
'''

last_solved     = "2026-09-09"
revisit_in_days = 45
difficulty      = "medium"
topic_tags      = ["binary-search"]
times_reviewed  = 7

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1

        return nums[left]
        # Time:  O(log N)
        # Space: O(1)
