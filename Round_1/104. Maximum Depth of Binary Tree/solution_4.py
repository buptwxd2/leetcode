# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # Recursive DFS
        if not root:
            return 0

        max_depth = 1

        def dfs(root, depth):
            nonlocal max_depth

            if depth > max_depth:
                max_depth = depth

            if root.left:
                dfs(root.left, depth + 1)
            if root.right:
                dfs(root.right, depth + 1)

        dfs(root, 1)

        return max_depth


"""
Results:
Recursive DFS
Runtime: 48 ms, faster than 26.68% of Python3 online submissions for Maximum Depth of Binary Tree.
Memory Usage: 15.9 MB, less than 10.35% of Python3 online submissions for Maximum Depth of Binary Tree.
"""