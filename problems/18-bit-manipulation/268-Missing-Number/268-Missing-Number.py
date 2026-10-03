'''
https://leetcode.com/problems/missing-number/
'''

last_solved     = "2026-10-02"
revisit_in_days = 30
times_reviewed  = 4
difficulty      = "easy"
topic_tags      = ["array", "hash-table", "math", "binary-search", "bit-manipulation", "sorting"]

'''
Gauss Sum Solution
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return (len(nums) * (len(nums) + 1) // 2) - sum(nums)

'''
XOR Solution — every index 0..n-1 and every value pair up and cancel (a ^ a = 0);
the final ^ len(nums) supplies n, leaving only the missing number.
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        val = 0

        for idx in range(0, len(nums)):
            val = val ^ idx ^ nums[idx]
        
        val = val ^ len(nums)

        return val
