'''
https://leetcode.com/problems/linked-list-cycle/
'''

last_solved     = "2026-10-14"
revisit_in_days = 45
difficulty      = "easy"
topic_tags      = ["linked-list"]
times_reviewed  = 7

# REVISIT 2026-10-14: code was instant; needed two nudges for WHY fast meets slow.
#   - Say unprompted: inside the cycle, the gap (fast behind slow) shrinks by exactly 1 per step,
#     so it hits 0 and fast can't jump over slow.
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False
