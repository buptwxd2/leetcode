# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        if not root.left and root.right:
            return self.minDepth(root.right) + 1

        if not root.right and root.left:
            return self.minDepth(root.left) + 1

        if root.right and root.left:
            return min(self.minDepth(root.left) + 1, self.minDepth(root.right) + 1)


"""
Results:
Runtime: 44 ms, faster than 61.13% of Python3 online submissions for Minimum Depth of Binary Tree.
Memory Usage: 15.5 MB, less than 51.35% of Python3 online submissions for Minimum Depth of Binary Tree.
"""