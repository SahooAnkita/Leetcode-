class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n

        while left <= right:
            mid = left + (right - left) // 2

            result = guess(mid)

            if result == 0:
                return mid

            elif result == -1:
                # mid is greater than pick
                right = mid - 1

            else:
                # mid is less than pick
                left = mid + 1

        return -1