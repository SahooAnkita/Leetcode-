class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # If only one row, no zigzag is possible
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows

        current_row = 0
        direction = 1  # 1 = down, -1 = up

        for char in s:
            rows[current_row] += char

            # Change direction at top and bottom
            if current_row == 0:
                direction = 1
            elif current_row == numRows - 1:
                direction = -1

            current_row += direction

        return "".join(rows)