class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            k = left + (right - left) // 2

            hours = 0

            for pile in piles:
                hours += (pile + k - 1) // k

            if hours <= h:
                # Speed k works.
                # Try a slower speed.
                right = k
            else:
                # Speed k is too slow.
                # Need a faster speed.
                left = k + 1

        return left