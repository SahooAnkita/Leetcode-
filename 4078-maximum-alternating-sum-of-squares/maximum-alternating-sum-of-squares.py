from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=lambda x: x * x, reverse=True)

        positive_count = (len(nums) + 1) // 2

        score = 0

        for i, num in enumerate(nums):
            square = num * num

            if i < positive_count:
                score += square
            else:
                score -= square

        return score