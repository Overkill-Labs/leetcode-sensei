'''
https://leetcode.com/problems/spiral-matrix/
'''

last_solved     = "2026-10-04"
revisit_in_days = 1
times_reviewed  = 1
difficulty      = "medium"
topic_tags      = ["array", "matrix", "simulation"]

# REVISIT 2026-10-05: implement the O(1)-extra-space version with shrinking boundaries
#   (top, bottom, left, right), no visited set. Watch the single-row / single-column leftovers.
# Approach: Direction FSM + visited set
# State s indexes DIRECTIONS (right, down, left, up); turn clockwise (s + 1) % 4 only when blocked.
# In a spiral one turn is always enough, and the loop runs exactly M * N times.
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        M, N = len(matrix), len(matrix[0])

        output = []

        DIRECTIONS = (
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0)
        )

        visited = set()

        i, j, s = 0, 0, 0
        for _ in range(M * N):
            output.append(matrix[i][j])
            visited.add((i, j))

            n_r, n_c = DIRECTIONS[s]
            n_i, n_j = i + n_r, j + n_c

            if (n_i, n_j) in visited or not (
                0 <= n_i < M and
                0 <= n_j < N
            ):
                s = (s + 1) % 4

                n_r, n_c = DIRECTIONS[s]
                n_i, n_j = i + n_r, j + n_c

            i, j = n_i, n_j

        return output
        # Time:  O(M * N) — each cell visited once
        # Space: O(M * N) — visited set
