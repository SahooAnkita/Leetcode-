class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = 10**9

        # cost[i][j] = minimum changes needed to make s[i:j+1]
        # a semi-palindrome
        cost = [[INF] * n for _ in range(n)]

        # Precompute costs for every substring
        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1

                # Try every proper divisor d of length
                for d in range(1, length):
                    if length % d != 0:
                        continue

                    changes = 0
                    group_size = length // d

                    # There are d groups
                    for start in range(d):
                        left = 0
                        right = group_size - 1

                        while left < right:
                            pos1 = i + start + left * d
                            pos2 = i + start + right * d

                            if s[pos1] != s[pos2]:
                                changes += 1

                            left += 1
                            right -= 1

                    cost[i][j] = min(cost[i][j], changes)

        # dp[g][i] = minimum changes to divide s[0:i]
        # into exactly g semi-palindromic substrings
        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0

        for groups in range(1, k + 1):
            for end in range(2 * groups, n + 1):
                # Last substring starts at start
                # Every substring must have length >= 2
                for start in range(2 * (groups - 1), end - 1):
                    if dp[groups - 1][start] == INF:
                        continue

                    current_cost = cost[start][end - 1]

                    if current_cost != INF:
                        dp[groups][end] = min(
                            dp[groups][end],
                            dp[groups - 1][start] + current_cost
                        )

        return dp[k][n]