# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        if root.left is None and root.right is None:
            return 1

        if not root.left:
            return self.maxDepth(root.right) + 1

        if not root.right:
            return self.maxDepth(root.left) + 1

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
