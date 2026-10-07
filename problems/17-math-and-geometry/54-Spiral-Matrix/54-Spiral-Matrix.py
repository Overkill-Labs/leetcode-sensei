'''
https://leetcode.com/problems/spiral-matrix/
'''

last_solved     = "2026-10-07"
revisit_in_days = 1
times_reviewed  = 2
difficulty      = "medium"
topic_tags      = ["array", "matrix", "simulation"]

# Approach 1: Direction FSM + visited set
# State s indexes DIRECTIONS (right, down, left, up); turn clockwise (s + 1) % 4 only when blocked.
# In a spiral one turn is always enough, and the loop runs exactly M * N times.
#
# class Solution:
#     def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
#         M, N = len(matrix), len(matrix[0])
#
#         output = []
#
#         DIRECTIONS = (
#             (0, 1),
#             (1, 0),
#             (0, -1),
#             (-1, 0)
#         )
#
#         visited = set()
#
#         i, j, s = 0, 0, 0
#         for _ in range(M * N):
#             output.append(matrix[i][j])
#             visited.add((i, j))
#
#             n_r, n_c = DIRECTIONS[s]
#             n_i, n_j = i + n_r, j + n_c
#
#             if (n_i, n_j) in visited or not (
#                 0 <= n_i < M and
#                 0 <= n_j < N
#             ):
#                 s = (s + 1) % 4
#
#                 n_r, n_c = DIRECTIONS[s]
#                 n_i, n_j = i + n_r, j + n_c
#
#             i, j = n_i, n_j
#
#         return output
#         # Time:  O(M * N) — each cell visited once
#         # Space: O(M * N) — visited set


# REVISIT 2026-10-07: write Approach 2 from memory — needed the wall table fully revealed today.
#   - Derive the table yourself: finishing direction s shrinks the row/column just completed.
#   - Explain why no single-row / single-column guards are needed (loop runs exactly M * N times).
#   - Know the textbook four-loop layer version too (needs top <= bottom / left <= right guards).
# Approach 2: Direction FSM + shrinking walls (O(1) extra space)
# Walls bound the unvisited region; anything outside is off-grid or already visited.
# On a turn, the wall for the row/column just finished moves inward:
#   right -> top += 1, down -> right -= 1, left -> bottom -= 1, up -> left += 1
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        output = []

        M, N = len(matrix), len(matrix[0])

        top, bottom, left, right = 0, M - 1, 0, N - 1

        DIR = (
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0)
        )

        i, j, s = 0, 0, 0
        for _ in range(M * N):
            output.append(matrix[i][j])

            r, c = DIR[s]
            n_i, n_j = i + r, j + c

            if not (
                top <= n_i <= bottom and
                left <= n_j <= right
            ):
                if s == 0:   top += 1
                elif s == 1: right -= 1
                elif s == 2: bottom -= 1
                else:        left += 1

                s = (s + 1) % 4

                r, c = DIR[s]
                n_i, n_j = i + r, j + c

            i, j = n_i, n_j

        return output
        # Time:  O(M * N) — each cell visited once
        # Space: O(1)     — four walls, excluding output
