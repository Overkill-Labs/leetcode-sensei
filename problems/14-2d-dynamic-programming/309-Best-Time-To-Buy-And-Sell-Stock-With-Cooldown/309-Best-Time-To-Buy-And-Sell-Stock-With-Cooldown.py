'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
'''

last_solved     = "2026-09-09"
revisit_in_days = 30
times_reviewed  = 4
difficulty      = "medium"
topic_tags      = ["array", "dynamic-programming"]

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold, sold, cold = -prices[0], float('-inf'), 0

        for price in prices:
            p_hold, p_sold, p_cold = hold, sold, cold

            hold = max(p_hold, p_cold - price)
            sold = p_hold + price
            cold = max(p_sold, p_cold)

        return max(sold, cold)
        # Time:  O(N)
        # Space: O(1)
