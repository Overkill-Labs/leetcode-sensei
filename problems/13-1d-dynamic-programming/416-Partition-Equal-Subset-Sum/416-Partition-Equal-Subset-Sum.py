'''
https://leetcode.com/problems/partition-equal-subset-sum/
'''

last_solved     = "2026-09-25"
revisit_in_days = 1
times_reviewed  = 4
difficulty      = "medium"
topic_tags      = ["array", "dynamic-programming", "knapsack-problem", "0-1-knapsack"]

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        S = sum(nums)
        TARGET = S // 2

        if S % 2 != 0:
            return False
        
        dp = [False] * (TARGET + 1)
        dp[0] = True

        # 0/1 knapsack: iterate backwards so each num is used at most once
        for num in nums:
            for target in range(TARGET, num-1, -1):
                dp[target] = dp[target] or dp[target - num]
        
        return dp[-1]
