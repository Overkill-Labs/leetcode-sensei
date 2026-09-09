'''
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
'''

last_solved     = "2026-09-09"
revisit_in_days = 1
times_reviewed  = 1
difficulty      = "hard"
topic_tags      = ["array", "dynamic-programming", "depth-first-search", "breadth-first-search", "graph", "topological-sort", "memoization", "matrix", "directed-acyclic-graph"]

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.M, self.N = len(matrix), len(matrix[0])

        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dfs(prev, i, j):
            if not (
                0 <= i < self.M and
                0 <= j < self.N and
                matrix[i][j] > prev
            ):
                return 0

            return 1 + max(
                dfs(matrix[i][j], i + 1, j),
                dfs(matrix[i][j], i - 1, j),
                dfs(matrix[i][j], i, j + 1),
                dfs(matrix[i][j], i, j - 1)
            )

        longest = 1

        for i in range(self.M):
            for j in range(self.N):
                longest = max(longest, dfs(float('-inf'), i, j))

        return longest
        # Time:  O(M * N) — each cell computed once (with memoization)
        # Space: O(M^2 * N^2) — cache keyed on (prev, i, j); prev has M*N possible values
