# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None

        root_val = preorder[0]
        root = TreeNode(root_val)

        right_start_idx = 1
        while right_start_idx < len(preorder) and preorder[right_start_idx] < root_val:
            right_start_idx += 1

        left_vals = preorder[1:right_start_idx]
        right_vals = preorder[right_start_idx:]
        root.left = self.bstFromPreorder(left_vals)
        root.right = self.bstFromPreorder(right_vals)

        return root

"""
Results:
Runtime: 32 ms, faster than 91.94% of Python3 online submissions for Construct Binary Search Tree from Preorder Traversal.
Memory Usage: 14.1 MB, less than 11.69% of Python3 online submissions for Construct Binary Search Tree from Preorder Traversal.
"""