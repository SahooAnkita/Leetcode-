class Solution:
    def successfulPairs(
        self,
        spells: list[int],
        potions: list[int],
        success: int
    ) -> list[int]:

        potions.sort()

        m = len(potions)
        result = []

        for spell in spells:

            left = 0
            right = m - 1
            first = m

            while left <= right:
                mid = left + (right - left) // 2

                if spell * potions[mid] >= success:
                    # This potion works.
                    # Try to find an even smaller working potion.
                    first = mid
                    right = mid - 1
                else:
                    # Potion is too weak.
                    left = mid + 1

            # All potions from first to the end work.
            result.append(m - first)

        return result