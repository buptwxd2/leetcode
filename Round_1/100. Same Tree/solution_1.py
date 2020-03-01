# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None or q is None:
            return p == q

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


"""
Results:
Runtime: 28 ms, faster than 69.74% of Python3 online submissions for Same Tree.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Same Tree.
"""