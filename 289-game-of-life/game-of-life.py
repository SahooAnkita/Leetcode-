class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows = len(board)
        cols = len(board[0])

        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        for r in range(rows):
            for c in range(cols):

                live_neighbors = 0

                # Count live neighbors
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < rows and 0 <= nc < cols:
                        # 1 = originally live
                        # 2 = originally live but will die
                        if board[nr][nc] == 1 or board[nr][nc] == 2:
                            live_neighbors += 1

                # Current cell is alive
                if board[r][c] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[r][c] = 2

                # Current cell is dead
                elif board[r][c] == 0:
                    if live_neighbors == 3:
                        board[r][c] = 3

        # Convert temporary states to final states
        for r in range(rows):
            for c in range(cols):

                if board[r][c] == 2:
                    board[r][c] = 0

                elif board[r][c] == 3:
                    board[r][c] = 1