'''
https://leetcode.com/problems/hand-of-straights/
'''

last_solved     = "2026-09-15"
revisit_in_days = 30
times_reviewed  = 4
difficulty      = "medium"
topic_tags      = ["array", "hash-table", "greedy", "sorting"]

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hand_counter = Counter(hand)
        hand_keys = sorted(hand_counter.keys())

        for key in hand_keys:
            cnt = hand_counter[key]

            while cnt:
                for i in range(groupSize):
                    if hand_counter[key + i] < cnt:
                        return False
                    hand_counter[key + i] -= 1
                cnt -= 1

        return True
        # Time: O(N log K) — sort over unique keys K, then O(N) traversal
        # Space: O(N)
