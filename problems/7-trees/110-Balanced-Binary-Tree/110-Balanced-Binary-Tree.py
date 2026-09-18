'''
https://leetcode.com/problems/balanced-binary-tree/
'''

last_solved     = "2026-09-17"
revisit_in_days = 90
difficulty      = "easy"
topic_tags      = ["trees"]
times_reviewed  = 8

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def depth(node):
            if not node:
                return 0
            
            left_depth, right_depth = depth(node.left), depth(node.right)

            if left_depth == -1 or right_depth == -1:
                return -1

            if abs(left_depth - right_depth) > 1:
                return -1
            
            return 1 + max(left_depth, right_depth)

        res = depth(root)

        if res == -1:
            return False
        else:
            return True