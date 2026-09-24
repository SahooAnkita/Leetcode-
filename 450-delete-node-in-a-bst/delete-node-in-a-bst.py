class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:

        # Node not found / empty tree
        if root is None:
            return None

        # Search in the left subtree
        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        # Search in the right subtree
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        # Node found
        else:

            # Case 1: No left child
            if root.left is None:
                return root.right

            # Case 2: No right child
            if root.right is None:
                return root.left

            # Case 3: Two children
            # Find the smallest node in the right subtree
            successor = root.right

            while successor.left:
                successor = successor.left

            # Replace current node's value
            root.val = successor.val

            # Delete the successor
            root.right = self.deleteNode(root.right, successor.val)

        return root