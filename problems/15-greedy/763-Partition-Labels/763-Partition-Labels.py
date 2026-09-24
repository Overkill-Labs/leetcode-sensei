'''
https://leetcode.com/problems/partition-labels/
'''

last_solved     = "2026-09-24"
revisit_in_days = 3
times_reviewed  = 2
difficulty      = "medium"
topic_tags      = ["hash-table", "two-pointers", "string", "greedy"]

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        output = []

        last_occurences = defaultdict(int)
        for i, c in enumerate(s):
            last_occurences[c] = max(last_occurences[c], i)

        start, end = 0, 0
        for i, c in enumerate(s):
            end = max(end, last_occurences[c])

            if i == end:
                output.append(end - start + 1)
                start, end = i + 1, i + 1

        return output
