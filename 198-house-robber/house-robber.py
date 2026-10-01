class Solution:
    def rob(self, nums: list[int]) -> int:
        prev2 = 0
        prev1 = 0

        for money in nums:
            rob_current = prev2 + money
            skip_current = prev1

            current = max(rob_current, skip_current)

            prev2 = prev1
            prev1 = current

        return prev1