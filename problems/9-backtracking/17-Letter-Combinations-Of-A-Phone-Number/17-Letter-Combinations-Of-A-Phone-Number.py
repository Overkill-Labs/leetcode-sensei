'''
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
'''

last_solved     = "2026-09-18"
revisit_in_days = 1
times_reviewed  = 1
difficulty      = "medium"
topic_tags      = ["hash-table", "string", "backtracking"]

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        output = []

        lookup = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(idx, path):
            if idx == len(digits):
                output.append("".join(path))
                return

            for letter in lookup[digits[idx]]:
                path.append(letter)
                backtrack(idx + 1, path)
                path.pop()

        backtrack(0, [])

        return output
