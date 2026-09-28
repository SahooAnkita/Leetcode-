from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        queue = deque()
        fresh = 0

        # Add all rotten oranges to the queue
        # and count fresh oranges.
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 2:
                    queue.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1

        minutes = 0

        directions = [
            (-1, 0),  # up
            (1, 0),   # down
            (0, -1),  # left
            (0, 1)    # right
        ]

        # BFS
        while queue and fresh > 0:
            level_size = len(queue)

            # Process all oranges that are rotten
            # at the beginning of this minute.
            for _ in range(level_size):
                row, col = queue.popleft()

                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc

                    # Check boundaries
                    if not (0 <= new_row < m and 0 <= new_col < n):
                        continue

                    # Only fresh oranges can become rotten
                    if grid[new_row][new_col] != 1:
                        continue

                    # Make the orange rotten
                    grid[new_row][new_col] = 2
                    fresh -= 1

                    # Add it to the queue for the next minute
                    queue.append((new_row, new_col))

            minutes += 1

        # If fresh oranges remain, they cannot be reached.
        if fresh > 0:
            return -1

        return minutes