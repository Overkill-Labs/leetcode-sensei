'''
https://leetcode.com/problems/reconstruct-itinerary/
'''

last_solved     = "2026-09-09"
revisit_in_days = 3
times_reviewed  = 2
difficulty      = "hard"
topic_tags      = ["array", "string", "depth-first-search", "graph", "sorting", "heap-priority-queue", "eulerian-circuit", "eulerian-path", "semi-eulerian-graph"]

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        heap = defaultdict(list)

        for src, dest in tickets:
            heapq.heappush(heap[src], dest)

        res = []

        def dfs(airport):
            while heap[airport]:
                nxt = heapq.heappop(heap[airport])
                dfs(nxt)
            res.append(airport)

        dfs("JFK")

        return res[::-1]
        # Time: O(E log E) — heap push/pop per edge
        # Space: O(E) — heap + recursion stack
