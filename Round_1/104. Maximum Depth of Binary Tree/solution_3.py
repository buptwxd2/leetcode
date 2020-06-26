# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # dfs + stack
        if not root:
            return 0

        my_stack = []
        max_depth = 0

        # initialize
        my_stack.append([root, 1])

        while my_stack:
            node, depth = my_stack.pop(-1)

            if depth > max_depth:
                max_depth = depth

            if node.left:
                my_stack.append([node.left, depth + 1])
            if node.right:
                my_stack.append([node.right, depth + 1])

        return max_depth

"""
Results:
DFS + Stack
Runtime: 56 ms, faster than 13.95% of Python3 online submissions for Maximum Depth of Binary Tree.
Memory Usage: 14.9 MB, less than 93.10% of Python3 online submissions for Maximum Depth of Binary Tree.
"""