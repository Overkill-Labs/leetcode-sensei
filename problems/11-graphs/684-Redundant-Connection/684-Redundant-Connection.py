'''
https://leetcode.com/problems/redundant-connection/
'''

last_solved     = "2026-09-25"
revisit_in_days = 1
times_reviewed  = 5
difficulty      = "medium"
topic_tags      = ["depth-first-search", "breadth-first-search", "union-find", "graph"]

class UnionFind:

    def __init__(self, size):
        self.parent = [node for node in range(size + 1)]
        self.rank = [0] * (size + 1)
    
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, src, dest):
        root_src, root_dest = self.find(src), self.find(dest)

        if root_src == root_dest:
            return
        
        if self.rank[root_src] >= self.rank[root_dest]:
            self.parent[root_dest] = root_src

            if self.rank[root_src] == self.rank[root_dest]:
                self.rank[root_src] += 1
        else:
            self.parent[root_src] = root_dest

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        union_find = UnionFind(len(edges))

        for src, dest in edges:
            if union_find.find(src) == union_find.find(dest):
                return [src, dest]
            union_find.union(src, dest)
