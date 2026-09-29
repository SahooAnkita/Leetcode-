class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        result = []

        def backtrack(start, current, remaining):
            # Found a valid combination
            if len(current) == k:
                if remaining == 0:
                    result.append(current[:])
                return

            # Try numbers from start to 9
            for num in range(start, 10):

                # No need to continue if num is too large
                if num > remaining:
                    break

                current.append(num)

                backtrack(
                    num + 1,
                    current,
                    remaining - num
                )

                # Backtrack
                current.pop()

        backtrack(1, [], n)

        return result