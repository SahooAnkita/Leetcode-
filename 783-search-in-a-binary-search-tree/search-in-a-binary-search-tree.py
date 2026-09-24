class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:

        if root is None:
            return None

        if root.val == val:
            return root

        if val < root.val:
            return self.searchBST(root.left, val)

        return self.searchBST(root.right, val)