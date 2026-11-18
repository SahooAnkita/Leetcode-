from collections import deque

class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:

        queue = deque([root])
        result = []

        while queue:
            level_size = len(queue)
            level_sum = 0

            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(level_sum / level_size)

        return result