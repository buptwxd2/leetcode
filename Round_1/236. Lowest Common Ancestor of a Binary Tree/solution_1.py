# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        else:
            return left or right

"""
Results:
Runtime: 104 ms, faster than 36.03% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
Memory Usage: 24.4 MB, less than 43.60% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
"""