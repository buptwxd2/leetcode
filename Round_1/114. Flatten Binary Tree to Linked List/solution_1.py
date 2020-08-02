# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        if not root:
            return

        if not root.left and not root.right:
            return

        # flattern left
        self.flatten(root.left)

        # flattern right
        self.flatten(root.right)

        left_root = root.left
        right_root = root.right

        if not left_root:
            return
        else:
            p = left_root
            while p.right:
                p = p.right

            p.right = right_root
            root.right = left_root
            root.left = None

            return

"""
Results:
Recursive way
Runtime: 32 ms, faster than 94.92% of Python3 online submissions for Flatten Binary Tree to Linked List.
Memory Usage: 14.6 MB, less than 26.98% of Python3 online submissions for Flatten Binary Tree to Linked List.
"""