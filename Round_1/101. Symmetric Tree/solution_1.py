# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True

        return self.left_is_equal_to_right(root.left, root.right)

    def left_is_equal_to_right(self, left, right):
        if left is None or right is None:
            return left == right

        if left.val != right.val:
            return False

        return self.left_is_equal_to_right(left.left, right.right) and self.left_is_equal_to_right(left.right,
                                                                                                   right.left)


"""
Results:
Runtime: 28 ms, faster than 89.61% of Python3 online submissions for Symmetric Tree.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Symmetric Tree.
"""
