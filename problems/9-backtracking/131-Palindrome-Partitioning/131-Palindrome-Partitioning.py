'''
https://leetcode.com/problems/palindrome-partitioning/description/
'''

last_solved     = "2026-09-25"
revisit_in_days = 7
times_reviewed  = 3
difficulty      = "medium"
topic_tags      = ["backtracking", "recursion"]

class Solution:
    def partition(self, s: str) -> list[list[str]]:
        output = []
        
        def backtrack(i, path):
            if i == len(s):
                output.append(list(path))
                return
            
            for j in range(i, len(s)):
                piece = s[i:j+1]

                if piece == piece[::-1]:
                    path.append(piece)
                    backtrack(j+1,path)
                    path.pop()
        
        backtrack(0, [])

        return output
