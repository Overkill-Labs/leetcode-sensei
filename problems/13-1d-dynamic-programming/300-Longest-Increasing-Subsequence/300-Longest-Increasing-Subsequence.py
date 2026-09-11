'''
https://leetcode.com/problems/longest-increasing-subsequence/
'''

last_solved     = "2026-09-11"
revisit_in_days = 1
times_reviewed  = 1
difficulty      = "medium"
topic_tags      = ["array", "binary-search", "dynamic-programming", "longest-increasing-subsequence"]


# Approach 1: Top-Down Memoization — dfs(idx, prev_idx)
# Intuition: at each index, decide to take or skip; take only if nums[idx] > nums[prev_idx].
# NOTE: lru_cache causes MLE on LeetCode due to closure retention across test cases.
# Works correctly in isolated environments / interviews.
#
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         from functools import lru_cache
#
#         @lru_cache(maxsize=None)
#         def memo(idx, prev_idx):
#             if idx == len(nums):
#                 return 0
#             take = 0
#             if prev_idx == -1 or nums[idx] > nums[prev_idx]:
#                 take = 1 + memo(idx + 1, idx)
#             skip = memo(idx + 1, prev_idx)
#             return max(take, skip)
#
#         return memo(0, -1)
#         # Time:  O(N²) — N * N unique states
#         # Space: O(N²) — memoization cache


# Approach 2: Bottom-Up DP — dp[i] = LIS length ending at index i
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
        # Time:  O(N²) — nested loop over all (i, j) pairs
        # Space: O(N)  — dp array
