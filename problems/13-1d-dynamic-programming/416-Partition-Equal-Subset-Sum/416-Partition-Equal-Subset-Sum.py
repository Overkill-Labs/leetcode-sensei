'''
https://leetcode.com/problems/partition-equal-subset-sum/
'''

last_solved     = "2026-09-18"
revisit_in_days = 7
times_reviewed  = 3
difficulty      = "medium"
topic_tags      = ["array", "dynamic-programming", "knapsack-problem", "0-1-knapsack"]

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        self.S = sum(nums)

        if self.S % 2 != 0:
            return False
        
        from functools import lru_cache
        
        @lru_cache(maxsize=None)
        def backtrack(idx, curr):
            if idx == len(nums):
                if curr == (self.S // 2):
                    return True
                return False
            
            return backtrack(idx + 1, curr + nums[idx]) or backtrack(idx + 1, curr)
        
        return backtrack(0, 0)
