'''
https://leetcode.com/problems/walls-and-gates/description/
'''

last_solved     = "2026-09-07"
revisit_in_days = 42
times_reviewed  = 8
difficulty      = "medium"
topic_tags      = ["graphs"]

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        INF = 2147483647
        M = len(rooms)
        N = len(rooms[0])

        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        queue = deque()
        for i in range(M):
            for j in range(N):
                if rooms[i][j] == 0:
                    queue.append((i, j))

        distance = 0
        while queue:
            distance += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()

                for i_adj, j_adj in DIRECTIONS:
                    n_i, n_j = i + i_adj, j + j_adj

                    if (
                        0 <= n_i < M and
                        0 <= n_j < N and
                        rooms[n_i][n_j] == INF
                    ):
                        rooms[n_i][n_j] = distance
                        queue.append((n_i, n_j))