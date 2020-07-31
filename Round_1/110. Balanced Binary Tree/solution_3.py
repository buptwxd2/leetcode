# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        def get_tree_depth(root):
            nonlocal heights

            if not root:
                return 0

            if root not in heights:
                heights[root] = max(get_tree_depth(root.left), get_tree_depth(root.right)) + 1

            return heights[root]

        if not root:
            return True

        heights = {}

        left_height = get_tree_depth(root.left)
        right_height = get_tree_depth(root.right)

        return abs(left_height - right_height) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

s = Solution()
root = TreeNode(5)
left = TreeNode(2)
right = TreeNode(3)

root.left = left
root.right = right

s.isBalanced(root)