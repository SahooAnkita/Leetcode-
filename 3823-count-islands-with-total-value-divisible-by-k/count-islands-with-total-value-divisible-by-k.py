from typing import List

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])

        count = 0

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        for i in range(m):
            for j in range(n):

                if grid[i][j] == 0:
                    continue

                queue = [(i, j)]

                # Save the starting cell's value
                island_sum = grid[i][j]

                # Mark as visited
                grid[i][j] = 0

                index = 0

                while index < len(queue):
                    row, col = queue[index]
                    index += 1

                    for dr, dc in directions:
                        new_row = row + dr
                        new_col = col + dc

                        if (
                            0 <= new_row < m
                            and 0 <= new_col < n
                            and grid[new_row][new_col] > 0
                        ):
                            island_sum += grid[new_row][new_col]

                            queue.append((new_row, new_col))

                            # Mark visited
                            grid[new_row][new_col] = 0

                if island_sum % k == 0:
                    count += 1

        return count