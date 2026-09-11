'''
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
'''

last_solved     = "2026-09-10"
revisit_in_days = 3
times_reviewed  = 2
difficulty      = "hard"
topic_tags      = ["array", "dynamic-programming", "depth-first-search", "breadth-first-search", "graph", "topological-sort", "memoization", "matrix", "directed-acyclic-graph"]

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.M, self.N = len(matrix), len(matrix[0])
        DIRECTIONS = (
            (1, 0),
            (-1, 0),
            (0, -1),
            (0, 1)
        )

        from functools import lru_cache

        @lru_cache(maxsize=None)
        def lis(i, j):
            lis_arr = [1]
            for i_adj, j_adj in DIRECTIONS:
                n_i, n_j = i + i_adj, j + j_adj

                if (
                    0 <= n_i < self.M and
                    0 <= n_j < self.N and
                    matrix[n_i][n_j] > matrix[i][j]
                ):
                    lis_arr.append(1 + lis(n_i, n_j))

            return max(lis_arr)

        max_len = 1

        for i in range(self.M):
            for j in range(self.N):
                max_len = max(max_len, lis(i, j))

        return max_len
        # Time:  O(M * N) — each cell computed once (with memoization)
        # Space: O(M * N) — cache keyed on (i, j) only
