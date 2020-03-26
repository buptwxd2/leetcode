# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None

        if root.val == key:
            if not root.left and not root.right:
                return None
            if root.left:
                root.val = root.left.val
                root
            if not root.left:
                return root.right
            if not root.right:
                return root.left

        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)

        return root




