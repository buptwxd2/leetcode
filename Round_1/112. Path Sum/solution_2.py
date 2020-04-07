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

        stack = list()
        stack.append([root, sum])

        while stack:
            node, _sum = stack.pop(-1)
            if not node.left and not node.right and node.val == _sum:
                return True

            if node.left:
                stack.append([node.left, _sum - node.val])
            if node.right:
                stack.append([node.right, _sum - node.val])

        return False


"""
Results:
Runtime: 40 ms, faster than 79.56% of Python3 online submissions for Path Sum.
Memory Usage: 15.5 MB, less than 5.45% of Python3 online submissions for Path Sum.
"""