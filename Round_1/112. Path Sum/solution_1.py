# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right:
            return root.val == sum

        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)


"""
Results:
Runtime: 48 ms, faster than 14.02% of Python3 online submissions for Path Sum.
Memory Usage: 15.6 MB, less than 5.45% of Python3 online submissions for Path Sum.
"""