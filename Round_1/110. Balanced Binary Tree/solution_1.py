# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        def get_tree_depth(root):
            if not root:
                return 0

            return max(get_tree_depth(root.left), get_tree_depth(root.right)) + 1

        if not root:
            return True

        left_height = get_tree_depth(root.left)
        right_height = get_tree_depth(root.right)

        return abs(left_height - right_height) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)