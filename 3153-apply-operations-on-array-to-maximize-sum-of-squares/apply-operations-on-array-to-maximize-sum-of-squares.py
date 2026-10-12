from typing import List

class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7

        # Count how many numbers contain each bit
        bit_count = [0] * 31

        for num in nums:
            for bit in range(31):
                if num & (1 << bit):
                    bit_count[bit] += 1

        # Build the k largest possible numbers
        result = [0] * k

        for bit in range(31):
            count = bit_count[bit]

            # Put this bit into the first 'count' numbers
            for i in range(min(count, k)):
                result[i] |= (1 << bit)

        # Calculate sum of squares
        answer = 0

        for num in result:
            answer = (answer + num * num) % MOD

        return answer