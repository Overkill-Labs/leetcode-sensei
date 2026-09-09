'''
https://leetcode.com/problems/copy-list-with-random-pointer/
'''

last_solved     = "2026-09-09"
revisit_in_days = 36
times_reviewed  = 8
difficulty      = "medium"
topic_tags      = ["linked-list", "hash-map"]

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return head

        cpy_list = Node(head.val)
        org_list = head

        lookup = {None: None}

        cpy, org = cpy_list, org_list
        while org:
            cpy.val = org.val
            lookup[org] = cpy
            if org.next:
                cpy.next = Node(-1)
            cpy, org = cpy.next, org.next

        cpy, org = cpy_list, org_list
        while org:
            cpy.random = lookup[org.random]
            cpy, org = cpy.next, org.next

        return cpy_list
        # Time:  O(N) — two passes over the list
        # Space: O(N) — lookup dict storing original -> copy mapping