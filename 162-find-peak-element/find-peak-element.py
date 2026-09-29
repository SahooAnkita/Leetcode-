class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] < nums[mid + 1]:
                # We are going uphill.
                # A peak must exist on the right.
                left = mid + 1
            else:
                # We are going downhill.
                # A peak exists at mid or on the left.
                right = mid

        return left