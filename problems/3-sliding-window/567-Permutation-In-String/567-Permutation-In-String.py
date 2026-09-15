'''
https://leetcode.com/problems/permutation-in-string/
'''

last_solved     = "2026-09-15"
revisit_in_days = 43
difficulty      = "medium"
topic_tags      = ["sliding-window", "hash-map"]
times_reviewed  = 7

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq_1 = Counter(s1)
        freq_2 = defaultdict(int)
        matches = 0

        left = 0
        for right, right_char in enumerate(s2):
            left_char = s2[left]
            freq_2[right_char] += 1

            if freq_2[right_char] == freq_1[right_char]:
                matches += 1

            if right - left + 1 > len(s1):
                if freq_2[left_char] == freq_1[left_char]:
                    matches -= 1
                freq_2[left_char] -= 1
                left += 1

            if right - left + 1 == len(s1):
                if matches == len(freq_1):
                    return True

        return False
        # Time: O(len(s2)) — O(1) per window step via matches counter
        # Space: O(26) = O(1)
