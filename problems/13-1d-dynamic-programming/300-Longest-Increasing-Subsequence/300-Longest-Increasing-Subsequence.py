'''
https://leetcode.com/problems/longest-increasing-subsequence/
'''

last_solved     = "2026-10-04"
revisit_in_days = 1
times_reviewed  = 5
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


# REVISIT 2026-10-05: re-derive Approach 3 from scratch without looking.
#   - Explain why tails stays sorted and what tails[k] means ("smallest tail of length k+1").
#   - Hand-write the binary search (first element >= num) and handle num == existing value.
#   - State precisely: dp[i] in Approach 2 = LIS *ending at* i (not "best in prefix").
# Approach 3: Patience / Binary Search — tails[k] = smallest tail of any increasing subsequence of length k+1
# Intuition: keep [2,3] over [2,5] — smaller tails leave more room to extend.
# tails is always sorted; for each num, overwrite the first element >= num (bisect_left), or append if num beats them all.
# NOTE: tails is NOT an actual LIS (e.g. [3,4,1] -> tails=[1,4]); only len(tails) is meaningful.
#
# class Solution:
#     def lengthOfLIS(self, nums: list[int]) -> int:
#         tails = []
#
#         for num in nums:
#             if not tails or tails[-1] < num:
#                 tails.append(num)
#             elif tails[-1] > num:
#                 left, right = 0, len(tails) - 1
#
#                 while left < right:
#                     mid = (left + right) // 2
#
#                     if tails[mid] < num:
#                         left = mid + 1
#                     else:
#                         right = mid
#
#                 tails[left] = num
#
#         return len(tails)
#         # Time:  O(N log N) — binary search per element
#         # Space: O(N)       — tails array
