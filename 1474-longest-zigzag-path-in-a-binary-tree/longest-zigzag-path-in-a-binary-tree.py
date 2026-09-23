class Solution:
    def longestZigZag(self, root: TreeNode | None) -> int:

        max_length = 0

        def dfs(node):
            nonlocal max_length

            if node is None:
                return -1, -1

            left_len_left, left_len_right = dfs(node.left)
            right_len_left, right_len_right = dfs(node.right)

            # If we move LEFT from current node,
            # the next move must be RIGHT.
            left = left_len_right + 1

            # If we move RIGHT from current node,
            # the next move must be LEFT.
            right = right_len_left + 1

            max_length = max(max_length, left, right)

            return left, right

        dfs(root)

        return max_length