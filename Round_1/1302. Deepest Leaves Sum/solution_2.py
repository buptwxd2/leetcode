# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        # Recursive dfs

        results = {}

        def dfs(root, depth):
            results.setdefault(depth, []).append(root.val)

            if root.left:
                dfs(root.left, depth + 1)

            if root.right:
                dfs(root.right, depth + 1)

        dfs(root, 0)

        max_depth = max(results.keys())

        return sum(results[max_depth])