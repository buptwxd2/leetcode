# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        def foo(root):
            if not root.left and not root.right:
                return 1, root.val

            if not root.left and root.right:
                depth, val = foo(root.right)
                return depth + 1, val

            if root.left and not root.right:
                depth, val = foo(root.left)
                return depth + 1, val

            if root.left and root.right:
                left_d, left_val = foo(root.left)
                right_d, right_val = foo(root.right)
                if left_d < right_d:
                    return right_d + 1, right_val
                if left_d >= right_d:
                    return left_d + 1, left_val

        _, val = foo(root)

        return val

"""
Results:
递归
Runtime: 52 ms, faster than 26.63% of Python3 online submissions for Find Bottom Left Tree Value.
Memory Usage: 16.7 MB, less than 9.29% of Python3 online submissions for Find Bottom Left Tree Value.
"""