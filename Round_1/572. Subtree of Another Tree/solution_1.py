# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        def is_same_tree(p, q):
            if not p or not q:
                return p is None and q is None

            return p.val == q.val and is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

        if not s or not t:
            return s is None and t is None

        if is_same_tree(s, t):
            return True
        else:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

"""
Results:
Recursive way
Runtime: 240 ms, faster than 74.23% of Python3 online submissions for Subtree of Another Tree.
Memory Usage: 15 MB, less than 23.38% of Python3 online submissions for Subtree of Another Tree.
"""