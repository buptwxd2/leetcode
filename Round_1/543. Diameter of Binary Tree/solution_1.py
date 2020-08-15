# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        ans = 0

        def get_height(root):
            nonlocal ans

            if not root:
                return -1

            if not root.left and not root.right:
                return 0

            l = get_height(root.left)
            r = get_height(root.right)
            ans = max(ans, l + r + 2)

            depth = max(l, r) + 1

            return depth

        get_height(root)

        return ans

"""
Result
Runtime: 40 ms, faster than 94.21% of Python3 online submissions for Diameter of Binary Tree.
Memory Usage: 15.9 MB, less than 43.86% of Python3 online submissions for Diameter of Binary Tree.
"""