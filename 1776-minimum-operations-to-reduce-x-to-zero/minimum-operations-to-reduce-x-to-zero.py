class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x
        n = len(nums)

        # We need to keep a subarray with sum = target
        if target < 0:
            return -1

        if target == 0:
            return n

        left = 0
        current_sum = 0
        max_length = -1

        for right in range(n):
            current_sum += nums[right]

            # Shrink window if sum becomes too large
            while left <= right and current_sum > target:
                current_sum -= nums[left]
                left += 1

            # Found a valid subarray
            if current_sum == target:
                max_length = max(max_length, right - left + 1)

        if max_length == -1:
            return -1

        return n - max_length