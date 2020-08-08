# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return None

        root_val = postorder[-1]
        root_idx = inorder.index(root_val)

        left_inorder = inorder[:root_idx]
        right_inorder = inorder[root_idx + 1:]

        left_len = len(left_inorder)
        left_postorder = postorder[:left_len]
        right_postorder = postorder[left_len:-1]

        left_tree = self.buildTree(left_inorder, left_postorder)
        right_tree = self.buildTree(right_inorder, right_postorder)

        root_node = TreeNode(root_val)
        root_node.left = left_tree
        root_node.right = right_tree

        return root_node

"""
Results:
Recursive way
Runtime: 204 ms, faster than 38.50% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
Memory Usage: 89.2 MB, less than 5.02% of Python3 online submissions for Construct Binary Tree from Inorder and Postorder Traversal.
"""