# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # dfs
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        min_depth = float('inf')

        def dfs(root, curr_depth):
            nonlocal min_depth

            if not root.left and not root.right:
                if curr_depth < min_depth:
                    min_depth = curr_depth

                return

            else:
                curr_depth += 1
                if root.left:
                    dfs(root.left, curr_depth)
                if root.right:
                    dfs(root.right, curr_depth)

        dfs(root, 1)

        return min_depth


"""
Results:
DFS
Runtime: 44 ms, faster than 80.28% of Python3 online submissions for Minimum Depth of Binary Tree.
Memory Usage: 15.8 MB, less than 18.17% of Python3 online submissions for Minimum Depth of Binary Tree.
"""