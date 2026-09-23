'''
https://leetcode.com/problems/coin-change-ii/
'''

last_solved     = "2026-09-23"
revisit_in_days = 5
times_reviewed  = 5
difficulty      = "medium"
topic_tags      = ["array", "dynamic-programming", "knapsack-problem", "complete-knapsack"]

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for amt in range(coin, amount + 1):
                dp[amt] += dp[amt - coin]

        return dp[-1]
