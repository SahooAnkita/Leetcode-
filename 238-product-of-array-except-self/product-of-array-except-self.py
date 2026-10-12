class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        # answer[i] = product of nums[0..i-1]
        prefix = 1

        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        # multiply in product of nums[i+1..n-1]
        suffix = 1

        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer