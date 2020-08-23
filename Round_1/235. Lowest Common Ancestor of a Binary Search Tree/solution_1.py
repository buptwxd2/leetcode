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

        min_val, max_val = min(p.val, q.val), max(p.val, q.val)

        if root.val > max_val:
            return self.lowestCommonAncestor(root.left, p, q)

        if root.val < min_val:
            return self.lowestCommonAncestor(root.right, p, q)

        if root.val >= min_val and root.val <= max_val:
            return root
