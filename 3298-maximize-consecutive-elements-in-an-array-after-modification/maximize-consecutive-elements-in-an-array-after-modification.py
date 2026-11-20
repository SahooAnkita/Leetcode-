class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:

        nums.sort()
        dp = {}
        answer = 0

        for num in nums:
            # Save dp[num] before updating it
            old = dp.get(num, 0)

            # Use num without increasing it
            dp[num] = max(
                dp.get(num, 0),
                dp.get(num - 1, 0) + 1
            )

            # Use num + 1
            dp[num + 1] = max(
                dp.get(num + 1, 0),
                old + 1
            )

            answer = max(answer, dp[num], dp[num + 1])

        return answer