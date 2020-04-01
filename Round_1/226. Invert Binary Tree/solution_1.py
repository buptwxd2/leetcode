# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        reversed_left = self.invertTree(root.left)
        reversed_right = self.invertTree(root.right)

        root.left = reversed_right
        root.right = reversed_left

        return root

"""
Results:
Runtime: 24 ms, faster than 89.65% of Python3 online submissions for Invert Binary Tree.
Memory Usage: 13.9 MB, less than 5.41% of Python3 online submissions for Invert Binary Tree.
"""