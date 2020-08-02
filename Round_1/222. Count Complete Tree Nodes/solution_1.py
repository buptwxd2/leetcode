# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        left_nodes = self.countNodes(root.left)
        right_nodes = self.countNodes(root.right)

        return left_nodes + right_nodes + 1

"""
Results:
Recursive way
Runtime: 96 ms, faster than 44.82% of Python3 online submissions for Count Complete Tree Nodes.
Memory Usage: 21.3 MB, less than 17.06% of Python3 online submissions for Count Complete Tree Nodes.
"""