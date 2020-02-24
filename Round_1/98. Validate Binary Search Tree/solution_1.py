# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, lower=float("-inf"), upper=float('inf')):
            if root is None:
                return True

            if root.left is None and root.right is None:
                return True

            if root.left is None and root.right:
                return root.val < root.right.val and self.isValidBST(root.right)

            if root.right is None and root.left:
                return root.val > root.left.val and self.isValidBST(root.left)

            # else left and right both non-empty
            if root.left.val < root.val < root.right.val:
                return self.isValidBST(root.left) and self.isValidBST(root.right)
            else:
                return False


"""
Results:
这个结果是错的，因为这个算法只能保证某科子树是BST，但不能保证整个这棵是BST，
See https://leetcode.com/problems/validate-binary-search-tree/solution/里的Intution部分
"""