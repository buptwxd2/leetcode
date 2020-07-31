# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        def height(root):
            if not root:
                return 0, True

            left_height, val = height(root.left)
            if not val:
                return -1, False
            right_height, val = height(root.right)
            if not val:
                return -1, False

            if abs(left_height - right_height) > 1:
                return -1, False

            return max(left_height, right_height) + 1, True

        if not root:
            return True

        _, val = height(root)

        return val

"""
Results:
Referred to https://www.youtube.com/watch?v=C75oWiy0bWM

"""