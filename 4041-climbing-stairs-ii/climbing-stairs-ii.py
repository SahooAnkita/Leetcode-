class Solution:
    def climbStairs(self, n: int, costs: list[int]) -> int:
        dp = [float('inf')] * (n + 1)

        # Starting point
        dp[0] = 0

        for i in range(1, n + 1):

            # Jump from i - 1
            dp[i] = min(
                dp[i],
                dp[i - 1] + costs[i - 1] + 1
            )

            # Jump from i - 2
            if i >= 2:
                dp[i] = min(
                    dp[i],
                    dp[i - 2] + costs[i - 1] + 4
                )

            # Jump from i - 3
            if i >= 3:
                dp[i] = min(
                    dp[i],
                    dp[i - 3] + costs[i - 1] + 9
                )

        return dp[n]