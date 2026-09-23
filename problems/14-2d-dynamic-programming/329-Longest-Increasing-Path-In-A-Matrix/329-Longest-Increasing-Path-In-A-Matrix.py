'''
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
'''

last_solved     = "2026-09-23"
revisit_in_days = 33
times_reviewed  = 5
difficulty      = "hard"
topic_tags      = ["array", "dynamic-programming", "depth-first-search", "breadth-first-search", "graph", "topological-sort", "memoization", "matrix", "directed-acyclic-graph"]

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.M, self.N = len(matrix), len(matrix[0])
        self.DIRECTIONS = (
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        )

        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dfs(i, j):
            path_len = 1

            for i_adj, j_adj in self.DIRECTIONS:
                n_i, n_j = i + i_adj, j + j_adj

                if (
                    0 <= n_i < self.M and
                    0 <= n_j < self.N and
                    matrix[n_i][n_j] > matrix[i][j]
                ):
                    path_len = max(path_len, 1 + dfs(n_i, n_j))
            
            return path_len
        
        max_lis = 1

        for i in range(self.M):
            for j in range(self.N):
                max_lis = max(max_lis, dfs(i,j))
        
        return max_lis
        # Time:  O(M * N) — each cell computed once (with memoization)
        # Space: O(M * N) — cache keyed on (i, j) only
