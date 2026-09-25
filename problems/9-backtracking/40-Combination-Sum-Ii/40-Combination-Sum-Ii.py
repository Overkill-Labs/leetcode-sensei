'''
https://leetcode.com/problems/combination-sum-ii/
'''

last_solved     = "2026-09-25"
revisit_in_days = 45
times_reviewed  = 9
difficulty      = "medium"
topic_tags      = ["backtracking", "recursion"]

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []

        candidates.sort()

        def backtrack(idx, curr_arr, curr_sum):
            if curr_sum >= target or idx >= len(candidates):
                if curr_sum == target:
                    output.append(list(curr_arr))
                return
            
            curr_arr.append(candidates[idx])
            curr_sum += candidates[idx]
            backtrack(idx+1, curr_arr, curr_sum)
            curr_sum -= curr_arr.pop()

            while idx < len(candidates) - 1 and candidates[idx] == candidates[idx + 1]:
                idx += 1
            
            backtrack(idx+1, curr_arr, curr_sum)
        
        backtrack(0, [], 0)

        return output
