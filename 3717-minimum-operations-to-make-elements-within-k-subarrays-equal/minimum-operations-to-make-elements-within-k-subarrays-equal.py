from typing import List


class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, value):
        while i <= self.n:
            self.bit[i] += value
            i += i & -i

    def sum(self, i):
        result = 0
        while i > 0:
            result += self.bit[i]
            i -= i & -i
        return result

    def kth(self, k):
        """
        Return the smallest index i such that
        prefix_sum(i) >= k.
        """
        idx = 0
        bit_mask = 1 << (self.n.bit_length() - 1)

        while bit_mask:
            next_idx = idx + bit_mask

            if next_idx <= self.n and self.bit[next_idx] < k:
                idx = next_idx
                k -= self.bit[next_idx]

            bit_mask >>= 1

        return idx + 1


class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)

        # ---------------------------------------------------------
        # 1. Coordinate compression
        # ---------------------------------------------------------
        values = sorted(set(nums))
        m = len(values)

        rank = {value: i + 1 for i, value in enumerate(values)}

        # Fenwick tree for frequencies
        count_bit = Fenwick(m)

        # Fenwick tree for sum of values
        sum_bit = Fenwick(m)

        def add_value(value, delta):
            r = rank[value]
            count_bit.add(r, delta)
            sum_bit.add(r, value * delta)

        # ---------------------------------------------------------
        # 2. Cost of every window of size x
        # ---------------------------------------------------------
        window_cost = [0] * (n - x + 1)

        # Initial window
        for i in range(x):
            add_value(nums[i], 1)

        def get_window_cost():
            # Median position
            median_pos = (x + 1) // 2

            median_rank = count_bit.kth(median_pos)
            median = values[median_rank - 1]

            # Number and sum of elements <= median
            left_count = count_bit.sum(median_rank)
            left_sum = sum_bit.sum(median_rank)

            # Total count and sum
            total_count = x
            total_sum = sum_bit.sum(m)

            # Cost on left side
            left_cost = median * left_count - left_sum

            # Cost on right side
            right_count = total_count - left_count
            right_sum = total_sum - left_sum

            right_cost = right_sum - median * right_count

            return left_cost + right_cost

        window_cost[0] = get_window_cost()

        # Slide the window
        for start in range(1, n - x + 1):
            # Remove outgoing element
            add_value(nums[start - 1], -1)

            # Add incoming element
            add_value(nums[start + x - 1], 1)

            window_cost[start] = get_window_cost()

        # ---------------------------------------------------------
        # 3. DP
        #
        # dp[j][i] =
        # minimum cost to choose j non-overlapping windows
        # from nums[0:i]
        # ---------------------------------------------------------

        INF = 10**30

        # dp[j][i]
        dp = [[INF] * (n + 1) for _ in range(k + 1)]

        # Choosing 0 windows costs 0
        for i in range(n + 1):
            dp[0][i] = 0

        for j in range(1, k + 1):
            for i in range(1, n + 1):

                # Don't use a window ending at i - 1
                dp[j][i] = dp[j][i - 1]

                # A window of size x ending at i - 1
                # starts at i - x.
                if i >= x:
                    start = i - x

                    # Previous j-1 windows must end
                    # at or before 'start'.
                    if dp[j - 1][start] != INF:
                        dp[j][i] = min(
                            dp[j][i],
                            dp[j - 1][start] + window_cost[start]
                        )

        return dp[k][n]