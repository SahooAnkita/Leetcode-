class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        # Path length must be even
        if (m + n - 1) % 2 == 1:
            return False

        # A valid string cannot start with ')'
        if grid[0][0] == ')':
            return False

        # A valid string cannot end with '('
        if grid[m - 1][n - 1] == '(':
            return False

        # dp[col] = set of possible balances
        # for the current row.
        dp = [set() for _ in range(n)]

        for row in range(m):
            for col in range(n):

                # Calculate balance contributed by current cell
                if grid[row][col] == '(':
                    change = 1
                else:
                    change = -1

                if row == 0 and col == 0:
                    dp[col].add(1)
                    continue

                current_balances = set()

                # From top
                if row > 0:
                    current_balances.update(dp[col])

                # From left
                if col > 0:
                    current_balances.update(dp[col - 1])

                # Calculate new balances
                new_balances = set()

                for balance in current_balances:
                    new_balance = balance + change

                    # Balance can never become negative
                    if new_balance >= 0:
                        new_balances.add(new_balance)

                dp[col] = new_balances

        # At the destination, balance must be exactly 0
        return 0 in dp[n - 1]