# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None

        root_val = preorder[0]

        root_idx = inorder.index(root_val)

        left_inorder = inorder[:root_idx]
        right_inorder = inorder[root_idx + 1:]

        left_len = len(left_inorder)

        left_preorder = preorder[1:1 + left_len]
        right_preorder = preorder[1 + left_len:]

        left_tree = self.buildTree(left_preorder, left_inorder)
        right_tree = self.buildTree(right_preorder, right_inorder)

        root_node = TreeNode(root_val)
        root_node.left = left_tree
        root_node.right = right_tree

        return root_node


"""
Results:
Use Recursive way
Runtime: 224 ms, faster than 33.30% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
Memory Usage: 89.3 MB, less than 5.02% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
"""