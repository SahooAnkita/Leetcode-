class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result = []

        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while top <= bottom and left <= right:

            # 1. Move left -> right
            for col in range(left, right + 1):
                result.append(matrix[top][col])

            top += 1

            # 2. Move top -> bottom
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])

            right -= 1

            # 3. Move right -> left
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])

                bottom -= 1

            # 4. Move bottom -> top
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])

                left += 1

        return result