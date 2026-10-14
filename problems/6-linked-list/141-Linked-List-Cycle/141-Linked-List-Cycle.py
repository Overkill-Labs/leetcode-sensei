'''
https://leetcode.com/problems/linked-list-cycle/
'''

last_solved     = "2026-10-14"
revisit_in_days = 14
difficulty      = "easy"
topic_tags      = ["linked-list"]
times_reviewed  = 6

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False
