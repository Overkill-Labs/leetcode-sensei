'''
https://leetcode.com/problems/redundant-connection/
'''

last_solved     = "2026-09-07"
revisit_in_days = 3
times_reviewed  = 2
difficulty      = "medium"
topic_tags      = ["depth-first-search", "breadth-first-search", "union-find", "graph"]

class UnionFind:

    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]

    def find(self, n):
        if self.parent[n] != n:
            self.parent[n] = self.find(self.parent[n])
        return self.parent[n]

    def union(self, src, dest):
        self.parent[self.find(dest)] = self.find(src)

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        union_find = UnionFind(len(edges))

        for src, dest in edges:
            if union_find.find(src) == union_find.find(dest):
                return [src, dest]

            union_find.union(src, dest)

        return []
