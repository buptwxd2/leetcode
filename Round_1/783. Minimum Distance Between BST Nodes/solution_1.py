# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:

        def in_order(root):
            if not root:
                return []

            lefts = in_order(root.left)
            rights = in_order(root.right)

            return lefts + [root.val] + rights

        inorder = in_order(root)

        min_diff = float('inf')

        for i in range(1, len(inorder)):
            if inorder[i] - inorder[i - 1] < min_diff:
                min_diff = inorder[i] - inorder[i - 1]

        return min_diff

"""
Results:
Runtime: 28 ms, faster than 88.54% of Python3 online submissions for Minimum Distance Between BST Nodes.
Memory Usage: 14.2 MB, less than 8.99% of Python3 online submissions for Minimum Distance Between BST Nodes.
"""