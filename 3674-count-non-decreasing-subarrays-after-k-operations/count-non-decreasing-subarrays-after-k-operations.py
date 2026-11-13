from collections import deque

class Solution:
    def countNonDecreasingSubarrays(self, nums: list[int], k: int) -> int:
        n = len(nums)

        dq = deque()
        cost = 0
        ans = 0

        j = n - 1

        for i in range(n - 1, -1, -1):
            num = nums[i]

            # Merge smaller groups into the current larger value
            while dq and nums[dq[-1]] < num:
                left = dq.pop()

                right = dq[-1] if dq else j + 1

                cost += (right - left) * (num - nums[left])

            dq.append(i)

            # Shrink the window if cost exceeds k
            while cost > k:
                cost -= nums[dq[0]] - nums[j]

                if dq[0] == j:
                    dq.popleft()

                j -= 1

            # All subarrays [i..i], [i..i+1], ..., [i..j] are valid
            ans += j - i + 1

        return ans