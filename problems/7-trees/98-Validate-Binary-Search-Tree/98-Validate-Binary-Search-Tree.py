'''
https://leetcode.com/problems/validate-binary-search-tree/
'''

last_solved     = "2026-09-07"
revisit_in_days = 40
times_reviewed  = 8
difficulty      = "medium"
topic_tags      = ["trees", "bst"]

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, lo, hi):
            if not node:
                return True

            if lo < node.val < hi:
                return validate(node.left, lo, node.val) and validate(node.right, node.val, hi)
                
            return False
        
        return validate(root, float('-inf'), float('inf'))