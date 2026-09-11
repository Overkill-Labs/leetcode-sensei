'''
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
'''

last_solved     = "2026-09-11"
revisit_in_days = 7
times_reviewed  = 3
difficulty      = "medium"
topic_tags      = ["depth-first-search", "breadth-first-search", "union-find", "graph"]

class UnionFind:

    def __init__(self, size):
        self.parent = [node for node in range(size)]

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, src, dest):
        self.parent[self.find(dest)] = self.find(src)


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        union_find = UnionFind(n)

        for src, dest in edges:
            union_find.union(src, dest)

        for node in range(n):
            union_find.find(node)

        return len(set(union_find.parent))
        # Time: O((N + E) log N) — path compression without rank
        # Space: O(N)
