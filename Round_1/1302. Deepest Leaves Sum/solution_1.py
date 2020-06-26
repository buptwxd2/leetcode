# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        # dfs + stack

        my_stack = []
        results = {}

        # initialize
        my_stack.append([root, 0])
        results[0] = [root.val]

        while my_stack:
            node, level = my_stack.pop(-1)

            results.setdefault(level, []).append(node.val)

            if node.left:
                my_stack.append([node.left, level + 1])
            if node.right:
                my_stack.append([node.right, level + 1])

        max_depth = max(results.keys())

        return sum(results[max_depth])

