# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def helper(preorder, inorder):
            if not preorder:
                return None

            root_val = preorder[0]
            root = TreeNode(root_val)

            inorder_idx = inorder.index(root_val)
            left_inorder = inorder[:inorder_idx]
            right_inorder = inorder[inorder_idx + 1:]

            left_len = len(left_inorder)
            left_preorder = preorder[1:1 + left_len]
            right_preorder = preorder[1 + left_len:]

            root.left = helper(left_preorder, left_inorder)
            root.right = helper(right_preorder, right_inorder)

            return root

        inorder = sorted(preorder)

        return helper(preorder, inorder)

"""
Results:
Runtime: 24 ms, faster than 99.69% of Python3 online submissions for Construct Binary Search Tree from Preorder Traversal.
Memory Usage: 14.3 MB, less than 5.04% of Python3 online submissions for Construct Binary Search Tree from Preorder Traversal.
"""