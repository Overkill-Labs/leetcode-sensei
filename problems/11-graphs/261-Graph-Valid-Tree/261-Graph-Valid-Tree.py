'''
https://leetcode.com/problems/graph-valid-tree/
'''

last_solved     = "2026-09-09"
revisit_in_days = 3
times_reviewed  = 2
difficulty      = "medium"
topic_tags      = ["depth-first-search", "breadth-first-search", "union-find", "graph"]

class UnionFind:

    def __init__(self, size):
        self.parent = [node for node in range(size)]

    def find(self, node):
        if node != self.parent[node]:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, src, dest):
        self.parent[self.find(dest)] = self.find(src)


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        union_find = UnionFind(n)

        for src, dest in edges:
            if union_find.find(src) == union_find.find(dest):
                return False

            union_find.union(src, dest)

        for node in range(n):
            union_find.find(node)

        return len(set(union_find.parent)) == 1
        # Time: O((N + E) log N) — path compression without rank
        # Space: O(N)
