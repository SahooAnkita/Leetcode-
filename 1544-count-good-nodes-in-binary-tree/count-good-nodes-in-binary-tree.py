class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, max_value):
            if node is None:
                return 0

            count = 0

            # Current node is good
            if node.val >= max_value:
                count = 1
                max_value = node.val

            count += dfs(node.left, max_value)
            count += dfs(node.right, max_value)

            return count

        return dfs(root, root.val)