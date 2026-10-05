class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        cash = 0
        hold = -prices[0]

        for price in prices:
            prev_cash = cash
            prev_hold = hold

            cash = max(
                prev_cash,
                prev_hold + price - fee
            )

            hold = max(
                prev_hold,
                prev_cash - price
            )

        return cash