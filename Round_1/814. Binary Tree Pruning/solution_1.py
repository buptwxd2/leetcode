# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:

        def containsOne(node):
            if not node:
                return False

            a1 = containsOne(node.left)
            a2 = containsOne(node.right)

            if not a1:
                node.left = None

            if not a2:
                node.right = None

            return node.val == 1 or a1 or a2

        return root if containsOne(root) else None
