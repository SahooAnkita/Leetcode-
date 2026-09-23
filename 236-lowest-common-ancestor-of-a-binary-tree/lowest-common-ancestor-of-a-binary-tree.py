class Solution:
    def lowestCommonAncestor(
        self,
        root: 'TreeNode',
        p: 'TreeNode',
        q: 'TreeNode'
    ) -> 'TreeNode':

        # Base case: empty subtree
        if root is None:
            return None

        # If current node is p or q
        if root == p or root == q:
            return root

        # Search left subtree
        left = self.lowestCommonAncestor(root.left, p, q)

        # Search right subtree
        right = self.lowestCommonAncestor(root.right, p, q)

        # p and q found in different subtrees
        if left and right:
            return root

        # Return the side where p or q was found
        if left:
            return left

        return right