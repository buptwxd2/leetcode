# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return 0

        all_leaves = []

        def dfs(root, level):
            nonlocal all_leaves

            if not root.left and not root.right:
                all_leaves.append([root.val, level])
                return

            if root.left:
                dfs(root.left, level + 1)

            if root.right:
                dfs(root.right, level + 1)

        dfs(root, 0)

        deepest_level = max(all_leaves, key=lambda x: x[1])[1]

        return sum(val for val, lvl in all_leaves if lvl == deepest_level)