# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:

        def in_order(root):
            if not root:
                return []

            lefts = in_order(root.left)
            rights = in_order(root.right)
            return lefts + [root.val] + rights

        inorder = in_order(root)

        min_abs_diff = float('inf')

        for i in range(1, len(inorder)):
            diff = inorder[i] - inorder[i - 1]
            if diff < min_abs_diff:
                min_abs_diff = diff

        return min_abs_diff

"""
Results:
Runtime: 56 ms, faster than 79.98% of Python3 online submissions for Minimum Absolute Difference in BST.
Memory Usage: 16 MB, less than 22.32% of Python3 online submissions for Minimum Absolute Difference in BST.
"""