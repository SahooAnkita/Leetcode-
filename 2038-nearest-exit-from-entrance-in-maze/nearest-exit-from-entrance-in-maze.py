from collections import deque

class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:

        m = len(maze)
        n = len(maze[0])

        queue = deque()
        queue.append((entrance[0], entrance[1], 0))

        # Mark entrance as visited
        maze[entrance[0]][entrance[1]] = '+'

        directions = [
            (-1, 0),  # up
            (1, 0),   # down
            (0, -1),  # left
            (0, 1)    # right
        ]

        while queue:
            row, col, steps = queue.popleft()

            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                # Check boundaries
                if not (0 <= new_row < m and 0 <= new_col < n):
                    continue

                # Can't move through walls or visited cells
                if maze[new_row][new_col] == '+':
                    continue

                # We found an exit
                if (
                    new_row == 0
                    or new_row == m - 1
                    or new_col == 0
                    or new_col == n - 1
                ):
                    return steps + 1

                # Mark as visited and add to queue
                maze[new_row][new_col] = '+'
                queue.append((new_row, new_col, steps + 1))

        return -1