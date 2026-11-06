from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        required = Counter(t)

        window = {}

        have = 0
        need = len(required)

        left = 0

        min_length = float("inf")
        min_left = 0

        for right in range(len(s)):
            char = s[right]

            window[char] = window.get(char, 0) + 1

            # Character has reached its required frequency
            if char in required and window[char] == required[char]:
                have += 1

            # Current window contains all required characters
            while have == need:
                # Update minimum window
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    min_left = left

                # Remove left character
                left_char = s[left]
                window[left_char] -= 1

                # Window is no longer valid
                if left_char in required and window[left_char] < required[left_char]:
                    have -= 1

                left += 1

        if min_length == float("inf"):
            return ""

        return s[min_left:min_left + min_length]