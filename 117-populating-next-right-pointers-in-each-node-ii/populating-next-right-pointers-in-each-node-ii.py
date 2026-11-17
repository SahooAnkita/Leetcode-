class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None

        queue = [root]

        while queue:
            level_size = len(queue)

            for i in range(level_size):
                node = queue.pop(0)

                # Connect to the next node in the same level
                if i < level_size - 1:
                    node.next = queue[0]

                # Add children for the next level
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return root