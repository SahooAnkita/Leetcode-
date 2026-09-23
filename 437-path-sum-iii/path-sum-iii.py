class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:

        prefix_sum = {0: 1}

        def dfs(node, current_sum):
            if node is None:
                return 0

            current_sum += node.val

            count = prefix_sum.get(current_sum - targetSum, 0)

            prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1

            count += dfs(node.left, current_sum)
            count += dfs(node.right, current_sum)

            prefix_sum[current_sum] -= 1

            return count

        return dfs(root, 0)